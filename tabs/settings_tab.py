import sys
import os
import csv
import re
from pebble import concurrent

from PyQt5.QtWidgets import QWidget, QColorDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont, QPixmap


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from designs.python.settings_tab import Ui_Settings_tab

from widgetStyles.Label import Label
from widgetStyles.PushButton import PushButton
from widgetStyles.QCheckBox import SettingsCheckBox
from widgetStyles.ComboBox import ComboBox
from widgetStyles.ScrollBar import ScrollBar

from utils.updateSVG import change_color
from utils.message import Message
from utils.helpers import StyleSheet
from database.model import Model

from windows.timer_window import Timer
from windows.login_window import Login

from integrations.calendar.c import Google_calendar


DESKTOP = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))


class SettingsTab(QWidget, Ui_Settings_tab):
    settings_signal = pyqtSignal(str)
    def __init__(self):
        super(SettingsTab, self).__init__()
        self.setupUi(self)
        self.read_styles()
        self.logged_in = False
        settings = Model().read('settings')[0]

        self.chkbox_nightmode.setChecked(settings[1])
        self.chkbox_vault.setChecked(settings[4])
        self.chkbox_calendar.setChecked(settings[6])
        
        self.chkbox_nightmode.stateChanged.connect(self.set_night_mode)
        self.btn_color.clicked.connect(self.set_color)
        self.fcmbx_font.currentFontChanged.connect(self.get_font)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_export_apps.clicked.connect(lambda: self.export_data("apps"))
        self.btn_export_notes.clicked.connect(lambda: self.export_data("notes"))
        self.btn_import_apps.clicked.connect(lambda: self.import_data("apps"))
        self.btn_import_notes.clicked.connect(lambda: self.import_data("notes"))
        self.chkbox_vault.stateChanged.connect(self.vault)
        self.btn_vault_timer.clicked.connect(self.vault_timer)
        self.chkbox_calendar.stateChanged.connect(self.calendar_toggle)

        self.settings_signal.connect(self.read_styles)    
    
    def create_tab(self):
        return self

    # color is at index 3 and nightmode is at index 1
    def set_night_mode(self):
        toggle = self.chkbox_nightmode
        settings = Model().read("settings")[0]
        color = settings[3]

        if toggle.isChecked() and color == "#000000":
            Message("You cannot activate nightmode if the default color is black.", "Please select a color.").exec_()
            toggle.setChecked(False)
            toggle.setCheckState(Qt.Unchecked)
        elif toggle.isChecked() and color != "#000000":
            Model().update("settings", {'nightmode': 1}, 'settings')
            self.settings_signal.emit("settings changed")
            self.updateWindow()
        elif not toggle.isChecked():
            Model().update("settings", {'nightmode': 0}, 'settings')
            self.settings_signal.emit("settings changed")
            self.updateWindow()


    def get_font(self):
        font = self.fcmbx_font.currentFont().family()
        Model().update("settings", {'font': font}, 'settings')
        self.settings_signal.emit("settings changed")
    
    def set_font(self):
        font = Model().read('settings')[0][2]
        widget_list = [
            self.lbl_color,
            self.lbl_night_mode,
            self.lbl_font,
            self.btn_color,
            self.btn_export_apps,
            self.btn_export_notes,
            self.btn_import_apps,
            self.btn_import_notes,
            self.btn_reset,
            self.btn_vault_timer,
            self.lbl_calendar,
            self.lbl_vault,
            self.lbl_vault_timer,
            self.lbl_reset
        ]
        for i in range(len(widget_list)):
            widget_list[i].setFont(QFont(font))
        

    def set_color(self):
        old_color = Model().read('settings')[0][3]
        new_color = QColorDialog().getColor().name()
        if new_color != "#000000":
            Model().update("settings", {'color': new_color}, 'settings')
            change_color(old_color, new_color)
            self.settings_signal.emit("settings changed")

    def reset(self):
        old_color = Model().read('settings')[0][3]
        change_color(old_color, "#000000")
        Model().reset()
        self.settings_signal.emit("settings changed")
        self.chkbox_nightmode.setChecked(False)
    
    def updateWindow(self):
        self.read_styles()
        self.settings_signal.emit("settings")

    def read_styles(self):
        styles = [Label, PushButton, SettingsCheckBox, ComboBox, ScrollBar]
        stylesheet = StyleSheet(styles).create()
        self.setStyleSheet(stylesheet)
        self.set_font()
        self.set_pic()
        


    def export_data(self, table):
        data = Model().read(table)
        if table == "apps":
            def get_website(app):
                website = re.search("^[http(s)?://|www\.]", app[2])
                if website is not None:
                    return app
            data = list(filter(get_website, data))
                
        if len(data) > 0:
            headings = ["name", "path"] if table == "apps" else ["name", "body"]
            with open(f"{DESKTOP}/{table}.csv", 'w', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(headings)
                for i in range(len(data)):
                    row = [data[i][1], data[i][2]]
                    writer.writerow(row)

    def import_data(self, table):
        file = QFileDialog.getOpenFileName(self, f"Choose the {table}.csv file", DESKTOP, f"csv files ({table}.csv)")[0]
        field = "body" if table == "notes" else "path"
        fields = []
        with open(file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            if header[1] != field:
                Message("The File does not match the data you want to import. Please ensure you don't change the name of the csv file or import the wrong file.", "File doesn't match data").exec_()
                return
            else:
                for row in reader:
                    fields.append(row)
                if table == "notes":
                    for item in fields:
                        data = {
                            header[0]: item[0],
                            header[1]: item[1]
                        }
                        Model().save(table, data)
                        self.settings_signal.emit("settings")
                elif table == "apps":
                    apps = Model().read("apps")
                    for i in range(len(fields)):
                        data = {
                            header[0]: fields[i][0],
                            header[1]: fields[i][1],
                            'sequence': len(apps) + (i + 1)
                        }
                        Model().save(table, data)
                        self.settings_signal.emit("settings")
    
    def vault(self):
        toggle = self.chkbox_vault
        if not toggle.isChecked():
            login = Login()
            login.login_status.connect(self.login)
            login.exec_()
            if not self.logged_in:
                toggle.setChecked(True)
                toggle.setCheckState(Qt.Checked)
            else:
                self.logged_in = False
        self.updateWindow()
            

    def vault_timer(self):
        vault_on = Model().read("settings")[0][4]
        if not vault_on:
            Message("The vault is not active, please turn on the vault in order to set the timer.", "The vault is off.").exec_()
        elif vault_on:
            login = Login()
            login.login_status.connect(self.login)
            login.exec_()
            if self.logged_in:
                Timer().exec_()
    
    def login(self, signal):
        if signal == "success":
            self.logged_in = True

    def calendar_toggle(self):
        toggle = self.chkbox_calendar
        if toggle.isChecked():
            google_thread()
            Model().update("settings", {"calendar": 1}, "settings")
        elif not toggle.isChecked():
            Model().update("settings", {"calendar": 0}, "settings")

    def set_pic(self):
        pic = QPixmap("./assets/settings_logo.png").scaled(400, 400)
        self.lbl_logo.setPixmap(pic)
        

            
            
@concurrent.process(timeout=30)
def google_thread():
    Google_calendar.connect()
    
        


        
