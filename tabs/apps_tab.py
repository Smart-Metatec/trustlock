import sys
import os
import math

from PyQt5.QtWidgets import QWidget, QFrame,QSizePolicy
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont

from utils.message import Message

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from designs.python.apps_tab import Ui_apps_tab
from database.model import Model

from windows.apps_window import Apps_window
from windows.protected_apps_edit_window import ProtectedApps
from windows.apps_edit_window import AppsEdit
from windows.protected_view_window import ProtectedView

from widgets.app_item import AppItem
from widgetStyles.PushButton import PushButton
from widgetStyles.QCheckBox import CheckBox
from widgetStyles.Line import Line

from utils.helpers import StyleSheet
from utils.helpers import clear_window

class Apps_tab(QWidget, Ui_apps_tab):
    app_signal = pyqtSignal(str)
    table_signal = pyqtSignal(str)
    # This signal is to communicate with the main window where the login will take place
    login_signal = pyqtSignal(str)

    def __init__(self):
        super(Apps_tab, self).__init__()
        self.setupUi(self)
        self.read_styles()


        
        self.create_apps()
        self.create_protected_apps()

        self.btn_add_app.clicked.connect(self.add_app)
        self.chk_edit_apps.stateChanged.connect(self.edit_checked)
        self.chk_delete_apps.stateChanged.connect(self.delete_checked)
        self.chkbox_pro_apps_edit.stateChanged.connect(self.edit_checked)
        self.chkbox_pro_apps_delete.stateChanged.connect(self.delete_checked)
        self.chkbox_pro_apps_view.stateChanged.connect(self.view_checked)
        self.btn_pro_apps_login.clicked.connect(self.login_clicked)

        self.logged_in = False
        
        # Signal slots for external signals
        self.app_signal.connect(self.update)
        # Login signal will run everytime the login signal is updated
        self.login_signal.connect(self.login)
    
    def create_tab(self):
        return self

    def read_styles(self):
        styles = [CheckBox, PushButton, Line]
        stylesheet = StyleSheet(styles).create()
        self.setStyleSheet(stylesheet)
        widgetList = [
            self.btn_add_app,
            self.chk_edit_apps,
            self.chk_delete_apps,
            self.btn_pro_apps_login,
            self.lbl_open_apps,
            self.lbl_pro_apps,
            self.chkbox_pro_apps_delete,
            self.chkbox_pro_apps_edit,
            self.chkbox_pro_apps_view
        ]
        font = Model().read('settings')[0][2]

        for i in range(len(widgetList)):
            widgetList[i].setFont(QFont(font))

        # self.line.setStyleSheet("border: 2px solid green;")

    def add_app(self):
        app_window = Apps_window()
        app_window.app_window_signal.connect(self.update)
        app_window.exec_()
    
    def create_apps(self):
        apps = Model().read('apps')
        COLUMNS = 2
        sorted_apps = sorted(apps, key=lambda item: item[2])
        grid_items = []
        for i in range(math.ceil(len(sorted_apps)/COLUMNS)):
            subarr = []
            for j in range(COLUMNS):
                if sorted_apps:
                    subarr.append(sorted_apps.pop(0))
            grid_items.append(subarr)
        for i in range(len(grid_items)):
            row = i
            for j in range(len(grid_items[i])):
                col = j
                app_button = AppItem(grid_items[i][j]).create()
                app_button.app_clicked_signal.connect(self.get_app)
                self.gbox_apps.addWidget(app_button, row, col)

    def create_protected_apps(self):
        apps = Model().read('protected_apps')
        COLUMNS = 2
        sorted_apps = sorted(apps, key=lambda item: item[COLUMNS])
        grid_items = []
        for i in range(math.ceil(len(sorted_apps)/COLUMNS)):
            subarr = []
            for j in range(COLUMNS):
                if sorted_apps:
                    subarr.append(sorted_apps.pop(0))
            grid_items.append(subarr)
        for i in range(len(grid_items)):
            row = i
            for j in range(len(grid_items[i])):
                col = j
                app_button = AppItem(grid_items[i][j]).create()
                app_button.app_clicked_signal.connect(self.get_app)
                self.gbox_pro_apps.addWidget(app_button, row, col)

    def edit_checked(self):
        delete_apps = self.chk_delete_apps
        edit_apps = self.chk_edit_apps
        pro_delete_apps = self.chkbox_pro_apps_delete
        pro_edit_apps = self.chkbox_pro_apps_edit
        view_toggle = self.chkbox_pro_apps_view

        if delete_apps.isChecked() and edit_apps.isChecked():
            edit_apps.setChecked(True)
            delete_apps.setChecked(False)



        elif pro_delete_apps.isChecked() and pro_edit_apps.isChecked():
            pro_edit_apps.setChecked(True)
            pro_delete_apps.setChecked(False)

        elif pro_edit_apps.isChecked() and view_toggle.isChecked():
            view_toggle.setChecked(False)

            
 

    def delete_checked(self):
        delete_apps = self.chk_delete_apps
        edit_apps = self.chk_edit_apps
        pro_delete_apps = self.chkbox_pro_apps_delete
        pro_edit_apps = self.chkbox_pro_apps_edit
        view_toggle = self.chkbox_pro_apps_view

        if edit_apps.isChecked() and delete_apps.isChecked():
            delete_apps.setChecked(True)
            edit_apps.setChecked(False)


        elif pro_edit_apps.isChecked() and pro_delete_apps.isChecked():
            pro_delete_apps.setChecked(True)
            pro_edit_apps.setChecked(False)

        elif pro_delete_apps.isChecked() and view_toggle.isChecked():
            view_toggle.setChecked(False)

    
    def view_checked(self):
        view_toggle = self.chkbox_pro_apps_view
        edit_toggle = self.chkbox_pro_apps_edit
        delete_toggle = self.chkbox_pro_apps_delete


        if view_toggle.isChecked() and edit_toggle.isChecked():
            view_toggle.setChecked(True)
            edit_toggle.setChecked(False)
        elif view_toggle.isChecked() and delete_toggle.isChecked():
            view_toggle.setChecked(True)
            delete_toggle.setChecked(False)

            
    
    # Handles the editing and deleting of the apps
    def get_app(self, app):
        delete = self.chk_delete_apps
        edit = self.chk_edit_apps
        pro_delete = self.chkbox_pro_apps_delete
        pro_edit = self.chkbox_pro_apps_edit
        view_toggle = self.chkbox_pro_apps_view
        is_protected_app = True if len(app) > 4 else False

        if delete.isChecked() and not is_protected_app:
            Model().delete('apps', app[0])
            self.update()
            delete.setChecked(False)
            
        elif edit.isChecked() and not is_protected_app:
            app_window = AppsEdit(app)
            app_window.app_edit_window_signal.connect(self.update)
            app_window.exec_()
            edit.setChecked(False)
        # app[4] tests to see if the app is open or protected
        elif pro_delete.isChecked() and is_protected_app and self.logged_in:
            Model().delete('protected_apps', app[0])
            self.update()
            pro_delete.setChecked(False)
        # app[4] tests to see if the app is open or protected
        elif pro_edit.isChecked() and is_protected_app and self.logged_in:
            app_window = ProtectedApps(app)
            app_window.protected_app_window_signal.connect(self.update)
            app_window.exec_()
            pro_edit.setChecked(False)
        elif view_toggle.isChecked() and is_protected_app and self.logged_in:
            view_window = ProtectedView(app, "app")
            view_window.exec_()
            view_toggle.setChecked(False)
        elif is_protected_app and not self.logged_in:
            Message("Please login before you can access the content of this app", "Restricted App").exec_()
        else:
            try:
                if is_protected_app and self.logged_in:
                    os.startfile(app[2])
                elif not is_protected_app:
                    os.startfile(app[2])
            except OSError:
                pass


    def update(self):
        clear_window(self.gbox_apps)
        clear_window(self.gbox_pro_apps)
        self.create_apps()
        self.create_protected_apps()
        self.read_styles()

    def login_clicked(self):
        if self.logged_in:
            self.login_signal.emit("logout requested")
        elif not self.logged_in:
            self.login_signal.emit("login requested")


    def login(self, signal):
        if signal == "logged in":
            self.btn_pro_apps_login.setText("Logout")
            self.logged_in = True
        elif signal == "logged out":
            self.btn_pro_apps_login.setText("login")
            self.logged_in = False



        

