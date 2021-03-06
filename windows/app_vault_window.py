import sys
import os
from json import dumps
from datetime import date, datetime, timedelta

from PyQt5.QtWidgets import QDialog, QFileDialog, QLineEdit, QWidget
from PyQt5.QtCore import pyqtSignal, Qt, pyqtSlot, QSize
from PyQt5.QtGui import QFont, QIcon

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

DESKTOP = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'))

from designs.python.app_vault_window import Ui_AppVault

from widgetStyles.Dialog import Dialog
from widgetStyles.PushButton import PushButton, IconToolButton
from widgetStyles.LineEdit import LineEdit
from widgetStyles.Label import Label
from widgetStyles.SpinBox import SpinBox
from widgetStyles.DateEdit import DateEditForm
from widgetStyles.Calendar import Calendar

from utils.helpers import StyleSheet, json_to_dict, get_checkbox, set_font
from utils.message import Message

from database.model import Model

from windows.generate_password import GeneratePasswordWindow

class AppVaultWindow(Ui_AppVault, QDialog):
    app_update_signal = pyqtSignal(bool)
    def __init__(self, app=None):
        super(Ui_AppVault, self).__init__()
        self.app = app
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon(":/other/app_icon"))
        self.secrets = list(filter(lambda a: a[1] == "app", Model().read("vault")))
        self.setupUi(self)
        self.set_groups()
        
        self.dte_password_exp.setDate(date.today() + timedelta(days=90))
        
        # Get the current apps to avoid collisions
        self.current_apps = self.get_current_apps()
        
        maxValue = len(self.secrets) if self.app else len(self.secrets)+1
        
        self.spn_index.setMaximum(maxValue)
        self.spn_index.setValue(maxValue)
        self.spn_index.setMinimum(1)
        self.lne_password.setEchoMode(QLineEdit.Password)
        

        if self.app: self.fill_data()
        
        self.read_styles()
        self.btn_save.clicked.connect(self.save)
        self.btn_desktop.clicked.connect(self.add_from_desktop)
        self.tbtn_password_generator.clicked.connect(self.generate_password)
        
        self.chk_show_password.stateChanged.connect(lambda show: self.show_password(show, self.lne_password))
        self.chk_password2.stateChanged.connect(lambda show: self.show_password(show, self.lne_password2))
    
    def set_groups(self):
        groups = Model().read("groups")
        
        for i in range(len(groups)):
            self.cmb_group.addItem(groups[i][1], groups[i][0])
            if self.app and int(self.app[4]) == groups[i][0]:
                self.cmb_group.setCurrentIndex(i)
    
    @pyqtSlot()
    def generate_password(self):
        GeneratePasswordWindow().exec_()
        

    def read_styles(self):
        checkbox = get_checkbox()
        widget_list = [
            Label,
            Dialog,
            PushButton,
            LineEdit,
            SpinBox,
            checkbox,
            Calendar,
            DateEditForm,
            IconToolButton()
        ]

        stylesheet: str = StyleSheet(widget_list).create()
        self.setStyleSheet(stylesheet)
        
        self.tbtn_password_generator.setIcon(QIcon(":/button_icons/password"))
        self.tbtn_password_generator.setIconSize(QSize(30, 20))
        
        font_widget = [
            self.lbl_email,         self.lbl_index,
            self.lbl_name,          self.lbl_password,
            self.lbl_path,          self.lbl_username,
            self.lne_email,         self.spn_index,
            self.lne_name,          self.lne_password,
            self.lne_path,          self.lne_username,
            self.btn_desktop,       self.btn_save,
            self.lbl_password2,     self.lne_password2,
            self.lbl_password_generator,
            self.lbl_password_expiration,
            self.dte_password_exp,
        ]
        
        set_font(font_widget)

    def save(self):
        
        name: str = self.lne_name.text()
        index: str = self.spn_index.text()
        path: str = self.lne_path.text()

        username: str = self.lne_username.text()
        email: str = self.lne_email.text()
        password: str = self.lne_password.text()
        confirm_password: str = self.lne_password2.text()
        password_exp = self.dte_password_exp.date().toPyDate()
        
        group = self.cmb_group.currentData()
        
        password_exp_string = datetime.strftime(password_exp, "%Y-%m-%d")

        name_list: list[str] = ["name", "index", "path", "username", "email", "password"]
        data_list: list[str] = [ name, index, path, username, email, password ]

        valid_submit: bool = True

        for i in range(len(data_list)):
            if(not data_list[i]):
                Message(f"Please add {name_list[i]}", f"Missing {name_list[i]}").exec_()
                valid_submit = False
                
        if not self.app and name in self.current_apps:
            Message(f"An App with this name already exists", "App already exists").exec_()
            valid_submit = False

        if valid_submit:
            data: str = dumps({
                'name': name,
                'sequence': index,
                'path': path,
                'username': username,
                'email': email,
                'password': password,
                'password_exp': password_exp_string,
            })
            
            if password != confirm_password:
                Message("The password and confirm password are not the same.", "Passwords don't match").exec_()
                return "Stop this method from further execution"
            
            if int(index) < len(self.secrets):
                # print(f"current index: {index}")
                self.update_sequence(str(index))
                
            payload = {
                'type': 'app', 
                'name': name, 
                'data': data,
                'group_id': group                
            }

            if self.app:
                Model().update("vault", payload, self.app[0])
            else:
                Model().save("vault", payload)
                
                
                
            self.app_update_signal.emit(True)
            self.close()
    
    def fill_data(self):
        
        self.btn_save.setText("Update")
        self.setWindowTitle("Update App")
        
        data: object = json_to_dict(self.app[3])
        
        self.lne_name.setText(data['name'])
        self.lne_password.setText(data['password'])
        self.lne_password2.setText(data['password'])
        self.lne_email.setText(data['email'])
        self.lne_username.setText(data['username'])
        self.lne_path.setText(data['path'])
        self.spn_index.setValue(int(data['sequence']))
        
        # Get the datetime object from string
        password_exp_datetime: datetime = datetime.strptime(data['password_exp'], "%Y-%m-%d")
        
        # Get the date object from datetime object
        password_exp_date: date = date(password_exp_datetime.year, password_exp_datetime.month, password_exp_datetime.day)
        
        # Set the date
        self.dte_password_exp.setDate(password_exp_date)
        
    def add_from_desktop(self):
        file = QFileDialog.getOpenFileName(self, "Open a file", DESKTOP, "All Files (*.*)")[0]
        self.lne_path.setText(file)
        
    def update_sequence(self, index: str):
        # Get the app that needs to be updated
        update_app = list(filter(lambda a: json_to_dict(a[3])['sequence'] == index, self.secrets))[0]
        # Get the data from the app that needs to be updated
        update_app_data = json_to_dict(update_app[3])
        # The app was edited
        if self.app:
            # Get the data from the current app being updated
            data = json_to_dict(self.app[3])
            # Get the sequence to put in the app the needs to be updated
            new_sequence = data['sequence']
            update_app_data['sequence'] = new_sequence
            Model().update("vault", {'data': dumps(update_app_data)}, update_app[0])
        # It's a new app
        else:
            # its a new app
            update_app_data['sequence'] = str(len(self.secrets)+1)
            Model().update("vault", {'data': dumps(update_app_data)}, update_app[0])
            
    def show_password(self, show, field):
        if show: field.setEchoMode(QLineEdit.Normal)
        else: field.setEchoMode(QLineEdit.Password)
        
    def get_current_apps(self):
        vault_items: list[list[int, str, str, str]] = Model().read("vault")
        current_app_list = list(filter(lambda item: item[1] == "app", vault_items))
        
        current_apps: object = {}
        
        for app in current_app_list:
            current_apps[app[2]] = app
            
        return current_apps