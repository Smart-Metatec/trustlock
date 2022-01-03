import sys
import os

from PyQt5.QtWidgets import QDial, QDialog, QLineEdit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from designs.python.register_window import Ui_Register
from utils.message import Message
from database.model import Model
from utils.helpers import StyleSheet

from widgetStyles.PushButton import PushButton
from widgetStyles.LineEdit import LineEdit
from widgetStyles.Label import Label
from widgetStyles.Dialog import Dialog

class Register(QDialog, Ui_Register):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.lnedt_password.setEchoMode(QLineEdit.Password)
        self.lnedt_password2.setEchoMode(QLineEdit.Password)
        self.read_styles()
        self.btn_register.clicked.connect(self.register_clicked)

    def register_clicked(self):
        name = self.lnedt_name.text()
        email = self.lnedt_email.text()
        password1 = self.lnedt_password.text()
        password2 = self.lnedt_password2.text()
        question = self.lnedt_question.text()
        answer = self.lnedt_answer.text()

        fields = [
            name,
            email,
            password1,
            password2,
            question,
            answer
        ]

        valid_submition = False
        
        for field in fields:
            if not field:
                Message(f"Make sure you fill in all the fields.", "Please fill in all the fields").exec_()
                break
            else:
                valid_submition = True

        if password1 != password2:
            Message("Please make sure your passwords match. Check to see if your caps lock is on", "Passwords don't match").exec_()
        elif valid_submition:
            data = {
                "name": name,
                "email": email,
                "password": password1,
                "question": question,
                "answer": answer
            }

            Model().save("user", data)
            self.close()

    def read_styles(self):
        styles = [
            PushButton,
            Label,
            LineEdit,
            Dialog
        ]

        stylesheet = StyleSheet(styles).create()
        self.setStyleSheet(stylesheet)



