import sys
import os
import re
import math
from json import dumps, load, loads
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QWidget, QGridLayout

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from designs.python.crypto_vault_window import Ui_CryptoVault

from widgetStyles.Dialog import Dialog
from widgetStyles.ComboBox import ComboBox
from widgetStyles.Label import Label
from widgetStyles.PushButton import PushButton
from widgetStyles.LineEdit import LineEdit

from utils.helpers import StyleSheet, clear_window
from utils.message import Message

from database.model import Model

class CryptoVaultWindow(Ui_CryptoVault, QDialog):
    def __init__(self, secret):
        super(CryptoVaultWindow, self).__init__()
        self.setupUi(self)
        self.displayWordBoxes()
        self.read_styles()

        self.secret: tuple or None = secret
        if self.secret: self.fill_data()

        self.cmb_num_words.currentIndexChanged.connect(self.update)
        self.btn_save.clicked.connect(self.save)

    def read_styles(self):
        widget_list = [
            Dialog,
            ComboBox,
            Label,
            PushButton,
            LineEdit
        ]
        self.setMinimumHeight(750)
        stylesheet = StyleSheet(widget_list).create()

        self.setStyleSheet(stylesheet)

    def displayWordBoxes(self):
        words: int = self.get_num_words()

        COLUMNS: int = 3
        count: int = 1
        for i in range(math.ceil(words/COLUMNS)):
            subarr = []
            print(i)
            for j in range(COLUMNS):
                hbox: QHBoxLayout = QHBoxLayout()
                widget: QWidget = QWidget()
                widget.setMinimumWidth(300)

                number: QLabel = QLabel(f"{str(count).zfill(2)}. ")
                field: QLineEdit = QLineEdit()

                widget.setLayout(hbox)

                hbox.addWidget(number)
                hbox.addWidget(field)

                if(count > words):
                    break
                self.gbox_words.addWidget(widget, i, j)
                count += 1

        

    def update(self) -> None:
        clear_window(self.gbox_words)
        self.displayWordBoxes()
        self.read_styles()

    def save(self) -> None:
        password1: str = self.lne_password1.text()
        password2: str = self.lne_password2.text()

        description:str = self.lne_description.text()
        username: str = self.lne_name.text()
        num_words: int = self.get_num_words()
        words_layout: QGridLayout = self.gbox_words
        words: list[str] = []

        valid_submit: bool = True

        for i in range(words_layout.count()):
            line_edit: QLineEdit = words_layout.itemAt(i).widget().layout().itemAt(1).widget()
            word: str = line_edit.text()
            if(not word):
                Message(f"There is no word in block {i + 1}.", "Missing Word")
                valid_submit = False
            words.append(word)


        if(password1 and (password1 != password2)):
            Message("The passwords don't match", "Passwords Incorrect").exec_()
            valid_submit = False

        if(not description): 
            valid_submit = False
            Message("Please Provide a description", "No Description").exec_()
        if(not username): 
            valid_submit = False
            Message("Please Provide a username", "No Username").exec_()
        
        if(valid_submit):
            data: str = dumps({
                'name': username,
                'num_words': num_words,
                'words': " ".join(words),
                'description': description,
                'password': password1
            })

            Model().save("vault", {'type': 'crypto', 'name': description, 'data': data})
            self.close()
    
    def get_num_words(self) -> int:
        num_words: str = self.cmb_num_words.currentText()
        # Get the start and end index matching the regex 
        (start, end) = re.match("^\d+", num_words).span()
        # Get the number of words that needs to be represented
        words: int = int(num_words[start: end])

        return words

    def fill_data(self):
        data: object = loads(self.secret[3])
        self.lne_description.setText(data['description'])
        self.lne_password1.setText(data['password'])
        self.lne_password2.setText(data['password'])
        self.lne_name.setText(data['name'])
        
        words = self.gbox_words
        db_words: list[str] = data['words'].split(" ")

        for i in range(words.count()):
            words.itemAt(i).widget().layout().itemAt(1).widget().setText(db_words[i])
