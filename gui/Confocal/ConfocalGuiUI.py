# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfocalGuiUI.ui'
#
# Created: Thu May 21 13:16:30 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(974, 735)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_8 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.xy_ViewWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xy_ViewWidget.sizePolicy().hasHeightForWidth())
        self.xy_ViewWidget.setSizePolicy(sizePolicy)
        self.xy_ViewWidget.setObjectName(_fromUtf8("xy_ViewWidget"))
        self.horizontalLayout_4.addWidget(self.xy_ViewWidget)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.xy_cb_ViewWidget = PlotWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xy_cb_ViewWidget.sizePolicy().hasHeightForWidth())
        self.xy_cb_ViewWidget.setSizePolicy(sizePolicy)
        self.xy_cb_ViewWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.xy_cb_ViewWidget.setObjectName(_fromUtf8("xy_cb_ViewWidget"))
        self.gridLayout.addWidget(self.xy_cb_ViewWidget, 1, 0, 1, 1)
        self.xy_cb_max_InputWidget = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xy_cb_max_InputWidget.sizePolicy().hasHeightForWidth())
        self.xy_cb_max_InputWidget.setSizePolicy(sizePolicy)
        self.xy_cb_max_InputWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.xy_cb_max_InputWidget.setObjectName(_fromUtf8("xy_cb_max_InputWidget"))
        self.gridLayout.addWidget(self.xy_cb_max_InputWidget, 0, 0, 1, 1)
        self.xy_cb_auto_CheckBox = QtGui.QCheckBox(self.centralwidget)
        self.xy_cb_auto_CheckBox.setChecked(True)
        self.xy_cb_auto_CheckBox.setObjectName(_fromUtf8("xy_cb_auto_CheckBox"))
        self.gridLayout.addWidget(self.xy_cb_auto_CheckBox, 3, 0, 1, 1)
        self.xy_cb_min_InputWidget = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xy_cb_min_InputWidget.sizePolicy().hasHeightForWidth())
        self.xy_cb_min_InputWidget.setSizePolicy(sizePolicy)
        self.xy_cb_min_InputWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.xy_cb_min_InputWidget.setObjectName(_fromUtf8("xy_cb_min_InputWidget"))
        self.gridLayout.addWidget(self.xy_cb_min_InputWidget, 2, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.xz_ViewWidget = PlotWidget(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xz_ViewWidget.sizePolicy().hasHeightForWidth())
        self.xz_ViewWidget.setSizePolicy(sizePolicy)
        self.xz_ViewWidget.setObjectName(_fromUtf8("xz_ViewWidget"))
        self.gridLayout_4.addWidget(self.xz_ViewWidget, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.xz_cb_ViewWidget = PlotWidget(self.tab_5)
        self.xz_cb_ViewWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.xz_cb_ViewWidget.setObjectName(_fromUtf8("xz_cb_ViewWidget"))
        self.gridLayout_2.addWidget(self.xz_cb_ViewWidget, 1, 0, 1, 1)
        self.xz_cb_max_InputWidget = QtGui.QLineEdit(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xz_cb_max_InputWidget.sizePolicy().hasHeightForWidth())
        self.xz_cb_max_InputWidget.setSizePolicy(sizePolicy)
        self.xz_cb_max_InputWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.xz_cb_max_InputWidget.setObjectName(_fromUtf8("xz_cb_max_InputWidget"))
        self.gridLayout_2.addWidget(self.xz_cb_max_InputWidget, 0, 0, 1, 1)
        self.xz_cb_min_InputWidget = QtGui.QLineEdit(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xz_cb_min_InputWidget.sizePolicy().hasHeightForWidth())
        self.xz_cb_min_InputWidget.setSizePolicy(sizePolicy)
        self.xz_cb_min_InputWidget.setMaximumSize(QtCore.QSize(70, 16777215))
        self.xz_cb_min_InputWidget.setObjectName(_fromUtf8("xz_cb_min_InputWidget"))
        self.gridLayout_2.addWidget(self.xz_cb_min_InputWidget, 2, 0, 1, 1)
        self.xz_cb_auto_CheckBox = QtGui.QCheckBox(self.tab_5)
        self.xz_cb_auto_CheckBox.setChecked(True)
        self.xz_cb_auto_CheckBox.setObjectName(_fromUtf8("xz_cb_auto_CheckBox"))
        self.gridLayout_2.addWidget(self.xz_cb_auto_CheckBox, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_6 = QtGui.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_6.addWidget(self.label_8, 4, 2, 1, 1)
        self.y_refocus_position_ViewWidget = QtGui.QLineEdit(self.tab_6)
        self.y_refocus_position_ViewWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.y_refocus_position_ViewWidget.setReadOnly(True)
        self.y_refocus_position_ViewWidget.setObjectName(_fromUtf8("y_refocus_position_ViewWidget"))
        self.gridLayout_6.addWidget(self.y_refocus_position_ViewWidget, 4, 3, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_6.addWidget(self.label_7, 4, 4, 1, 1)
        self.x_refocus_position_ViewWidget = QtGui.QLineEdit(self.tab_6)
        self.x_refocus_position_ViewWidget.setEnabled(True)
        self.x_refocus_position_ViewWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.x_refocus_position_ViewWidget.setReadOnly(True)
        self.x_refocus_position_ViewWidget.setObjectName(_fromUtf8("x_refocus_position_ViewWidget"))
        self.gridLayout_6.addWidget(self.x_refocus_position_ViewWidget, 4, 1, 1, 1)
        self.z_refocus_position_ViewWidget = QtGui.QLineEdit(self.tab_6)
        self.z_refocus_position_ViewWidget.setAlignment(QtCore.Qt.AlignCenter)
        self.z_refocus_position_ViewWidget.setReadOnly(True)
        self.z_refocus_position_ViewWidget.setObjectName(_fromUtf8("z_refocus_position_ViewWidget"))
        self.gridLayout_6.addWidget(self.z_refocus_position_ViewWidget, 4, 5, 1, 1)
        self.xz_refocus_ViewWidget = PlotWidget(self.tab_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.xz_refocus_ViewWidget.sizePolicy().hasHeightForWidth())
        self.xz_refocus_ViewWidget.setSizePolicy(sizePolicy)
        self.xz_refocus_ViewWidget.setObjectName(_fromUtf8("xz_refocus_ViewWidget"))
        self.gridLayout_6.addWidget(self.xz_refocus_ViewWidget, 3, 0, 1, 6)
        self.xy_refocus_ViewWidget = PlotWidget(self.tab_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.xy_refocus_ViewWidget.sizePolicy().hasHeightForWidth())
        self.xy_refocus_ViewWidget.setSizePolicy(sizePolicy)
        self.xy_refocus_ViewWidget.setObjectName(_fromUtf8("xy_refocus_ViewWidget"))
        self.gridLayout_6.addWidget(self.xy_refocus_ViewWidget, 2, 0, 1, 6)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(51, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.z_res_InputWidget = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_res_InputWidget.sizePolicy().hasHeightForWidth())
        self.z_res_InputWidget.setSizePolicy(sizePolicy)
        self.z_res_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.z_res_InputWidget.setObjectName(_fromUtf8("z_res_InputWidget"))
        self.horizontalLayout_2.addWidget(self.z_res_InputWidget)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_2.addWidget(self.line_4)
        self.z_min_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.z_min_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.z_min_InputWidget.setObjectName(_fromUtf8("z_min_InputWidget"))
        self.horizontalLayout_2.addWidget(self.z_min_InputWidget)
        self.z_max_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.z_max_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.z_max_InputWidget.setObjectName(_fromUtf8("z_max_InputWidget"))
        self.horizontalLayout_2.addWidget(self.z_max_InputWidget)
        self.z_SliderWidget = QtGui.QSlider(self.centralwidget)
        self.z_SliderWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.z_SliderWidget.setOrientation(QtCore.Qt.Horizontal)
        self.z_SliderWidget.setObjectName(_fromUtf8("z_SliderWidget"))
        self.horizontalLayout_2.addWidget(self.z_SliderWidget)
        self.z_current_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.z_current_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.z_current_InputWidget.setObjectName(_fromUtf8("z_current_InputWidget"))
        self.horizontalLayout_2.addWidget(self.z_current_InputWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.ready_StateWidget = QtGui.QRadioButton(self.centralwidget)
        self.ready_StateWidget.setObjectName(_fromUtf8("ready_StateWidget"))
        self.horizontalLayout_6.addWidget(self.ready_StateWidget)
        self.xy_scan_StateWidget = QtGui.QRadioButton(self.centralwidget)
        self.xy_scan_StateWidget.setObjectName(_fromUtf8("xy_scan_StateWidget"))
        self.horizontalLayout_6.addWidget(self.xy_scan_StateWidget)
        self.xz_scan_StateWidget = QtGui.QRadioButton(self.centralwidget)
        self.xz_scan_StateWidget.setObjectName(_fromUtf8("xz_scan_StateWidget"))
        self.horizontalLayout_6.addWidget(self.xz_scan_StateWidget)
        self.refocus_StateWidget = QtGui.QRadioButton(self.centralwidget)
        self.refocus_StateWidget.setObjectName(_fromUtf8("refocus_StateWidget"))
        self.horizontalLayout_6.addWidget(self.refocus_StateWidget)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem2 = QtGui.QSpacerItem(56, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(125, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_7.addWidget(self.line)
        spacerItem3 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem5 = QtGui.QSpacerItem(56, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_3.addWidget(self.line_3)
        self.y_min_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.y_min_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.y_min_InputWidget.setObjectName(_fromUtf8("y_min_InputWidget"))
        self.horizontalLayout_3.addWidget(self.y_min_InputWidget)
        self.y_max_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.y_max_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.y_max_InputWidget.setObjectName(_fromUtf8("y_max_InputWidget"))
        self.horizontalLayout_3.addWidget(self.y_max_InputWidget)
        self.y_SliderWidget = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_SliderWidget.sizePolicy().hasHeightForWidth())
        self.y_SliderWidget.setSizePolicy(sizePolicy)
        self.y_SliderWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.y_SliderWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.y_SliderWidget.setBaseSize(QtCore.QSize(0, 0))
        self.y_SliderWidget.setOrientation(QtCore.Qt.Horizontal)
        self.y_SliderWidget.setObjectName(_fromUtf8("y_SliderWidget"))
        self.horizontalLayout_3.addWidget(self.y_SliderWidget)
        self.y_current_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.y_current_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.y_current_InputWidget.setObjectName(_fromUtf8("y_current_InputWidget"))
        self.horizontalLayout_3.addWidget(self.y_current_InputWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.xy_res_InputWidget = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xy_res_InputWidget.sizePolicy().hasHeightForWidth())
        self.xy_res_InputWidget.setSizePolicy(sizePolicy)
        self.xy_res_InputWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.xy_res_InputWidget.setMaximumSize(QtCore.QSize(50, 1111))
        self.xy_res_InputWidget.setObjectName(_fromUtf8("xy_res_InputWidget"))
        self.horizontalLayout.addWidget(self.xy_res_InputWidget)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout.addWidget(self.line_2)
        self.x_min_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.x_min_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.x_min_InputWidget.setObjectName(_fromUtf8("x_min_InputWidget"))
        self.horizontalLayout.addWidget(self.x_min_InputWidget)
        self.x_max_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.x_max_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.x_max_InputWidget.setObjectName(_fromUtf8("x_max_InputWidget"))
        self.horizontalLayout.addWidget(self.x_max_InputWidget)
        self.x_SliderWidget = QtGui.QSlider(self.centralwidget)
        self.x_SliderWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.x_SliderWidget.setSingleStep(1)
        self.x_SliderWidget.setOrientation(QtCore.Qt.Horizontal)
        self.x_SliderWidget.setObjectName(_fromUtf8("x_SliderWidget"))
        self.horizontalLayout.addWidget(self.x_SliderWidget)
        self.x_current_InputWidget = QtGui.QLineEdit(self.centralwidget)
        self.x_current_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.x_current_InputWidget.setObjectName(_fromUtf8("x_current_InputWidget"))
        self.horizontalLayout.addWidget(self.x_current_InputWidget)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menu_Options = QtGui.QMenu(self.menubar)
        self.menu_Options.setObjectName(_fromUtf8("menu_Options"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_XY_Scan = QtGui.QAction(MainWindow)
        self.actionSave_XY_Scan.setObjectName(_fromUtf8("actionSave_XY_Scan"))
        self.actionSave_configuration = QtGui.QAction(MainWindow)
        self.actionSave_configuration.setObjectName(_fromUtf8("actionSave_configuration"))
        self.action_Settings = QtGui.QAction(MainWindow)
        self.action_Settings.setObjectName(_fromUtf8("action_Settings"))
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName(_fromUtf8("action_Exit"))
        self.actionSave_XZ_Scan = QtGui.QAction(MainWindow)
        self.actionSave_XZ_Scan.setObjectName(_fromUtf8("actionSave_XZ_Scan"))
        self.action_optimiser_settings = QtGui.QAction(MainWindow)
        self.action_optimiser_settings.setObjectName(_fromUtf8("action_optimiser_settings"))
        self.menuFile.addAction(self.actionSave_XY_Scan)
        self.menuFile.addAction(self.actionSave_XZ_Scan)
        self.menuFile.addAction(self.actionSave_configuration)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Exit)
        self.menu_Options.addAction(self.action_Settings)
        self.menu_Options.addAction(self.action_optimiser_settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Options.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_Exit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.xy_ViewWidget, self.xz_ViewWidget)
        MainWindow.setTabOrder(self.xz_ViewWidget, self.xy_res_InputWidget)
        MainWindow.setTabOrder(self.xy_res_InputWidget, self.z_res_InputWidget)
        MainWindow.setTabOrder(self.z_res_InputWidget, self.x_min_InputWidget)
        MainWindow.setTabOrder(self.x_min_InputWidget, self.x_max_InputWidget)
        MainWindow.setTabOrder(self.x_max_InputWidget, self.y_min_InputWidget)
        MainWindow.setTabOrder(self.y_min_InputWidget, self.y_max_InputWidget)
        MainWindow.setTabOrder(self.y_max_InputWidget, self.z_min_InputWidget)
        MainWindow.setTabOrder(self.z_min_InputWidget, self.z_max_InputWidget)
        MainWindow.setTabOrder(self.z_max_InputWidget, self.x_current_InputWidget)
        MainWindow.setTabOrder(self.x_current_InputWidget, self.y_current_InputWidget)
        MainWindow.setTabOrder(self.y_current_InputWidget, self.z_current_InputWidget)
        MainWindow.setTabOrder(self.z_current_InputWidget, self.ready_StateWidget)
        MainWindow.setTabOrder(self.ready_StateWidget, self.xy_scan_StateWidget)
        MainWindow.setTabOrder(self.xy_scan_StateWidget, self.xz_scan_StateWidget)
        MainWindow.setTabOrder(self.xz_scan_StateWidget, self.refocus_StateWidget)
        MainWindow.setTabOrder(self.refocus_StateWidget, self.z_SliderWidget)
        MainWindow.setTabOrder(self.z_SliderWidget, self.y_SliderWidget)
        MainWindow.setTabOrder(self.y_SliderWidget, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.x_SliderWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "qudi: Confocal", None, QtGui.QApplication.UnicodeUTF8))
        self.xy_cb_max_InputWidget.setText(QtGui.QApplication.translate("MainWindow", "100000", None, QtGui.QApplication.UnicodeUTF8))
        self.xy_cb_auto_CheckBox.setText(QtGui.QApplication.translate("MainWindow", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.xy_cb_min_InputWidget.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.xz_cb_max_InputWidget.setText(QtGui.QApplication.translate("MainWindow", "100000", None, QtGui.QApplication.UnicodeUTF8))
        self.xz_cb_min_InputWidget.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.xz_cb_auto_CheckBox.setText(QtGui.QApplication.translate("MainWindow", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Z-Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "X :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Y :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Z :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Optimiser", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Z-Axis :", None, QtGui.QApplication.UnicodeUTF8))
        self.z_res_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z-Resolution</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.z_min_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z_Min</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.z_max_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z_Max</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.z_current_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Z-position</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.ready_StateWidget.setText(QtGui.QApplication.translate("MainWindow", "Ready", None, QtGui.QApplication.UnicodeUTF8))
        self.xy_scan_StateWidget.setText(QtGui.QApplication.translate("MainWindow", "Scan XY", None, QtGui.QApplication.UnicodeUTF8))
        self.xz_scan_StateWidget.setText(QtGui.QApplication.translate("MainWindow", "Scan Z", None, QtGui.QApplication.UnicodeUTF8))
        self.refocus_StateWidget.setText(QtGui.QApplication.translate("MainWindow", "Optimise position", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Scan Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Y-Axis :", None, QtGui.QApplication.UnicodeUTF8))
        self.y_min_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y_Min</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.y_max_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y_Max</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.y_current_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Y-position</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "X-Axis :", None, QtGui.QApplication.UnicodeUTF8))
        self.xy_res_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">XY-Resolution</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.x_min_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X_Min</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.x_max_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X_Max</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.x_current_InputWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">X-position</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Options.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_XY_Scan.setText(QtGui.QApplication.translate("MainWindow", "Save XY Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_configuration.setText(QtGui.QApplication.translate("MainWindow", "Save &configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Settings.setText(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_XZ_Scan.setText(QtGui.QApplication.translate("MainWindow", "Save XZ Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.action_optimiser_settings.setText(QtGui.QApplication.translate("MainWindow", "Optimiser Settings", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
