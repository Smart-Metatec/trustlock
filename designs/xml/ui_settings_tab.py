# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\SA Trust PC Big\Desktop\WorkMate 3.0 Pro\designs\xml\settings_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_tab(object):
    def setupUi(self, Settings_tab):
        Settings_tab.setObjectName("Settings_tab")
        Settings_tab.resize(949, 598)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Settings_tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lbl_google_integration = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_google_integration.sizePolicy().hasHeightForWidth())
        self.lbl_google_integration.setSizePolicy(sizePolicy)
        self.lbl_google_integration.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_google_integration.setObjectName("lbl_google_integration")
        self.horizontalLayout_13.addWidget(self.lbl_google_integration)
        self.btn_google = QtWidgets.QToolButton(Settings_tab)
        self.btn_google.setStyleSheet("background-color: transparent;\n"
"padding: 0px;")
        self.btn_google.setObjectName("btn_google")
        self.horizontalLayout_13.addWidget(self.btn_google)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.frame = QtWidgets.QFrame(Settings_tab)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame.setStyleSheet("background:#9ecd16;")
        self.frame.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_2fa = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_2fa.sizePolicy().hasHeightForWidth())
        self.lbl_2fa.setSizePolicy(sizePolicy)
        self.lbl_2fa.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_2fa.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_2fa.setObjectName("lbl_2fa")
        self.horizontalLayout_7.addWidget(self.lbl_2fa)
        self.chkbox_2fa = QtWidgets.QCheckBox(Settings_tab)
        self.chkbox_2fa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbox_2fa.setText("")
        self.chkbox_2fa.setObjectName("chkbox_2fa")
        self.horizontalLayout_7.addWidget(self.chkbox_2fa)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.frame_6 = QtWidgets.QFrame(Settings_tab)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_6.setStyleSheet("background: #9ecd16;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout.addWidget(self.frame_6)
        self.hbox_night_mode = QtWidgets.QHBoxLayout()
        self.hbox_night_mode.setObjectName("hbox_night_mode")
        self.lbl_night_mode = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_night_mode.sizePolicy().hasHeightForWidth())
        self.lbl_night_mode.setSizePolicy(sizePolicy)
        self.lbl_night_mode.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_night_mode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_night_mode.setObjectName("lbl_night_mode")
        self.hbox_night_mode.addWidget(self.lbl_night_mode)
        self.chkbox_nightmode = QtWidgets.QCheckBox(Settings_tab)
        self.chkbox_nightmode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbox_nightmode.setText("")
        self.chkbox_nightmode.setObjectName("chkbox_nightmode")
        self.hbox_night_mode.addWidget(self.chkbox_nightmode)
        self.verticalLayout.addLayout(self.hbox_night_mode)
        self.frame_7 = QtWidgets.QFrame(Settings_tab)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_7.setStyleSheet("background: #9ecd16;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setLineWidth(1)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout.addWidget(self.frame_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_calendar = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_calendar.sizePolicy().hasHeightForWidth())
        self.lbl_calendar.setSizePolicy(sizePolicy)
        self.lbl_calendar.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_calendar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_calendar.setObjectName("lbl_calendar")
        self.horizontalLayout_4.addWidget(self.lbl_calendar)
        self.chkbox_calendar = QtWidgets.QCheckBox(Settings_tab)
        self.chkbox_calendar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chkbox_calendar.setText("")
        self.chkbox_calendar.setObjectName("chkbox_calendar")
        self.horizontalLayout_4.addWidget(self.chkbox_calendar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame_8 = QtWidgets.QFrame(Settings_tab)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_8.setStyleSheet("background: #9ecd16;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout.addWidget(self.frame_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_auto_save = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_auto_save.sizePolicy().hasHeightForWidth())
        self.lbl_auto_save.setSizePolicy(sizePolicy)
        self.lbl_auto_save.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_auto_save.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_auto_save.setObjectName("lbl_auto_save")
        self.horizontalLayout_10.addWidget(self.lbl_auto_save)
        self.btn_auto_save = QtWidgets.QPushButton(Settings_tab)
        self.btn_auto_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_auto_save.setText("")
        self.btn_auto_save.setObjectName("btn_auto_save")
        self.horizontalLayout_10.addWidget(self.btn_auto_save)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.frame_9 = QtWidgets.QFrame(Settings_tab)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_9.setStyleSheet("background: #9ecd16;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout.addWidget(self.frame_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_save_remote = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_save_remote.sizePolicy().hasHeightForWidth())
        self.lbl_save_remote.setSizePolicy(sizePolicy)
        self.lbl_save_remote.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_save_remote.setObjectName("lbl_save_remote")
        self.horizontalLayout_2.addWidget(self.lbl_save_remote)
        self.btn_save_google_drive = QtWidgets.QPushButton(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_google_drive.sizePolicy().hasHeightForWidth())
        self.btn_save_google_drive.setSizePolicy(sizePolicy)
        self.btn_save_google_drive.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_google_drive.setText("")
        self.btn_save_google_drive.setObjectName("btn_save_google_drive")
        self.horizontalLayout_2.addWidget(self.btn_save_google_drive)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame_10 = QtWidgets.QFrame(Settings_tab)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_10.setStyleSheet("background: #9ecd16;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout.addWidget(self.frame_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbl_restore_remote = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_restore_remote.sizePolicy().hasHeightForWidth())
        self.lbl_restore_remote.setSizePolicy(sizePolicy)
        self.lbl_restore_remote.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_restore_remote.setObjectName("lbl_restore_remote")
        self.horizontalLayout_11.addWidget(self.lbl_restore_remote)
        self.btn_google_drive_sync = QtWidgets.QPushButton(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_google_drive_sync.sizePolicy().hasHeightForWidth())
        self.btn_google_drive_sync.setSizePolicy(sizePolicy)
        self.btn_google_drive_sync.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_google_drive_sync.setText("")
        self.btn_google_drive_sync.setObjectName("btn_google_drive_sync")
        self.horizontalLayout_11.addWidget(self.btn_google_drive_sync)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.frame_2 = QtWidgets.QFrame(Settings_tab)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_2.setStyleSheet("background: #9ecd16;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_save_local = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_save_local.sizePolicy().hasHeightForWidth())
        self.lbl_save_local.setSizePolicy(sizePolicy)
        self.lbl_save_local.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_save_local.setObjectName("lbl_save_local")
        self.horizontalLayout_9.addWidget(self.lbl_save_local)
        self.btn_save_local = QtWidgets.QPushButton(Settings_tab)
        self.btn_save_local.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_save_local.setText("")
        self.btn_save_local.setObjectName("btn_save_local")
        self.horizontalLayout_9.addWidget(self.btn_save_local)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.frame_11 = QtWidgets.QFrame(Settings_tab)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_11.setStyleSheet("background: #9ecd16;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout.addWidget(self.frame_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_restore_local = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_restore_local.sizePolicy().hasHeightForWidth())
        self.lbl_restore_local.setSizePolicy(sizePolicy)
        self.lbl_restore_local.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_restore_local.setObjectName("lbl_restore_local")
        self.horizontalLayout_3.addWidget(self.lbl_restore_local)
        self.btn_restore_local = QtWidgets.QPushButton(Settings_tab)
        self.btn_restore_local.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_restore_local.setText("")
        self.btn_restore_local.setObjectName("btn_restore_local")
        self.horizontalLayout_3.addWidget(self.btn_restore_local)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_login = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_login.sizePolicy().hasHeightForWidth())
        self.lbl_login.setSizePolicy(sizePolicy)
        self.lbl_login.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_login.setObjectName("lbl_login")
        self.horizontalLayout_6.addWidget(self.lbl_login)
        self.btn_login = QtWidgets.QPushButton(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setText("")
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_6.addWidget(self.btn_login)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.frame_14 = QtWidgets.QFrame(Settings_tab)
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_14.setStyleSheet("background: #9ecd16;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_2.addWidget(self.frame_14)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbl_update_password = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_update_password.sizePolicy().hasHeightForWidth())
        self.lbl_update_password.setSizePolicy(sizePolicy)
        self.lbl_update_password.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_update_password.setObjectName("lbl_update_password")
        self.horizontalLayout_16.addWidget(self.lbl_update_password)
        self.btn_update_password = QtWidgets.QPushButton(Settings_tab)
        self.btn_update_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_update_password.setText("")
        self.btn_update_password.setObjectName("btn_update_password")
        self.horizontalLayout_16.addWidget(self.btn_update_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.frame_4 = QtWidgets.QFrame(Settings_tab)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_4.setStyleSheet("background: #9ecd16;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_forgot_password = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_forgot_password.sizePolicy().hasHeightForWidth())
        self.lbl_forgot_password.setSizePolicy(sizePolicy)
        self.lbl_forgot_password.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_forgot_password.setObjectName("lbl_forgot_password")
        self.horizontalLayout_8.addWidget(self.lbl_forgot_password)
        self.btn_forgot_password = QtWidgets.QPushButton(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forgot_password.sizePolicy().hasHeightForWidth())
        self.btn_forgot_password.setSizePolicy(sizePolicy)
        self.btn_forgot_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_forgot_password.setText("")
        self.btn_forgot_password.setObjectName("btn_forgot_password")
        self.horizontalLayout_8.addWidget(self.btn_forgot_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.frame_15 = QtWidgets.QFrame(Settings_tab)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_15.setStyleSheet("background: #9ecd16;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_2.addWidget(self.frame_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.lbl_timer = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_timer.sizePolicy().hasHeightForWidth())
        self.lbl_timer.setSizePolicy(sizePolicy)
        self.lbl_timer.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_timer.setObjectName("lbl_timer")
        self.horizontalLayout_17.addWidget(self.lbl_timer)
        self.btn_timer = QtWidgets.QPushButton(Settings_tab)
        self.btn_timer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_timer.setText("")
        self.btn_timer.setObjectName("btn_timer")
        self.horizontalLayout_17.addWidget(self.btn_timer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_17)
        self.frame_3 = QtWidgets.QFrame(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_3.setStyleSheet("background: #9ecd16;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lbl_generate_password = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_generate_password.sizePolicy().hasHeightForWidth())
        self.lbl_generate_password.setSizePolicy(sizePolicy)
        self.lbl_generate_password.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_generate_password.setObjectName("lbl_generate_password")
        self.horizontalLayout_12.addWidget(self.lbl_generate_password)
        self.btn_generate_password = QtWidgets.QPushButton(Settings_tab)
        self.btn_generate_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_generate_password.setText("")
        self.btn_generate_password.setObjectName("btn_generate_password")
        self.horizontalLayout_12.addWidget(self.btn_generate_password)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.frame_5 = QtWidgets.QFrame(Settings_tab)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_5.setStyleSheet("background: #9edc16;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_browser_web_import = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_browser_web_import.sizePolicy().hasHeightForWidth())
        self.lbl_browser_web_import.setSizePolicy(sizePolicy)
        self.lbl_browser_web_import.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_browser_web_import.setObjectName("lbl_browser_web_import")
        self.horizontalLayout.addWidget(self.lbl_browser_web_import)
        self.btn_browser_web_import = QtWidgets.QPushButton(Settings_tab)
        self.btn_browser_web_import.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_browser_web_import.setText("")
        self.btn_browser_web_import.setObjectName("btn_browser_web_import")
        self.horizontalLayout.addWidget(self.btn_browser_web_import)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.frame_12 = QtWidgets.QFrame(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_12.setStyleSheet("background: #9ecd16;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_2.addWidget(self.frame_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lbl_setup = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_setup.sizePolicy().hasHeightForWidth())
        self.lbl_setup.setSizePolicy(sizePolicy)
        self.lbl_setup.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_setup.setObjectName("lbl_setup")
        self.horizontalLayout_15.addWidget(self.lbl_setup)
        self.btn_setup = QtWidgets.QPushButton(Settings_tab)
        self.btn_setup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_setup.setText("")
        self.btn_setup.setObjectName("btn_setup")
        self.horizontalLayout_15.addWidget(self.btn_setup)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.frame_13 = QtWidgets.QFrame(Settings_tab)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 1))
        self.frame_13.setStyleSheet("background: #9ecd16;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_2.addWidget(self.frame_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lbl_groups = QtWidgets.QLabel(Settings_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_groups.sizePolicy().hasHeightForWidth())
        self.lbl_groups.setSizePolicy(sizePolicy)
        self.lbl_groups.setMinimumSize(QtCore.QSize(0, 45))
        self.lbl_groups.setObjectName("lbl_groups")
        self.horizontalLayout_14.addWidget(self.lbl_groups)
        self.btn_groups = QtWidgets.QPushButton(Settings_tab)
        self.btn_groups.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_groups.setText("")
        self.btn_groups.setObjectName("btn_groups")
        self.horizontalLayout_14.addWidget(self.btn_groups)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(Settings_tab)
        QtCore.QMetaObject.connectSlotsByName(Settings_tab)

    def retranslateUi(self, Settings_tab):
        _translate = QtCore.QCoreApplication.translate
        Settings_tab.setWindowTitle(_translate("Settings_tab", "Form"))
        self.lbl_google_integration.setText(_translate("Settings_tab", "Integrate your Google account"))
        self.btn_google.setText(_translate("Settings_tab", "Google Button"))
        self.lbl_2fa.setText(_translate("Settings_tab", "Two Factor Authentication"))
        self.lbl_night_mode.setText(_translate("Settings_tab", "Night Mode"))
        self.lbl_calendar.setText(_translate("Settings_tab", "Integrate With Google Calendar"))
        self.lbl_auto_save.setText(_translate("Settings_tab", "Automatically Save To Remote Storage"))
        self.lbl_save_remote.setText(_translate("Settings_tab", "Save To Remote Storage"))
        self.lbl_restore_remote.setText(_translate("Settings_tab", "Restore From Remote Storage"))
        self.lbl_save_local.setText(_translate("Settings_tab", "Save To Local Storage"))
        self.lbl_restore_local.setText(_translate("Settings_tab", "Restore From Local Storage"))
        self.lbl_login.setText(_translate("Settings_tab", "Login"))
        self.lbl_update_password.setText(_translate("Settings_tab", "Update Password"))
        self.lbl_forgot_password.setText(_translate("Settings_tab", "Reset Security"))
        self.lbl_timer.setText(_translate("Settings_tab", "Set Login Timer"))
        self.lbl_generate_password.setText(_translate("Settings_tab", "Generate Password"))
        self.lbl_browser_web_import.setText(_translate("Settings_tab", "Import Passwords From Browser"))
        self.lbl_setup.setText(_translate("Settings_tab", "Setup Wizard"))
        self.lbl_groups.setText(_translate("Settings_tab", "Edit Groups"))