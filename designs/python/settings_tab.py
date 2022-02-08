# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_tab(object):
    def setupUi(self, Settings_tab):
        Settings_tab.setObjectName("Settings_tab")
        Settings_tab.resize(949, 618)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Settings_tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_login = QtWidgets.QLabel(Settings_tab)
        self.lbl_login.setObjectName("lbl_login")
        self.horizontalLayout_6.addWidget(self.lbl_login)
        self.btn_login = QtWidgets.QPushButton(Settings_tab)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_6.addWidget(self.btn_login)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.hbox_night_mode = QtWidgets.QHBoxLayout()
        self.hbox_night_mode.setObjectName("hbox_night_mode")
        self.lbl_night_mode = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_night_mode.sizePolicy().hasHeightForWidth())
        self.lbl_night_mode.setSizePolicy(sizePolicy)
        self.lbl_night_mode.setMinimumSize(QtCore.QSize(100, 50))
        self.lbl_night_mode.setObjectName("lbl_night_mode")
        self.hbox_night_mode.addWidget(self.lbl_night_mode)
        self.chkbox_nightmode = QtWidgets.QCheckBox(Settings_tab)
        self.chkbox_nightmode.setText("")
        self.chkbox_nightmode.setObjectName("chkbox_nightmode")
        self.hbox_night_mode.addWidget(self.chkbox_nightmode)
        self.verticalLayout.addLayout(self.hbox_night_mode)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_vault = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_vault.sizePolicy().hasHeightForWidth())
        self.lbl_vault.setSizePolicy(sizePolicy)
        self.lbl_vault.setMinimumSize(QtCore.QSize(100, 50))
        self.lbl_vault.setObjectName("lbl_vault")
        self.horizontalLayout_2.addWidget(self.lbl_vault)
        self.chkbox_vault = QtWidgets.QCheckBox(Settings_tab)
        self.chkbox_vault.setText("")
        self.chkbox_vault.setObjectName("chkbox_vault")
        self.horizontalLayout_2.addWidget(self.chkbox_vault)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_vault_timer = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_vault_timer.sizePolicy().hasHeightForWidth())
        self.lbl_vault_timer.setSizePolicy(sizePolicy)
        self.lbl_vault_timer.setMinimumSize(QtCore.QSize(100, 50))
        self.lbl_vault_timer.setObjectName("lbl_vault_timer")
        self.horizontalLayout_3.addWidget(self.lbl_vault_timer)
        self.btn_vault_timer = QtWidgets.QPushButton(Settings_tab)
        self.btn_vault_timer.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_vault_timer.setObjectName("btn_vault_timer")
        self.horizontalLayout_3.addWidget(self.btn_vault_timer)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.hbox_font = QtWidgets.QHBoxLayout()
        self.hbox_font.setObjectName("hbox_font")
        self.lbl_font = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_font.sizePolicy().hasHeightForWidth())
        self.lbl_font.setSizePolicy(sizePolicy)
        self.lbl_font.setMinimumSize(QtCore.QSize(100, 50))
        self.lbl_font.setObjectName("lbl_font")
        self.hbox_font.addWidget(self.lbl_font)
        self.fcmbx_font = QtWidgets.QFontComboBox(Settings_tab)
        self.fcmbx_font.setMinimumSize(QtCore.QSize(100, 25))
        self.fcmbx_font.setObjectName("fcmbx_font")
        self.hbox_font.addWidget(self.fcmbx_font)
        self.verticalLayout.addLayout(self.hbox_font)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_calendar = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_calendar.sizePolicy().hasHeightForWidth())
        self.lbl_calendar.setSizePolicy(sizePolicy)
        self.lbl_calendar.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_calendar.setObjectName("lbl_calendar")
        self.horizontalLayout_4.addWidget(self.lbl_calendar)
        self.chkbox_calendar = QtWidgets.QCheckBox(Settings_tab)
        self.chkbox_calendar.setText("")
        self.chkbox_calendar.setObjectName("chkbox_calendar")
        self.horizontalLayout_4.addWidget(self.chkbox_calendar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.hbox_export = QtWidgets.QHBoxLayout()
        self.hbox_export.setObjectName("hbox_export")
        self.btn_export_apps = QtWidgets.QPushButton(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.btn_export_apps.sizePolicy().hasHeightForWidth())
        self.btn_export_apps.setSizePolicy(sizePolicy)
        self.btn_export_apps.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_export_apps.setObjectName("btn_export_apps")
        self.hbox_export.addWidget(self.btn_export_apps)
        self.btn_export_notes = QtWidgets.QPushButton(Settings_tab)
        self.btn_export_notes.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_export_notes.setObjectName("btn_export_notes")
        self.hbox_export.addWidget(self.btn_export_notes)
        self.verticalLayout.addLayout(self.hbox_export)
        self.hbox_import = QtWidgets.QHBoxLayout()
        self.hbox_import.setObjectName("hbox_import")
        self.btn_import_apps = QtWidgets.QPushButton(Settings_tab)
        self.btn_import_apps.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_import_apps.setObjectName("btn_import_apps")
        self.hbox_import.addWidget(self.btn_import_apps)
        self.btn_import_notes = QtWidgets.QPushButton(Settings_tab)
        self.btn_import_notes.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_import_notes.setObjectName("btn_import_notes")
        self.hbox_import.addWidget(self.btn_import_notes)
        self.verticalLayout.addLayout(self.hbox_import)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_reset = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_reset.sizePolicy().hasHeightForWidth())
        self.lbl_reset.setSizePolicy(sizePolicy)
        self.lbl_reset.setMinimumSize(QtCore.QSize(100, 50))
        self.lbl_reset.setObjectName("lbl_reset")
        self.horizontalLayout.addWidget(self.lbl_reset)
        self.btn_reset = QtWidgets.QPushButton(Settings_tab)
        self.btn_reset.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)

        self.retranslateUi(Settings_tab)
        QtCore.QMetaObject.connectSlotsByName(Settings_tab)

    def retranslateUi(self, Settings_tab):
        _translate = QtCore.QCoreApplication.translate
        Settings_tab.setWindowTitle(_translate("Settings_tab", "Form"))
        self.lbl_login.setText(_translate("Settings_tab", "Login"))
        self.btn_login.setText(_translate("Settings_tab", "Login"))
        self.lbl_night_mode.setText(_translate("Settings_tab", "Night Mode"))
        self.lbl_vault.setText(_translate("Settings_tab", "Vault"))
        self.lbl_vault_timer.setText(_translate("Settings_tab", "Vault Timer"))
        self.btn_vault_timer.setText(_translate("Settings_tab", "Set Timer"))
        self.lbl_font.setText(_translate("Settings_tab", "Font"))
        self.lbl_calendar.setText(_translate("Settings_tab", "Integrate With Google Calendar"))
        self.btn_export_apps.setText(_translate("Settings_tab", "Export Apps"))
        self.btn_export_notes.setText(_translate("Settings_tab", "Export Notes"))
        self.btn_import_apps.setText(_translate("Settings_tab", "Import Apps"))
        self.btn_import_notes.setText(_translate("Settings_tab", "Import Notes"))
        self.lbl_reset.setText(_translate("Settings_tab", "Reset Settings"))
        self.btn_reset.setText(_translate("Settings_tab", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings_tab = QtWidgets.QWidget()
    ui = Ui_Settings_tab()
    ui.setupUi(Settings_tab)
    Settings_tab.show()
    sys.exit(app.exec_())
