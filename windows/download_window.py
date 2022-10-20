import sys
import os

from utils.globals import PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from zipfile import ZipFile

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QIcon

from utils.helpers import StyleSheet, set_font
from utils.message import Message

from widgetStyles.Dialog import Dialog
from widgetStyles.Label import Label

from designs.python.download_window import Ui_DownloadDialog

from threads.update_trustlock import update_trustlock


class DownloadWindow(Ui_DownloadDialog, QDialog):
    close_app = pyqtSignal(bool)    
    
    def __init__(self) -> None:
        super(DownloadWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowIcon(QIcon(":/other/app_icon"))
        self.set_style()
        update_trustlock(self)
        
    def cancel_update(self):
        # TODO: Update the database to show that you already tried to update today
        self.hide()
        Message("The update was unsuccessful.", "update Failed").exec_()
        self.close()
        
    def set_style(self):
        widget_list = [
            Dialog,
            Label
        ]
        
        stylesheet = StyleSheet(widget_list).create()
        self.setStyleSheet(stylesheet)
        
        font_list = [
            self.lbl_message,
            self.lbl_no_close,
            self.bar_download
        ]
        set_font(font_list)
    
    def update_trustlock_progress(self, value):
        self.bar_download.setValue(value)
        
    def update_state(self, state):
        self.lbl_message.setText(state)
        
    def open_zip(self):
        self.update_state("Extracting Data...")
        
        # with ZipFile("./update.zip", "r") as zip:
        #     zip.extractall()
        # self.update_state("Finished Extracting.")
        
        os.remove("./update.zip")
        
        # try:
        #     os.startfile(PATH+ "\\TrustLock Installer.exe")
        # except:
        #     pass
        
        # self.close_app.emit(True)