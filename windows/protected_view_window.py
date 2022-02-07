import sys
import os
import json

from PyQt5.QtWidgets import QDialog,QHBoxLayout, QRadioButton, QLabel, QFrame
from cryptography.fernet import Fernet

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from designs.python.protected_view_window import Ui_ProtectedView

from widgetStyles.PushButton import PushButton
from widgetStyles.Label import Label
from widgetStyles.Dialog import Dialog
from widgetStyles.RadioButton import RadioButton
from widgetStyles.Line import Line

from utils.helpers import StyleSheet


class ProtectedView(QDialog, Ui_ProtectedView):
    def __init__(self, item, type):
        super(ProtectedView, self).__init__()
        self.setupUi(self)
        self.read_styles()
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)

        # This is a tuple of an entry from the database
        self.item = item
        self.type = type
        
        # Format the data and add display it on screen
        self.display_item(self.format_data())

    def read_styles(self):
        styles = [
            PushButton,
            Label,
            Dialog,
            RadioButton,
            Line
        ]

        stylesheet = StyleSheet(styles).create()
        self.setStyleSheet(stylesheet)

    def display_item(self, data):
        container = self.vbox_data
        for i in range(len(data)):
            hbox = QHBoxLayout()

            radio_label = QRadioButton(data[i][0])
            data_entry = QLabel(data[i][1])

            hbox.addWidget(radio_label)
            hbox.addWidget(data_entry)

            container.addLayout(hbox)

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)

            container.addWidget(line)
    
    def format_data(self):
        data = []
        if self.type == 'secret':
            f = Fernet(self.item[3])

            data = json.loads(f.decrypt(self.item[2]).decode('UTF-8'))
        elif self.type == "app":
            app = list(self.item)
            # Remove the id of the app
            app.pop(0)
            # Remove the index of the app
            app.pop(2)
            LABELS = ["Name", "URL", "Username", "Email", "Password"]
            for i in range(len(app)):
                data.append([LABELS[i], app[i]])
        
        return data
