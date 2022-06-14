import sys
import os
from json import dumps

from PyQt5.QtWidgets import QDialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from designs.python.app_vault_window import Ui_AppVault

from widgetStyles.Dialog import Dialog
from widgetStyles.PushButton import PushButton
from widgetStyles.LineEdit import LineEdit
from widgetStyles.Label import Label
from widgetStyles.SpinBox import SpinBox

from utils.helpers import StyleSheet
from utils.message import Message

from database.model import Model

class AppVaultWindow(Ui_AppVault, QDialog):
    def __init__(self):
        super(Ui_AppVault, self).__init__()
        self.setupUi(self)
        self.read_styles()

        self.btn_save.clicked.connect(self.save)

    def read_styles(self):
        widget_list = [
            Label,
            Dialog,
            PushButton,
            LineEdit,
            SpinBox
        ]

        stylesheet: str = StyleSheet(widget_list).create()
        self.setStyleSheet(stylesheet)

    def save(self):
        name: str = self.lne_name.text()
        index: str = self.spn_index.text()
        path: str = self.lne_path.text()

        username: str = self.lne_username.text()
        email: str = self.lne_email.text()
        password: str = self.lne_password.text()

        name_list: list[str] = ["name", "index", "path", "username", "email", "password"]
        data_list: list[str] = [ name, index, path, username, email, password ]

        valid_submit: bool = True

        for i in range(len(data_list)):
            if(not data_list[i]):
                Message(f"Please add {name_list[i]}", f"Missing {name_list[i]}").exec_()
                valid_submit = False

        if valid_submit:
            data: str = dumps({
                'name': name,
                'sequence': index,
                'path': path,
                'username': username,
                'email': email,
                'password': password
            })

            Model().save("vault", {
                'type': "app",
                'name': name,
                'data': data
            })
            self.close()