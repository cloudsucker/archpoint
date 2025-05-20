# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(957, 697)
        Widget.setMinimumSize(QSize(600, 400))
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(10)
        Widget.setFont(font)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_main = QGroupBox(Widget)
        self.groupBox_main.setObjectName(u"groupBox_main")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_pagesAndSettings = QGroupBox(self.groupBox_main)
        self.groupBox_pagesAndSettings.setObjectName(u"groupBox_pagesAndSettings")
        self.groupBox_pagesAndSettings.setMinimumSize(QSize(170, 0))
        self.groupBox_pagesAndSettings.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(9)
        self.groupBox_pagesAndSettings.setFont(font1)
        self.verticalLayout = QVBoxLayout(self.groupBox_pagesAndSettings)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_appLogo = QLabel(self.groupBox_pagesAndSettings)
        self.label_appLogo.setObjectName(u"label_appLogo")
        self.label_appLogo.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamilies([u"Rubik"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_appLogo.setFont(font2)

        self.verticalLayout.addWidget(self.label_appLogo)

        self.groupBox_pages = QGroupBox(self.groupBox_pagesAndSettings)
        self.groupBox_pages.setObjectName(u"groupBox_pages")
        self.groupBox_pages.setFlat(True)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_pages)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_pageCalibration = QPushButton(self.groupBox_pages)
        self.pushButton_pageCalibration.setObjectName(u"pushButton_pageCalibration")
        font3 = QFont()
        font3.setFamilies([u"Rubik"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.pushButton_pageCalibration.setFont(font3)
        self.pushButton_pageCalibration.setCheckable(True)
        self.pushButton_pageCalibration.setChecked(True)
        self.pushButton_pageCalibration.setAutoExclusive(True)
        self.pushButton_pageCalibration.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_pageCalibration)

        self.pushButton_pageProcess = QPushButton(self.groupBox_pages)
        self.pushButton_pageProcess.setObjectName(u"pushButton_pageProcess")
        self.pushButton_pageProcess.setFont(font3)
        self.pushButton_pageProcess.setCheckable(True)
        self.pushButton_pageProcess.setChecked(False)
        self.pushButton_pageProcess.setAutoExclusive(True)
        self.pushButton_pageProcess.setFlat(True)

        self.verticalLayout_3.addWidget(self.pushButton_pageProcess)


        self.verticalLayout.addWidget(self.groupBox_pages)

        self.verticalSpacer_underPages = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_underPages)

        self.groupBox_settingsAndTheme = QGroupBox(self.groupBox_pagesAndSettings)
        self.groupBox_settingsAndTheme.setObjectName(u"groupBox_settingsAndTheme")
        self.groupBox_settingsAndTheme.setMinimumSize(QSize(0, 30))
        self.groupBox_settingsAndTheme.setMaximumSize(QSize(16777215, 50))
        self.groupBox_settingsAndTheme.setFlat(True)
        self.groupBox_settingsAndTheme.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_settingsAndTheme)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.pushButton_settings = QPushButton(self.groupBox_settingsAndTheme)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        font4 = QFont()
        font4.setFamilies([u"Rubik"])
        font4.setPointSize(8)
        self.pushButton_settings.setFont(font4)
        self.pushButton_settings.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_settings)

        self.pushButton_themeToggle = QPushButton(self.groupBox_settingsAndTheme)
        self.pushButton_themeToggle.setObjectName(u"pushButton_themeToggle")
        self.pushButton_themeToggle.setFont(font4)
        self.pushButton_themeToggle.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_themeToggle)


        self.verticalLayout.addWidget(self.groupBox_settingsAndTheme)


        self.horizontalLayout_2.addWidget(self.groupBox_pagesAndSettings)

        self.groupBox_workspace = QGroupBox(self.groupBox_main)
        self.groupBox_workspace.setObjectName(u"groupBox_workspace")
        font5 = QFont()
        font5.setFamilies([u"Rubik"])
        font5.setPointSize(12)
        self.groupBox_workspace.setFont(font5)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_workspace)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.stackedWidget_workSpace = QStackedWidget(self.groupBox_workspace)
        self.stackedWidget_workSpace.setObjectName(u"stackedWidget_workSpace")
        self.stackedWidget_workSpace.setLineWidth(0)
        self.page_calibrationInitialChoice = QWidget()
        self.page_calibrationInitialChoice.setObjectName(u"page_calibrationInitialChoice")
        self.gridLayout_3 = QGridLayout(self.page_calibrationInitialChoice)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_page_calibrationInitialChoiceOptions = QGroupBox(self.page_calibrationInitialChoice)
        self.groupBox_page_calibrationInitialChoiceOptions.setObjectName(u"groupBox_page_calibrationInitialChoiceOptions")
        self.groupBox_page_calibrationInitialChoiceOptions.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.groupBox_page_calibrationInitialChoiceOptions)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_page_calibrationFromFileOptionField = QGroupBox(self.groupBox_page_calibrationInitialChoiceOptions)
        self.groupBox_page_calibrationFromFileOptionField.setObjectName(u"groupBox_page_calibrationFromFileOptionField")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_page_calibrationFromFileOptionField)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_page_calibrationFromFileOptionTitle = QLabel(self.groupBox_page_calibrationFromFileOptionField)
        self.label_page_calibrationFromFileOptionTitle.setObjectName(u"label_page_calibrationFromFileOptionTitle")
        font6 = QFont()
        font6.setFamilies([u"Rubik"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_page_calibrationFromFileOptionTitle.setFont(font6)

        self.verticalLayout_4.addWidget(self.label_page_calibrationFromFileOptionTitle)

        self.label_page_calibrationFromFileOptionIcon = QLabel(self.groupBox_page_calibrationFromFileOptionField)
        self.label_page_calibrationFromFileOptionIcon.setObjectName(u"label_page_calibrationFromFileOptionIcon")
        font7 = QFont()
        font7.setFamilies([u"Rubik"])
        font7.setPointSize(20)
        font7.setBold(False)
        self.label_page_calibrationFromFileOptionIcon.setFont(font7)

        self.verticalLayout_4.addWidget(self.label_page_calibrationFromFileOptionIcon)

        self.pushButton_page_calibrationFromFileOptionButton = QPushButton(self.groupBox_page_calibrationFromFileOptionField)
        self.pushButton_page_calibrationFromFileOptionButton.setObjectName(u"pushButton_page_calibrationFromFileOptionButton")
        self.pushButton_page_calibrationFromFileOptionButton.setFont(font5)

        self.verticalLayout_4.addWidget(self.pushButton_page_calibrationFromFileOptionButton)


        self.gridLayout_2.addWidget(self.groupBox_page_calibrationFromFileOptionField, 0, 0, 1, 1)

        self.groupBox_page_0_calibrationStartOptionField = QGroupBox(self.groupBox_page_calibrationInitialChoiceOptions)
        self.groupBox_page_0_calibrationStartOptionField.setObjectName(u"groupBox_page_0_calibrationStartOptionField")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_page_0_calibrationStartOptionField)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_page_calibrationStartOptionTitle = QLabel(self.groupBox_page_0_calibrationStartOptionField)
        self.label_page_calibrationStartOptionTitle.setObjectName(u"label_page_calibrationStartOptionTitle")
        self.label_page_calibrationStartOptionTitle.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_page_calibrationStartOptionTitle)

        self.label_page_calibrationStartOptionIcon = QLabel(self.groupBox_page_0_calibrationStartOptionField)
        self.label_page_calibrationStartOptionIcon.setObjectName(u"label_page_calibrationStartOptionIcon")
        font8 = QFont()
        font8.setFamilies([u"Rubik"])
        font8.setPointSize(20)
        self.label_page_calibrationStartOptionIcon.setFont(font8)

        self.verticalLayout_5.addWidget(self.label_page_calibrationStartOptionIcon)

        self.pushButton_page_calibrationStartOptionButton = QPushButton(self.groupBox_page_0_calibrationStartOptionField)
        self.pushButton_page_calibrationStartOptionButton.setObjectName(u"pushButton_page_calibrationStartOptionButton")
        self.pushButton_page_calibrationStartOptionButton.setFont(font5)

        self.verticalLayout_5.addWidget(self.pushButton_page_calibrationStartOptionButton)


        self.gridLayout_2.addWidget(self.groupBox_page_0_calibrationStartOptionField, 0, 1, 1, 1)

        self.groupBox_page_calibrationSkipOptionField = QGroupBox(self.groupBox_page_calibrationInitialChoiceOptions)
        self.groupBox_page_calibrationSkipOptionField.setObjectName(u"groupBox_page_calibrationSkipOptionField")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_page_calibrationSkipOptionField)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_page_calibrationSkipOptionTitle = QLabel(self.groupBox_page_calibrationSkipOptionField)
        self.label_page_calibrationSkipOptionTitle.setObjectName(u"label_page_calibrationSkipOptionTitle")
        self.label_page_calibrationSkipOptionTitle.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_page_calibrationSkipOptionTitle)

        self.label_page_calibrationSkipOptionText = QLabel(self.groupBox_page_calibrationSkipOptionField)
        self.label_page_calibrationSkipOptionText.setObjectName(u"label_page_calibrationSkipOptionText")
        self.label_page_calibrationSkipOptionText.setFont(font)
        self.label_page_calibrationSkipOptionText.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_page_calibrationSkipOptionText)

        self.label_page_calibrationSkipOptionIcon = QLabel(self.groupBox_page_calibrationSkipOptionField)
        self.label_page_calibrationSkipOptionIcon.setObjectName(u"label_page_calibrationSkipOptionIcon")
        font9 = QFont()
        font9.setFamilies([u"Rubik"])
        font9.setPointSize(20)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_page_calibrationSkipOptionIcon.setFont(font9)

        self.verticalLayout_6.addWidget(self.label_page_calibrationSkipOptionIcon)

        self.pushButton_page_calibrationSkipOptionButton = QPushButton(self.groupBox_page_calibrationSkipOptionField)
        self.pushButton_page_calibrationSkipOptionButton.setObjectName(u"pushButton_page_calibrationSkipOptionButton")

        self.verticalLayout_6.addWidget(self.pushButton_page_calibrationSkipOptionButton)


        self.gridLayout_2.addWidget(self.groupBox_page_calibrationSkipOptionField, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_page_calibrationInitialChoiceOptions, 1, 0, 1, 1)

        self.verticalSpacer_page_calibrationChoiceOptionsBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_page_calibrationChoiceOptionsBottom, 2, 0, 1, 1)

        self.verticalSpacer_page_calibrationChoiceOptionsTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_page_calibrationChoiceOptionsTop, 0, 0, 1, 1)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationInitialChoice)
        self.page_calibrationSteps_0_MethodSelection = QWidget()
        self.page_calibrationSteps_0_MethodSelection.setObjectName(u"page_calibrationSteps_0_MethodSelection")
        self.verticalLayout_23 = QVBoxLayout(self.page_calibrationSteps_0_MethodSelection)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.groupBox_calibrationSteps_0_MethodSelectionMain = QGroupBox(self.page_calibrationSteps_0_MethodSelection)
        self.groupBox_calibrationSteps_0_MethodSelectionMain.setObjectName(u"groupBox_calibrationSteps_0_MethodSelectionMain")
        self.groupBox_calibrationSteps_0_MethodSelectionMain.setFont(font3)
        self.verticalLayout_24 = QVBoxLayout(self.groupBox_calibrationSteps_0_MethodSelectionMain)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacer_calibrationSteps_0_MethodSelectionTop = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_calibrationSteps_0_MethodSelectionTop)

        self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField = QGroupBox(self.groupBox_calibrationSteps_0_MethodSelectionMain)
        self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField.setObjectName(u"groupBox_calibrationSteps_0_CalibrationMethodsSelectionField")
        self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField.setFlat(True)
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.groupBox_calibrationSteps_0_MethodAutoField = QGroupBox(self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField)
        self.groupBox_calibrationSteps_0_MethodAutoField.setObjectName(u"groupBox_calibrationSteps_0_MethodAutoField")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_calibrationSteps_0_MethodAutoField)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_calibrationSteps_0_MethodAutoTitle = QLabel(self.groupBox_calibrationSteps_0_MethodAutoField)
        self.label_calibrationSteps_0_MethodAutoTitle.setObjectName(u"label_calibrationSteps_0_MethodAutoTitle")
        self.label_calibrationSteps_0_MethodAutoTitle.setFont(font6)

        self.verticalLayout_26.addWidget(self.label_calibrationSteps_0_MethodAutoTitle)

        self.label_calibrationSteps_0_MethodAutoIcon = QLabel(self.groupBox_calibrationSteps_0_MethodAutoField)
        self.label_calibrationSteps_0_MethodAutoIcon.setObjectName(u"label_calibrationSteps_0_MethodAutoIcon")
        self.label_calibrationSteps_0_MethodAutoIcon.setFont(font3)

        self.verticalLayout_26.addWidget(self.label_calibrationSteps_0_MethodAutoIcon)

        self.pushButton_calibrationSteps_0_MethodAutoSelectButton = QPushButton(self.groupBox_calibrationSteps_0_MethodAutoField)
        self.pushButton_calibrationSteps_0_MethodAutoSelectButton.setObjectName(u"pushButton_calibrationSteps_0_MethodAutoSelectButton")
        self.pushButton_calibrationSteps_0_MethodAutoSelectButton.setFont(font3)

        self.verticalLayout_26.addWidget(self.pushButton_calibrationSteps_0_MethodAutoSelectButton)


        self.horizontalLayout_17.addWidget(self.groupBox_calibrationSteps_0_MethodAutoField)

        self.groupBox_calibrationSteps_0_MethodManualField = QGroupBox(self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField)
        self.groupBox_calibrationSteps_0_MethodManualField.setObjectName(u"groupBox_calibrationSteps_0_MethodManualField")
        self.verticalLayout_25 = QVBoxLayout(self.groupBox_calibrationSteps_0_MethodManualField)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_calibrationSteps_0_MethodManualTitle = QLabel(self.groupBox_calibrationSteps_0_MethodManualField)
        self.label_calibrationSteps_0_MethodManualTitle.setObjectName(u"label_calibrationSteps_0_MethodManualTitle")
        self.label_calibrationSteps_0_MethodManualTitle.setFont(font6)

        self.verticalLayout_25.addWidget(self.label_calibrationSteps_0_MethodManualTitle)

        self.label_calibrationSteps_0_MethodManualIcon = QLabel(self.groupBox_calibrationSteps_0_MethodManualField)
        self.label_calibrationSteps_0_MethodManualIcon.setObjectName(u"label_calibrationSteps_0_MethodManualIcon")
        self.label_calibrationSteps_0_MethodManualIcon.setFont(font3)

        self.verticalLayout_25.addWidget(self.label_calibrationSteps_0_MethodManualIcon)

        self.pushButton_calibrationSteps_0_MethodManualSelectButton = QPushButton(self.groupBox_calibrationSteps_0_MethodManualField)
        self.pushButton_calibrationSteps_0_MethodManualSelectButton.setObjectName(u"pushButton_calibrationSteps_0_MethodManualSelectButton")
        self.pushButton_calibrationSteps_0_MethodManualSelectButton.setFont(font3)

        self.verticalLayout_25.addWidget(self.pushButton_calibrationSteps_0_MethodManualSelectButton)


        self.horizontalLayout_17.addWidget(self.groupBox_calibrationSteps_0_MethodManualField)


        self.verticalLayout_24.addWidget(self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField)

        self.verticalSpacer_calibrationSteps_0_MethodSelectionBottom = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_calibrationSteps_0_MethodSelectionBottom)

        self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField = QGroupBox(self.groupBox_calibrationSteps_0_MethodSelectionMain)
        self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField.setObjectName(u"groupBox_calibrationSteps_0_MethodSelectionMainButtonsField")
        self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField.setFlat(True)
        self.horizontalLayout_14 = QHBoxLayout(self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_returnToCalibrationChoice = QPushButton(self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField)
        self.pushButton_returnToCalibrationChoice.setObjectName(u"pushButton_returnToCalibrationChoice")

        self.horizontalLayout_14.addWidget(self.pushButton_returnToCalibrationChoice)

        self.horizontalSpacer_calibrationSteps_0_MethodSelectionMainButtonsSpacer = QSpacerItem(602, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_calibrationSteps_0_MethodSelectionMainButtonsSpacer)


        self.verticalLayout_24.addWidget(self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField)


        self.verticalLayout_23.addWidget(self.groupBox_calibrationSteps_0_MethodSelectionMain)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_0_MethodSelection)
        self.page_processingChoiceProject = QWidget()
        self.page_processingChoiceProject.setObjectName(u"page_processingChoiceProject")
        self.verticalLayout_19 = QVBoxLayout(self.page_processingChoiceProject)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_processingProjectOptionsTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_processingProjectOptionsTop)

        self.groupBox_processingProjectOptions = QGroupBox(self.page_processingChoiceProject)
        self.groupBox_processingProjectOptions.setObjectName(u"groupBox_processingProjectOptions")
        self.groupBox_processingProjectOptions.setFlat(True)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_processingProjectOptions)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_newProject = QGroupBox(self.groupBox_processingProjectOptions)
        self.groupBox_newProject.setObjectName(u"groupBox_newProject")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_newProject)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_newProjectTitle = QLabel(self.groupBox_newProject)
        self.label_newProjectTitle.setObjectName(u"label_newProjectTitle")
        self.label_newProjectTitle.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_newProjectTitle)

        self.label_newProjectIcon = QLabel(self.groupBox_newProject)
        self.label_newProjectIcon.setObjectName(u"label_newProjectIcon")
        self.label_newProjectIcon.setFont(font8)

        self.verticalLayout_8.addWidget(self.label_newProjectIcon)

        self.pushButton_newProject = QPushButton(self.groupBox_newProject)
        self.pushButton_newProject.setObjectName(u"pushButton_newProject")
        self.pushButton_newProject.setFont(font5)

        self.verticalLayout_8.addWidget(self.pushButton_newProject)


        self.horizontalLayout_6.addWidget(self.groupBox_newProject)

        self.groupBox_chooseProject = QGroupBox(self.groupBox_processingProjectOptions)
        self.groupBox_chooseProject.setObjectName(u"groupBox_chooseProject")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_chooseProject)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_chooseProjectTitle = QLabel(self.groupBox_chooseProject)
        self.label_chooseProjectTitle.setObjectName(u"label_chooseProjectTitle")
        self.label_chooseProjectTitle.setFont(font6)

        self.verticalLayout_7.addWidget(self.label_chooseProjectTitle)

        self.label_chooseProjectIcon = QLabel(self.groupBox_chooseProject)
        self.label_chooseProjectIcon.setObjectName(u"label_chooseProjectIcon")
        self.label_chooseProjectIcon.setFont(font8)

        self.verticalLayout_7.addWidget(self.label_chooseProjectIcon)

        self.pushButton_chooseProject = QPushButton(self.groupBox_chooseProject)
        self.pushButton_chooseProject.setObjectName(u"pushButton_chooseProject")
        self.pushButton_chooseProject.setFont(font5)

        self.verticalLayout_7.addWidget(self.pushButton_chooseProject)


        self.horizontalLayout_6.addWidget(self.groupBox_chooseProject)


        self.verticalLayout_19.addWidget(self.groupBox_processingProjectOptions)

        self.verticalSpacer_processingProjectOptionsBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_processingProjectOptionsBottom)

        self.stackedWidget_workSpace.addWidget(self.page_processingChoiceProject)
        self.page_processingNewProjectCreating = QWidget()
        self.page_processingNewProjectCreating.setObjectName(u"page_processingNewProjectCreating")
        self.verticalLayout_20 = QVBoxLayout(self.page_processingNewProjectCreating)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.groupBox_newProjectCreatingMain = QGroupBox(self.page_processingNewProjectCreating)
        self.groupBox_newProjectCreatingMain.setObjectName(u"groupBox_newProjectCreatingMain")
        self.groupBox_newProjectCreatingMain.setFont(font6)
        self.groupBox_newProjectCreatingMain.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_newProjectCreatingMain)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_newProjectCreatingNameFieldTitle = QLabel(self.groupBox_newProjectCreatingMain)
        self.label_newProjectCreatingNameFieldTitle.setObjectName(u"label_newProjectCreatingNameFieldTitle")
        self.label_newProjectCreatingNameFieldTitle.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_newProjectCreatingNameFieldTitle)

        self.lineEdit_newProjectCreatingNameField = QLineEdit(self.groupBox_newProjectCreatingMain)
        self.lineEdit_newProjectCreatingNameField.setObjectName(u"lineEdit_newProjectCreatingNameField")
        font10 = QFont()
        font10.setFamilies([u"Rubik"])
        font10.setPointSize(9)
        font10.setBold(False)
        self.lineEdit_newProjectCreatingNameField.setFont(font10)
        self.lineEdit_newProjectCreatingNameField.setMaxLength(40)

        self.verticalLayout_2.addWidget(self.lineEdit_newProjectCreatingNameField)

        self.label_newProjectCreatingPathFieldTitle = QLabel(self.groupBox_newProjectCreatingMain)
        self.label_newProjectCreatingPathFieldTitle.setObjectName(u"label_newProjectCreatingPathFieldTitle")
        self.label_newProjectCreatingPathFieldTitle.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_newProjectCreatingPathFieldTitle)

        self.groupBox_newProjectCreatingPath = QGroupBox(self.groupBox_newProjectCreatingMain)
        self.groupBox_newProjectCreatingPath.setObjectName(u"groupBox_newProjectCreatingPath")
        self.groupBox_newProjectCreatingPath.setFlat(True)
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_newProjectCreatingPath)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_newProjectCreatingPathField = QLineEdit(self.groupBox_newProjectCreatingPath)
        self.lineEdit_newProjectCreatingPathField.setObjectName(u"lineEdit_newProjectCreatingPathField")
        self.lineEdit_newProjectCreatingPathField.setFont(font10)

        self.horizontalLayout_8.addWidget(self.lineEdit_newProjectCreatingPathField)

        self.pushButton_newProjectCreatingPathChoose = QPushButton(self.groupBox_newProjectCreatingPath)
        self.pushButton_newProjectCreatingPathChoose.setObjectName(u"pushButton_newProjectCreatingPathChoose")
        font11 = QFont()
        font11.setFamilies([u"Rubik"])
        font11.setPointSize(8)
        font11.setBold(False)
        self.pushButton_newProjectCreatingPathChoose.setFont(font11)

        self.horizontalLayout_8.addWidget(self.pushButton_newProjectCreatingPathChoose)


        self.verticalLayout_2.addWidget(self.groupBox_newProjectCreatingPath)

        self.verticalSpacer_newProjectCreatingUnderParameters = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_newProjectCreatingUnderParameters)

        self.groupBox_newProjectCreatingSubmitField = QGroupBox(self.groupBox_newProjectCreatingMain)
        self.groupBox_newProjectCreatingSubmitField.setObjectName(u"groupBox_newProjectCreatingSubmitField")
        self.groupBox_newProjectCreatingSubmitField.setFlat(True)
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_newProjectCreatingSubmitField)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_newProjectCreatingCancel = QPushButton(self.groupBox_newProjectCreatingSubmitField)
        self.pushButton_newProjectCreatingCancel.setObjectName(u"pushButton_newProjectCreatingCancel")
        self.pushButton_newProjectCreatingCancel.setFont(font3)

        self.horizontalLayout_9.addWidget(self.pushButton_newProjectCreatingCancel)

        self.horizontalSpacer_newProjectCreating_createButtonLeft = QSpacerItem(602, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_newProjectCreating_createButtonLeft)

        self.pushButton_newProjectCreatingSubmit = QPushButton(self.groupBox_newProjectCreatingSubmitField)
        self.pushButton_newProjectCreatingSubmit.setObjectName(u"pushButton_newProjectCreatingSubmit")
        self.pushButton_newProjectCreatingSubmit.setFont(font3)

        self.horizontalLayout_9.addWidget(self.pushButton_newProjectCreatingSubmit)


        self.verticalLayout_2.addWidget(self.groupBox_newProjectCreatingSubmitField)


        self.verticalLayout_20.addWidget(self.groupBox_newProjectCreatingMain)

        self.stackedWidget_workSpace.addWidget(self.page_processingNewProjectCreating)
        self.page_processingProcess = QWidget()
        self.page_processingProcess.setObjectName(u"page_processingProcess")
        self.verticalLayout_21 = QVBoxLayout(self.page_processingProcess)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_processingProcessMain = QGroupBox(self.page_processingProcess)
        self.groupBox_processingProcessMain.setObjectName(u"groupBox_processingProcessMain")
        self.groupBox_processingProcessMain.setFont(font6)
        self.groupBox_processingProcessMain.setFlat(True)
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_processingProcessMain)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.groupBox_processPathSetter_Field = QGroupBox(self.groupBox_processingProcessMain)
        self.groupBox_processPathSetter_Field.setObjectName(u"groupBox_processPathSetter_Field")
        self.groupBox_processPathSetter_Field.setFont(font3)
        self.groupBox_processPathSetter_Field.setFlat(True)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_processPathSetter_Field)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.lineEdit_imagesDirectoryField = QLineEdit(self.groupBox_processPathSetter_Field)
        self.lineEdit_imagesDirectoryField.setObjectName(u"lineEdit_imagesDirectoryField")
        self.lineEdit_imagesDirectoryField.setFont(font10)

        self.horizontalLayout_11.addWidget(self.lineEdit_imagesDirectoryField)

        self.pushButton_imagesDirectoryChoose = QPushButton(self.groupBox_processPathSetter_Field)
        self.pushButton_imagesDirectoryChoose.setObjectName(u"pushButton_imagesDirectoryChoose")
        self.pushButton_imagesDirectoryChoose.setFont(font11)

        self.horizontalLayout_11.addWidget(self.pushButton_imagesDirectoryChoose)


        self.verticalLayout_22.addWidget(self.groupBox_processPathSetter_Field)

        self.groupBox_secondCameraProcessingField = QGroupBox(self.groupBox_processingProcessMain)
        self.groupBox_secondCameraProcessingField.setObjectName(u"groupBox_secondCameraProcessingField")
        self.groupBox_secondCameraProcessingField.setFont(font3)
        self.groupBox_secondCameraProcessingField.setFlat(True)
        self.groupBox_secondCameraProcessingField.setCheckable(True)
        self.groupBox_secondCameraProcessingField.setChecked(False)
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_secondCameraProcessingField)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lineEdit_secondCameraProcessingImagesDirectory = QLineEdit(self.groupBox_secondCameraProcessingField)
        self.lineEdit_secondCameraProcessingImagesDirectory.setObjectName(u"lineEdit_secondCameraProcessingImagesDirectory")
        self.lineEdit_secondCameraProcessingImagesDirectory.setFont(font10)

        self.horizontalLayout_16.addWidget(self.lineEdit_secondCameraProcessingImagesDirectory)

        self.pushButton_setSecondCameraProcessingImagesDirectory = QPushButton(self.groupBox_secondCameraProcessingField)
        self.pushButton_setSecondCameraProcessingImagesDirectory.setObjectName(u"pushButton_setSecondCameraProcessingImagesDirectory")
        self.pushButton_setSecondCameraProcessingImagesDirectory.setFont(font10)

        self.horizontalLayout_16.addWidget(self.pushButton_setSecondCameraProcessingImagesDirectory)


        self.verticalLayout_22.addWidget(self.groupBox_secondCameraProcessingField)

        self.checkBox_preprocessingImages = QCheckBox(self.groupBox_processingProcessMain)
        self.checkBox_preprocessingImages.setObjectName(u"checkBox_preprocessingImages")
        font12 = QFont()
        font12.setFamilies([u"Rubik"])
        font12.setPointSize(10)
        font12.setBold(False)
        self.checkBox_preprocessingImages.setFont(font12)

        self.verticalLayout_22.addWidget(self.checkBox_preprocessingImages)

        self.pushButton_processingStart = QPushButton(self.groupBox_processingProcessMain)
        self.pushButton_processingStart.setObjectName(u"pushButton_processingStart")
        self.pushButton_processingStart.setFont(font3)

        self.verticalLayout_22.addWidget(self.pushButton_processingStart)

        self.graphicsView_dotsVisualization = QGraphicsView(self.groupBox_processingProcessMain)
        self.graphicsView_dotsVisualization.setObjectName(u"graphicsView_dotsVisualization")

        self.verticalLayout_22.addWidget(self.graphicsView_dotsVisualization)

        self.progressBar_processingProgressBar = QProgressBar(self.groupBox_processingProcessMain)
        self.progressBar_processingProgressBar.setObjectName(u"progressBar_processingProgressBar")
        self.progressBar_processingProgressBar.setFont(font12)
        self.progressBar_processingProgressBar.setValue(24)

        self.verticalLayout_22.addWidget(self.progressBar_processingProgressBar)

        self.textBrowser_processingLogs = QTextBrowser(self.groupBox_processingProcessMain)
        self.textBrowser_processingLogs.setObjectName(u"textBrowser_processingLogs")
        self.textBrowser_processingLogs.setMaximumSize(QSize(16777215, 120))
        self.textBrowser_processingLogs.setFont(font3)

        self.verticalLayout_22.addWidget(self.textBrowser_processingLogs)

        self.groupBox_exportOptions = QGroupBox(self.groupBox_processingProcessMain)
        self.groupBox_exportOptions.setObjectName(u"groupBox_exportOptions")
        self.groupBox_exportOptions.setFlat(True)
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_exportOptions)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportAsDotsCloud = QPushButton(self.groupBox_exportOptions)
        self.pushButton_exportAsDotsCloud.setObjectName(u"pushButton_exportAsDotsCloud")
        self.pushButton_exportAsDotsCloud.setFont(font3)

        self.horizontalLayout_10.addWidget(self.pushButton_exportAsDotsCloud)

        self.horizontalSpacer_exportOptions_buttonsBetween = QSpacerItem(374, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_exportOptions_buttonsBetween)

        self.pushButton_exportAsObjectFile = QPushButton(self.groupBox_exportOptions)
        self.pushButton_exportAsObjectFile.setObjectName(u"pushButton_exportAsObjectFile")
        self.pushButton_exportAsObjectFile.setFont(font3)

        self.horizontalLayout_10.addWidget(self.pushButton_exportAsObjectFile)


        self.verticalLayout_22.addWidget(self.groupBox_exportOptions)


        self.verticalLayout_21.addWidget(self.groupBox_processingProcessMain)

        self.stackedWidget_workSpace.addWidget(self.page_processingProcess)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_15 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.groupBox_settingsMain = QGroupBox(self.page_settings)
        self.groupBox_settingsMain.setObjectName(u"groupBox_settingsMain")
        self.groupBox_settingsMain.setFont(font6)
        self.groupBox_settingsMain.setFlat(True)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_settingsMain)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_settingsTempText = QLabel(self.groupBox_settingsMain)
        self.label_settingsTempText.setObjectName(u"label_settingsTempText")
        self.label_settingsTempText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_settingsTempText)


        self.horizontalLayout_15.addWidget(self.groupBox_settingsMain)

        self.stackedWidget_workSpace.addWidget(self.page_settings)
        self.page_calibrationSteps_1_3_PreparingChessboardTips = QWidget()
        self.page_calibrationSteps_1_3_PreparingChessboardTips.setObjectName(u"page_calibrationSteps_1_3_PreparingChessboardTips")
        self.verticalLayout_13 = QVBoxLayout(self.page_calibrationSteps_1_3_PreparingChessboardTips)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain = QGroupBox(self.page_calibrationSteps_1_3_PreparingChessboardTips)
        self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain.setObjectName(u"groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain")
        self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain.setFont(font6)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_calibrationPreparingStep1 = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain)
        self.groupBox_calibrationPreparingStep1.setObjectName(u"groupBox_calibrationPreparingStep1")
        self.groupBox_calibrationPreparingStep1.setFont(font3)
        self.groupBox_calibrationPreparingStep1.setFlat(True)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_calibrationPreparingStep1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_calibrationPreparingStep1_info = QLabel(self.groupBox_calibrationPreparingStep1)
        self.label_calibrationPreparingStep1_info.setObjectName(u"label_calibrationPreparingStep1_info")
        self.label_calibrationPreparingStep1_info.setFont(font10)
        self.label_calibrationPreparingStep1_info.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_calibrationPreparingStep1_info)

        self.verticalSpacer_calibrationPreparingStep_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_calibrationPreparingStep_1)


        self.verticalLayout_9.addWidget(self.groupBox_calibrationPreparingStep1)

        self.groupBox_calibrationPreparingStep2 = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain)
        self.groupBox_calibrationPreparingStep2.setObjectName(u"groupBox_calibrationPreparingStep2")
        self.groupBox_calibrationPreparingStep2.setFont(font3)
        self.groupBox_calibrationPreparingStep2.setFlat(True)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_calibrationPreparingStep2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_calibrationPreparingStep2_info = QLabel(self.groupBox_calibrationPreparingStep2)
        self.label_calibrationPreparingStep2_info.setObjectName(u"label_calibrationPreparingStep2_info")
        self.label_calibrationPreparingStep2_info.setFont(font10)
        self.label_calibrationPreparingStep2_info.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_calibrationPreparingStep2_info)

        self.verticalSpacer_calibrationPreparingStep_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_calibrationPreparingStep_2)


        self.verticalLayout_9.addWidget(self.groupBox_calibrationPreparingStep2)

        self.groupBox_calibrationPreparingStep3 = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain)
        self.groupBox_calibrationPreparingStep3.setObjectName(u"groupBox_calibrationPreparingStep3")
        self.groupBox_calibrationPreparingStep3.setFont(font3)
        self.groupBox_calibrationPreparingStep3.setFlat(True)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_calibrationPreparingStep3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_calibrationPreparingStep3_info = QLabel(self.groupBox_calibrationPreparingStep3)
        self.label_calibrationPreparingStep3_info.setObjectName(u"label_calibrationPreparingStep3_info")
        self.label_calibrationPreparingStep3_info.setFont(font10)
        self.label_calibrationPreparingStep3_info.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_calibrationPreparingStep3_info)

        self.verticalSpacer_calibrationPreparingStep_3 = QSpacerItem(20, 59, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_calibrationPreparingStep_3)


        self.verticalLayout_9.addWidget(self.groupBox_calibrationPreparingStep3)

        self.verticalSpacer_underChessboardSteps = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_underChessboardSteps)

        self.groupBox_calibrationSteps_1_3_ButtonsField = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain)
        self.groupBox_calibrationSteps_1_3_ButtonsField.setObjectName(u"groupBox_calibrationSteps_1_3_ButtonsField")
        self.groupBox_calibrationSteps_1_3_ButtonsField.setFlat(True)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_calibrationSteps_1_3_ButtonsField)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection = QPushButton(self.groupBox_calibrationSteps_1_3_ButtonsField)
        self.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection.setObjectName(u"pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection")
        self.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection.setFont(font3)

        self.horizontalLayout_4.addWidget(self.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection)

        self.horizontalSpacer_calibrationSteps_1_3_ButtonSpacer = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_calibrationSteps_1_3_ButtonSpacer)

        self.pushButton_calibrationChessboardSteps_1_3_GoToCalibration = QPushButton(self.groupBox_calibrationSteps_1_3_ButtonsField)
        self.pushButton_calibrationChessboardSteps_1_3_GoToCalibration.setObjectName(u"pushButton_calibrationChessboardSteps_1_3_GoToCalibration")
        self.pushButton_calibrationChessboardSteps_1_3_GoToCalibration.setFont(font3)

        self.horizontalLayout_4.addWidget(self.pushButton_calibrationChessboardSteps_1_3_GoToCalibration)


        self.verticalLayout_9.addWidget(self.groupBox_calibrationSteps_1_3_ButtonsField)


        self.verticalLayout_13.addWidget(self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_1_3_PreparingChessboardTips)
        self.page_calibrationSteps_1_3_PreparingRoomTips = QWidget()
        self.page_calibrationSteps_1_3_PreparingRoomTips.setObjectName(u"page_calibrationSteps_1_3_PreparingRoomTips")
        self.verticalLayout_33 = QVBoxLayout(self.page_calibrationSteps_1_3_PreparingRoomTips)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain = QGroupBox(self.page_calibrationSteps_1_3_PreparingRoomTips)
        self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain.setObjectName(u"groupBox_calibrationSteps_1_3_PreparingRoomTipsMain")
        self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain.setFont(font6)
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.groupBox_calibrationPreparingRoomTipsStep_1 = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain)
        self.groupBox_calibrationPreparingRoomTipsStep_1.setObjectName(u"groupBox_calibrationPreparingRoomTipsStep_1")
        self.groupBox_calibrationPreparingRoomTipsStep_1.setFont(font3)
        self.groupBox_calibrationPreparingRoomTipsStep_1.setFlat(True)
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_calibrationPreparingRoomTipsStep_1)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_calibrationPreparingRoomTipsStep1_Info = QLabel(self.groupBox_calibrationPreparingRoomTipsStep_1)
        self.label_calibrationPreparingRoomTipsStep1_Info.setObjectName(u"label_calibrationPreparingRoomTipsStep1_Info")
        self.label_calibrationPreparingRoomTipsStep1_Info.setFont(font10)
        self.label_calibrationPreparingRoomTipsStep1_Info.setWordWrap(True)

        self.verticalLayout_30.addWidget(self.label_calibrationPreparingRoomTipsStep1_Info)

        self.verticalSpacer_calibrationPreparingRoomTipsStep_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_calibrationPreparingRoomTipsStep_1)


        self.verticalLayout_29.addWidget(self.groupBox_calibrationPreparingRoomTipsStep_1)

        self.groupBox_calibrationPreparingRoomTipsStep_2 = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain)
        self.groupBox_calibrationPreparingRoomTipsStep_2.setObjectName(u"groupBox_calibrationPreparingRoomTipsStep_2")
        self.groupBox_calibrationPreparingRoomTipsStep_2.setFont(font3)
        self.groupBox_calibrationPreparingRoomTipsStep_2.setFlat(True)
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_calibrationPreparingRoomTipsStep_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_calibrationPreparingRoomTipsStep2_Info = QLabel(self.groupBox_calibrationPreparingRoomTipsStep_2)
        self.label_calibrationPreparingRoomTipsStep2_Info.setObjectName(u"label_calibrationPreparingRoomTipsStep2_Info")
        self.label_calibrationPreparingRoomTipsStep2_Info.setFont(font10)
        self.label_calibrationPreparingRoomTipsStep2_Info.setWordWrap(True)

        self.verticalLayout_31.addWidget(self.label_calibrationPreparingRoomTipsStep2_Info)

        self.verticalSpacer_calibrationPreparingRoomTipsStep_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_calibrationPreparingRoomTipsStep_2)


        self.verticalLayout_29.addWidget(self.groupBox_calibrationPreparingRoomTipsStep_2)

        self.groupBox_calibrationPreparingRoomTipsStep_3 = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain)
        self.groupBox_calibrationPreparingRoomTipsStep_3.setObjectName(u"groupBox_calibrationPreparingRoomTipsStep_3")
        self.groupBox_calibrationPreparingRoomTipsStep_3.setFont(font3)
        self.groupBox_calibrationPreparingRoomTipsStep_3.setFlat(True)
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_calibrationPreparingRoomTipsStep_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_calibrationPreparingRoomTipsStep3_Info = QLabel(self.groupBox_calibrationPreparingRoomTipsStep_3)
        self.label_calibrationPreparingRoomTipsStep3_Info.setObjectName(u"label_calibrationPreparingRoomTipsStep3_Info")
        self.label_calibrationPreparingRoomTipsStep3_Info.setFont(font10)
        self.label_calibrationPreparingRoomTipsStep3_Info.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.label_calibrationPreparingRoomTipsStep3_Info)

        self.verticalSpacer_calibrationPreparingRoomTipsStep_3 = QSpacerItem(20, 59, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_calibrationPreparingRoomTipsStep_3)


        self.verticalLayout_29.addWidget(self.groupBox_calibrationPreparingRoomTipsStep_3)

        self.verticalSpacer_calibrationRoomTipsUnderSteps = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_calibrationRoomTipsUnderSteps)

        self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField = QGroupBox(self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain)
        self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField.setObjectName(u"groupBox_calibrationRoomTipsSteps_1_3_ButtonsField")
        self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField.setFlat(True)
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection = QPushButton(self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField)
        self.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection.setObjectName(u"pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection")
        self.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection.setFont(font3)

        self.horizontalLayout_19.addWidget(self.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection)

        self.horizontalSpacer_calibrationRoomSteps_1_3_ButtonSpacer = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_calibrationRoomSteps_1_3_ButtonSpacer)

        self.pushButton_calibrationRoomSteps_1_3_GoToCalibration = QPushButton(self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField)
        self.pushButton_calibrationRoomSteps_1_3_GoToCalibration.setObjectName(u"pushButton_calibrationRoomSteps_1_3_GoToCalibration")
        self.pushButton_calibrationRoomSteps_1_3_GoToCalibration.setFont(font3)

        self.horizontalLayout_19.addWidget(self.pushButton_calibrationRoomSteps_1_3_GoToCalibration)


        self.verticalLayout_29.addWidget(self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField)


        self.verticalLayout_33.addWidget(self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_1_3_PreparingRoomTips)
        self.page_calibrationSteps_4_MainPage = QWidget()
        self.page_calibrationSteps_4_MainPage.setObjectName(u"page_calibrationSteps_4_MainPage")
        self.verticalLayout_15 = QVBoxLayout(self.page_calibrationSteps_4_MainPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox_calibrationSteps_4 = QGroupBox(self.page_calibrationSteps_4_MainPage)
        self.groupBox_calibrationSteps_4.setObjectName(u"groupBox_calibrationSteps_4")
        self.groupBox_calibrationSteps_4.setFont(font6)
        self.groupBox_calibrationSteps_4.setFlat(True)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_calibrationSteps_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.groupBox_calibrationImagesDirectoryField = QGroupBox(self.groupBox_calibrationSteps_4)
        self.groupBox_calibrationImagesDirectoryField.setObjectName(u"groupBox_calibrationImagesDirectoryField")
        self.groupBox_calibrationImagesDirectoryField.setFont(font3)
        self.groupBox_calibrationImagesDirectoryField.setFlat(True)
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_calibrationImagesDirectoryField)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_calibrationImagesDirectory = QLineEdit(self.groupBox_calibrationImagesDirectoryField)
        self.lineEdit_calibrationImagesDirectory.setObjectName(u"lineEdit_calibrationImagesDirectory")
        self.lineEdit_calibrationImagesDirectory.setFont(font10)

        self.horizontalLayout_12.addWidget(self.lineEdit_calibrationImagesDirectory)

        self.pushButton_setCalibrationImagesDirectory = QPushButton(self.groupBox_calibrationImagesDirectoryField)
        self.pushButton_setCalibrationImagesDirectory.setObjectName(u"pushButton_setCalibrationImagesDirectory")
        self.pushButton_setCalibrationImagesDirectory.setFont(font10)

        self.horizontalLayout_12.addWidget(self.pushButton_setCalibrationImagesDirectory)


        self.verticalLayout_14.addWidget(self.groupBox_calibrationImagesDirectoryField)

        self.groupBox_calibrationImagesDirectoryFieldSecondCamera = QGroupBox(self.groupBox_calibrationSteps_4)
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setObjectName(u"groupBox_calibrationImagesDirectoryFieldSecondCamera")
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setEnabled(True)
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setFont(font3)
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setFlat(True)
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setCheckable(True)
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setChecked(False)
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_calibrationImagesDirectoryFieldSecondCamera)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_calibrationImagesDirectorySecondCamera = QLineEdit(self.groupBox_calibrationImagesDirectoryFieldSecondCamera)
        self.lineEdit_calibrationImagesDirectorySecondCamera.setObjectName(u"lineEdit_calibrationImagesDirectorySecondCamera")
        self.lineEdit_calibrationImagesDirectorySecondCamera.setFont(font10)

        self.horizontalLayout_13.addWidget(self.lineEdit_calibrationImagesDirectorySecondCamera)

        self.pushButton_setCalibrationImagesDirectorySecondCamera = QPushButton(self.groupBox_calibrationImagesDirectoryFieldSecondCamera)
        self.pushButton_setCalibrationImagesDirectorySecondCamera.setObjectName(u"pushButton_setCalibrationImagesDirectorySecondCamera")
        self.pushButton_setCalibrationImagesDirectorySecondCamera.setFont(font10)

        self.horizontalLayout_13.addWidget(self.pushButton_setCalibrationImagesDirectorySecondCamera)


        self.verticalLayout_14.addWidget(self.groupBox_calibrationImagesDirectoryFieldSecondCamera)

        self.groupBox_chessboardSize_Setting = QGroupBox(self.groupBox_calibrationSteps_4)
        self.groupBox_chessboardSize_Setting.setObjectName(u"groupBox_chessboardSize_Setting")
        self.groupBox_chessboardSize_Setting.setFont(font3)
        self.groupBox_chessboardSize_Setting.setFlat(True)
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox_chessboardSize_Setting)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_chessboardSize_Setting_WidthTitle = QLabel(self.groupBox_chessboardSize_Setting)
        self.label_chessboardSize_Setting_WidthTitle.setObjectName(u"label_chessboardSize_Setting_WidthTitle")
        font13 = QFont()
        font13.setFamilies([u"Rubik"])
        font13.setPointSize(11)
        font13.setBold(False)
        self.label_chessboardSize_Setting_WidthTitle.setFont(font13)

        self.horizontalLayout_22.addWidget(self.label_chessboardSize_Setting_WidthTitle)

        self.spinBox_chessboardSize_Setting_WidthInput = QSpinBox(self.groupBox_chessboardSize_Setting)
        self.spinBox_chessboardSize_Setting_WidthInput.setObjectName(u"spinBox_chessboardSize_Setting_WidthInput")
        self.spinBox_chessboardSize_Setting_WidthInput.setFont(font12)
        self.spinBox_chessboardSize_Setting_WidthInput.setValue(11)

        self.horizontalLayout_22.addWidget(self.spinBox_chessboardSize_Setting_WidthInput)

        self.label_chessboardSize_Setting_HeightTitle = QLabel(self.groupBox_chessboardSize_Setting)
        self.label_chessboardSize_Setting_HeightTitle.setObjectName(u"label_chessboardSize_Setting_HeightTitle")
        self.label_chessboardSize_Setting_HeightTitle.setFont(font13)

        self.horizontalLayout_22.addWidget(self.label_chessboardSize_Setting_HeightTitle)

        self.spinBox_chessboardSize_Setting_HeightInput = QSpinBox(self.groupBox_chessboardSize_Setting)
        self.spinBox_chessboardSize_Setting_HeightInput.setObjectName(u"spinBox_chessboardSize_Setting_HeightInput")
        self.spinBox_chessboardSize_Setting_HeightInput.setFont(font12)
        self.spinBox_chessboardSize_Setting_HeightInput.setValue(7)

        self.horizontalLayout_22.addWidget(self.spinBox_chessboardSize_Setting_HeightInput)

        self.horizontalSpacer_chessboardSize_Setting = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_chessboardSize_Setting)


        self.verticalLayout_14.addWidget(self.groupBox_chessboardSize_Setting)

        self.label_3 = QLabel(self.groupBox_calibrationSteps_4)
        self.label_3.setObjectName(u"label_3")
        font14 = QFont()
        font14.setFamilies([u"Rubik"])
        font14.setPointSize(10)
        font14.setBold(False)
        font14.setItalic(True)
        self.label_3.setFont(font14)

        self.verticalLayout_14.addWidget(self.label_3)

        self.pushButton_calibrationProcessStart = QPushButton(self.groupBox_calibrationSteps_4)
        self.pushButton_calibrationProcessStart.setObjectName(u"pushButton_calibrationProcessStart")
        self.pushButton_calibrationProcessStart.setFont(font3)

        self.verticalLayout_14.addWidget(self.pushButton_calibrationProcessStart)

        self.graphicsView_calibrationProcessView = QGraphicsView(self.groupBox_calibrationSteps_4)
        self.graphicsView_calibrationProcessView.setObjectName(u"graphicsView_calibrationProcessView")
        self.graphicsView_calibrationProcessView.setMinimumSize(QSize(0, 0))

        self.verticalLayout_14.addWidget(self.graphicsView_calibrationProcessView)

        self.progressBar_calibrationProcessProgress = QProgressBar(self.groupBox_calibrationSteps_4)
        self.progressBar_calibrationProcessProgress.setObjectName(u"progressBar_calibrationProcessProgress")
        self.progressBar_calibrationProcessProgress.setFont(font12)
        self.progressBar_calibrationProcessProgress.setValue(24)

        self.verticalLayout_14.addWidget(self.progressBar_calibrationProcessProgress)

        self.textBrowser_calibrationProcessLogs = QTextBrowser(self.groupBox_calibrationSteps_4)
        self.textBrowser_calibrationProcessLogs.setObjectName(u"textBrowser_calibrationProcessLogs")
        self.textBrowser_calibrationProcessLogs.setMaximumSize(QSize(16777215, 120))
        self.textBrowser_calibrationProcessLogs.setFont(font3)

        self.verticalLayout_14.addWidget(self.textBrowser_calibrationProcessLogs)

        self.groupBox_calibrationSteps_4_ButtonField = QGroupBox(self.groupBox_calibrationSteps_4)
        self.groupBox_calibrationSteps_4_ButtonField.setObjectName(u"groupBox_calibrationSteps_4_ButtonField")
        self.groupBox_calibrationSteps_4_ButtonField.setFlat(True)
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_calibrationSteps_4_ButtonField)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_calibrationSteps_4_returnToTipsButton = QPushButton(self.groupBox_calibrationSteps_4_ButtonField)
        self.pushButton_calibrationSteps_4_returnToTipsButton.setObjectName(u"pushButton_calibrationSteps_4_returnToTipsButton")
        self.pushButton_calibrationSteps_4_returnToTipsButton.setFont(font3)

        self.horizontalLayout_18.addWidget(self.pushButton_calibrationSteps_4_returnToTipsButton)

        self.horizontalSpacer_calibrationSteps_4_ButtonSpacer = QSpacerItem(602, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_calibrationSteps_4_ButtonSpacer)


        self.verticalLayout_14.addWidget(self.groupBox_calibrationSteps_4_ButtonField)


        self.verticalLayout_15.addWidget(self.groupBox_calibrationSteps_4)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_4_MainPage)
        self.page_calibrationSteps_5_ImageDotsCreating = QWidget()
        self.page_calibrationSteps_5_ImageDotsCreating.setObjectName(u"page_calibrationSteps_5_ImageDotsCreating")
        self.verticalLayout_27 = QVBoxLayout(self.page_calibrationSteps_5_ImageDotsCreating)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.groupBox_ImageDotsCreatorField = QGroupBox(self.page_calibrationSteps_5_ImageDotsCreating)
        self.groupBox_ImageDotsCreatorField.setObjectName(u"groupBox_ImageDotsCreatorField")
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_ImageDotsCreatorField)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.groupBox_dotsCreatorImagePreviewField = QGroupBox(self.groupBox_ImageDotsCreatorField)
        self.groupBox_dotsCreatorImagePreviewField.setObjectName(u"groupBox_dotsCreatorImagePreviewField")
        self.groupBox_dotsCreatorImagePreviewField.setFlat(True)
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_dotsCreatorImagePreviewField)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_imageDotsCreator_ImageName = QLabel(self.groupBox_dotsCreatorImagePreviewField)
        self.label_imageDotsCreator_ImageName.setObjectName(u"label_imageDotsCreator_ImageName")

        self.verticalLayout_34.addWidget(self.label_imageDotsCreator_ImageName)

        self.graphicsView_imageDotsCreator_ImagePreview = QGraphicsView(self.groupBox_dotsCreatorImagePreviewField)
        self.graphicsView_imageDotsCreator_ImagePreview.setObjectName(u"graphicsView_imageDotsCreator_ImagePreview")

        self.verticalLayout_34.addWidget(self.graphicsView_imageDotsCreator_ImagePreview)

        self.groupBox_imageDotsCreator_ButtonsField = QGroupBox(self.groupBox_dotsCreatorImagePreviewField)
        self.groupBox_imageDotsCreator_ButtonsField.setObjectName(u"groupBox_imageDotsCreator_ButtonsField")
        self.groupBox_imageDotsCreator_ButtonsField.setFlat(True)
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_imageDotsCreator_ButtonsField)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_imageDotsCreator_getPreviousImage = QPushButton(self.groupBox_imageDotsCreator_ButtonsField)
        self.pushButton_imageDotsCreator_getPreviousImage.setObjectName(u"pushButton_imageDotsCreator_getPreviousImage")
        self.pushButton_imageDotsCreator_getPreviousImage.setFont(font)

        self.horizontalLayout_20.addWidget(self.pushButton_imageDotsCreator_getPreviousImage)

        self.horizontalSpacer_imageDotsCreator_betweenButtons = QSpacerItem(505, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_imageDotsCreator_betweenButtons)

        self.pushButton_imageDotsCreator_getNextImage = QPushButton(self.groupBox_imageDotsCreator_ButtonsField)
        self.pushButton_imageDotsCreator_getNextImage.setObjectName(u"pushButton_imageDotsCreator_getNextImage")
        self.pushButton_imageDotsCreator_getNextImage.setFont(font)

        self.horizontalLayout_20.addWidget(self.pushButton_imageDotsCreator_getNextImage)


        self.verticalLayout_34.addWidget(self.groupBox_imageDotsCreator_ButtonsField)


        self.horizontalLayout_21.addWidget(self.groupBox_dotsCreatorImagePreviewField)

        self.tableWidget_imageDotsCreator_DotsData = QTableWidget(self.groupBox_ImageDotsCreatorField)
        if (self.tableWidget_imageDotsCreator_DotsData.columnCount() < 3):
            self.tableWidget_imageDotsCreator_DotsData.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_imageDotsCreator_DotsData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_imageDotsCreator_DotsData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_imageDotsCreator_DotsData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_imageDotsCreator_DotsData.setObjectName(u"tableWidget_imageDotsCreator_DotsData")
        self.tableWidget_imageDotsCreator_DotsData.setFont(font)
        self.tableWidget_imageDotsCreator_DotsData.horizontalHeader().setDefaultSectionSize(40)
        self.tableWidget_imageDotsCreator_DotsData.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_21.addWidget(self.tableWidget_imageDotsCreator_DotsData)


        self.verticalLayout_27.addWidget(self.groupBox_ImageDotsCreatorField)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_5_ImageDotsCreating)
        self.page_calibrationSteps_5_done = QWidget()
        self.page_calibrationSteps_5_done.setObjectName(u"page_calibrationSteps_5_done")
        self.verticalLayout_17 = QVBoxLayout(self.page_calibrationSteps_5_done)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_calibrationSteps_5_doneMain = QGroupBox(self.page_calibrationSteps_5_done)
        self.groupBox_calibrationSteps_5_doneMain.setObjectName(u"groupBox_calibrationSteps_5_doneMain")
        self.groupBox_calibrationSteps_5_doneMain.setFont(font6)
        self.groupBox_calibrationSteps_5_doneMain.setFlat(True)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_calibrationSteps_5_doneMain)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_calibrationSteps_5_done_resultsTitle = QLabel(self.groupBox_calibrationSteps_5_doneMain)
        self.label_calibrationSteps_5_done_resultsTitle.setObjectName(u"label_calibrationSteps_5_done_resultsTitle")
        self.label_calibrationSteps_5_done_resultsTitle.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_calibrationSteps_5_done_resultsTitle)

        self.textBrowser_calibrationResultsData = QTextBrowser(self.groupBox_calibrationSteps_5_doneMain)
        self.textBrowser_calibrationResultsData.setObjectName(u"textBrowser_calibrationResultsData")

        self.verticalLayout_16.addWidget(self.textBrowser_calibrationResultsData)

        self.groupBox_calibrationSteps_5_doneContinueOptions = QGroupBox(self.groupBox_calibrationSteps_5_doneMain)
        self.groupBox_calibrationSteps_5_doneContinueOptions.setObjectName(u"groupBox_calibrationSteps_5_doneContinueOptions")
        self.groupBox_calibrationSteps_5_doneContinueOptions.setFlat(True)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_calibrationSteps_5_doneContinueOptions)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_cancelCalibration = QPushButton(self.groupBox_calibrationSteps_5_doneContinueOptions)
        self.pushButton_cancelCalibration.setObjectName(u"pushButton_cancelCalibration")
        self.pushButton_cancelCalibration.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_cancelCalibration)

        self.horizontalSpacer_calibrationSteps_5_buttonsBetween = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_calibrationSteps_5_buttonsBetween)

        self.pushButton_saveCalibrationResults = QPushButton(self.groupBox_calibrationSteps_5_doneContinueOptions)
        self.pushButton_saveCalibrationResults.setObjectName(u"pushButton_saveCalibrationResults")
        self.pushButton_saveCalibrationResults.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_saveCalibrationResults)


        self.verticalLayout_16.addWidget(self.groupBox_calibrationSteps_5_doneContinueOptions)


        self.verticalLayout_17.addWidget(self.groupBox_calibrationSteps_5_doneMain)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_5_done)

        self.horizontalLayout_7.addWidget(self.stackedWidget_workSpace)


        self.horizontalLayout_2.addWidget(self.groupBox_workspace)


        self.horizontalLayout.addWidget(self.groupBox_main)


        self.retranslateUi(Widget)

        self.pushButton_pageCalibration.setDefault(False)
        self.stackedWidget_workSpace.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox_main.setTitle("")
        self.groupBox_pagesAndSettings.setTitle("")
        self.label_appLogo.setText(QCoreApplication.translate("Widget", u"<APP LOGO>", None))
        self.groupBox_pages.setTitle("")
        self.pushButton_pageCalibration.setText(QCoreApplication.translate("Widget", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.pushButton_pageProcess.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.groupBox_settingsAndTheme.setTitle("")
        self.pushButton_settings.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.pushButton_themeToggle.setText(QCoreApplication.translate("Widget", u"\u0422\u0435\u043c\u0430", None))
        self.groupBox_workspace.setTitle("")
        self.groupBox_page_calibrationInitialChoiceOptions.setTitle("")
        self.groupBox_page_calibrationFromFileOptionField.setTitle("")
        self.label_page_calibrationFromFileOptionTitle.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.label_page_calibrationFromFileOptionIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_page_calibrationFromFileOptionButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_page_0_calibrationStartOptionField.setTitle("")
        self.label_page_calibrationStartOptionTitle.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.label_page_calibrationStartOptionIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_page_calibrationStartOptionButton.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_page_calibrationSkipOptionField.setTitle("")
        self.label_page_calibrationSkipOptionTitle.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.label_page_calibrationSkipOptionText.setText(QCoreApplication.translate("Widget", u"\u0411\u0435\u0437 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043c\u043e\u0436\u0435\u0442 \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043d\u0438\u0437\u0438\u0442\u044c\u0441\u044f.", None))
        self.label_page_calibrationSkipOptionIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_page_calibrationSkipOptionButton.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_calibrationSteps_0_MethodSelectionMain.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u043e\u0440 \u043c\u0435\u0442\u043e\u0434\u0430 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438", None))
        self.groupBox_calibrationSteps_0_CalibrationMethodsSelectionField.setTitle("")
        self.groupBox_calibrationSteps_0_MethodAutoField.setTitle("")
        self.label_calibrationSteps_0_MethodAutoTitle.setText(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439", None))
        self.label_calibrationSteps_0_MethodAutoIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_calibrationSteps_0_MethodAutoSelectButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_calibrationSteps_0_MethodManualField.setTitle("")
        self.label_calibrationSteps_0_MethodManualTitle.setText(QCoreApplication.translate("Widget", u"\u0420\u0443\u0447\u043d\u043e\u0439", None))
        self.label_calibrationSteps_0_MethodManualIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_calibrationSteps_0_MethodManualSelectButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_calibrationSteps_0_MethodSelectionMainButtonsField.setTitle("")
        self.pushButton_returnToCalibrationChoice.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.groupBox_processingProjectOptions.setTitle("")
        self.groupBox_newProject.setTitle("")
        self.label_newProjectTitle.setText(QCoreApplication.translate("Widget", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.label_newProjectIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_newProject.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox_chooseProject.setTitle("")
        self.label_chooseProjectTitle.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.label_chooseProjectIcon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_chooseProject.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_newProjectCreatingMain.setTitle(QCoreApplication.translate("Widget", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.label_newProjectCreatingNameFieldTitle.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430", None))
        self.lineEdit_newProjectCreatingNameField.setText("")
        self.label_newProjectCreatingPathFieldTitle.setText(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u043f\u0440\u043e\u0435\u043a\u0442\u0443", None))
        self.groupBox_newProjectCreatingPath.setTitle("")
        self.pushButton_newProjectCreatingPathChoose.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_newProjectCreatingSubmitField.setTitle("")
        self.pushButton_newProjectCreatingCancel.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_newProjectCreatingSubmit.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox_processingProcessMain.setTitle(QCoreApplication.translate("Widget", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.groupBox_processPathSetter_Field.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c", None))
        self.pushButton_imagesDirectoryChoose.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_secondCameraProcessingField.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c \u0441\u043e \u0432\u0442\u043e\u0440\u043e\u0439 \u043a\u0430\u043c\u0435\u0440\u044b (\u0440\u0435\u0436\u0438\u043c \u0441\u0442\u0435\u0440\u0435\u043e\u043a\u0430\u043c\u0435\u0440\u044b)", None))
        self.pushButton_setSecondCameraProcessingImagesDirectory.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.checkBox_preprocessingImages.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0435\u0434\u043e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043e\u0447\u043d\u044b\u043c \u0434\u0430\u043d\u043d\u044b\u043c", None))
        self.pushButton_processingStart.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0443", None))
        self.textBrowser_processingLogs.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rubik'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">logging information...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">starting some process</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"
                        "9pt;\">fatal error, 404 not found :)</span></p></body></html>", None))
        self.groupBox_exportOptions.setTitle("")
        self.pushButton_exportAsDotsCloud.setText(QCoreApplication.translate("Widget", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u043e\u0431\u043b\u0430\u043a\u0430 \u0442\u043e\u0447\u0435\u043a", None))
        self.pushButton_exportAsObjectFile.setText(QCoreApplication.translate("Widget", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.groupBox_settingsMain.setTitle(QCoreApplication.translate("Widget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_settingsTempText.setText(QCoreApplication.translate("Widget", u"\u0422\u0443\u0442 \u043a\u043e\u0433\u0434\u0430-\u0442\u043e \u043f\u043e\u044f\u0432\u044f\u0442\u0441\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435\u043c", None))
        self.groupBox_calibrationSteps_1_3_PreparingChessboardTipsMain.setTitle(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430 \u043a \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0435", None))
        self.groupBox_calibrationPreparingStep1.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 1. \u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0439\u0442\u0435 \u0448\u0430\u0445\u043c\u0430\u0442\u043d\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438.", None))
        self.label_calibrationPreparingStep1_info.setText(QCoreApplication.translate("Widget", u"\u0428\u0430\u0445\u043c\u0430\u0442\u043d\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d \u043d\u0443\u0436\u0435\u043d \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043a\u0430\u043c\u0435\u0440\u044b.", None))
        self.groupBox_calibrationPreparingStep2.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 2. \u0412\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u043e\u0441\u0432\u0435\u0449\u0435\u043d\u0438\u0435 \u0438 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u044c\u0442\u0435 \u043a\u0430\u043c\u0435\u0440\u0443.", None))
        self.label_calibrationPreparingStep2_info.setText(QCoreApplication.translate("Widget", u"\u041e\u0441\u0432\u0435\u0449\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0440\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u044b\u043c, \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u0438\u0437\u0431\u0435\u0436\u0430\u0442\u044c \u0442\u0435\u043d\u0435\u0439 \u043d\u0430 \u0448\u0430\u0431\u043b\u043e\u043d\u0435.", None))
        self.groupBox_calibrationPreparingStep3.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 3. \u041e\u0442\u0441\u043d\u0438\u043c\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.label_calibrationPreparingStep3_info.setText(QCoreApplication.translate("Widget", u"\u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u043c\u0438\u043d\u0438\u043c\u0443\u043c 20 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u043d\u0438\u0439 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0441 \u0440\u0430\u0437\u043d\u044b\u0445 \u0441\u0442\u043e\u0440\u043e\u043d.\n"
"\u0421\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u0441\u043e\u0431\u043b\u044e\u0434\u0430\u0442\u044c \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u043a\u0430\u043c\u0435\u0440\u044b \u0434\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430. \u041f\u043e\u0441\u043b\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0439\u0442\u0435 \u0435\u0434\u0438\u043d\u044b\u0439 \u0434\u0430\u0442\u0430c\u0435\u0442 (\u0434\u043b\u044f \u043a\u0430\u0436"
                        "\u0434\u043e\u0439 \u043a\u0430\u043c\u0435\u0440\u044b - \u0441\u0432\u043e\u044f \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f \u0441 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c\u0438).\n"
"\n"
"\u041f\u043e\u0441\u043b\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u0434\u043b\u044f \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u0430 \u043a \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c\u0443 \u044d\u0442\u0430\u043f\u0443.", None))
        self.groupBox_calibrationSteps_1_3_ButtonsField.setTitle("")
        self.pushButton_calibrationChessboardSteps_1_3_ReturnToMethodSelection.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_calibrationChessboardSteps_1_3_GoToCalibration.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0435", None))
        self.groupBox_calibrationSteps_1_3_PreparingRoomTipsMain.setTitle(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430 \u043a \u0440\u0443\u0447\u043d\u043e\u0439 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0435", None))
        self.groupBox_calibrationPreparingRoomTipsStep_1.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 1. \u041e\u0442\u0441\u043d\u0438\u043c\u0438\u0442\u0435 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043e\u0447\u043d\u044b\u0439 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.label_calibrationPreparingRoomTipsStep1_Info.setText(QCoreApplication.translate("Widget", u"\u0412 \u0434\u0430\u043d\u043d\u043e\u043c \u0440\u0435\u0436\u0438\u043c\u0435 \u0432 \u0432\u0438\u0434\u0435 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0432\u044b\u0441\u0442\u0443\u043f\u0430\u0435\u0442 \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043e\u0447\u043d\u0430\u044f \u043a\u043e\u043c\u043d\u0430\u0442\u0430. \u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0441\u043d\u044f\u0442\u044c \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u043c\u0438\u043d\u0438\u043c\u0443\u043c 20 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439 \u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0445 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442 \u0442\u043e\u0447\u0435\u043a.", None))
        self.groupBox_calibrationPreparingRoomTipsStep_2.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 2. \u0420\u0430\u0437\u043c\u0435\u0442\u044c\u0442\u0435 \u0442\u043e\u0447\u043a\u0438 \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u0445", None))
        self.label_calibrationPreparingRoomTipsStep2_Info.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u043b\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0445 \u044d\u0442\u0430\u043f\u0430\u0445 \u0432\u0430\u043c \u0431\u0443\u0434\u0435\u0442 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043e \u0440\u0430\u0437\u043c\u0435\u0442\u0438\u0442\u044c \u0432\u0440\u0443\u0447\u043d\u0443\u044e \u0442\u043e\u0447\u043a\u0438 \u043d\u0430 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043b\u0435\u043d\u043d\u044b\u0445 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u0445. \u041f\u043e\u0441\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u044d\u0442\u043e \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u0442\u043e\u0447\u043d\u043e.", None))
        self.groupBox_calibrationPreparingRoomTipsStep_3.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 3. \u0412\u043d\u0435\u0441\u0438\u0442\u0435 \u043d\u043e\u043c\u0435\u0440\u0430 \u0442\u043e\u0447\u0435\u043a \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.label_calibrationPreparingRoomTipsStep3_Info.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0441\u043b\u0435 \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u0438 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u0445 \u0431\u0443\u0434\u0435\u0442 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0432\u043d\u0435\u0441\u0442\u0438 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443 (\u0438\u043b\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u044c \u0443\u0436\u0435 \u0433\u043e\u0442\u043e\u0432\u0443\u044e) \u0441 \u0441\u043e\u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435\u043c \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0445 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u0432 \u0442\u043e\u0447\u0435\u043a \u043d\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u0445 \u0438 \u0438\u0445 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0445 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442.", None))
        self.groupBox_calibrationRoomTipsSteps_1_3_ButtonsField.setTitle("")
        self.pushButton_calibrationRoomSteps_1_3_ReturnToMethodSelection.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_calibrationRoomSteps_1_3_GoToCalibration.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0435", None))
        self.groupBox_calibrationSteps_4.setTitle(QCoreApplication.translate("Widget", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox_calibrationImagesDirectoryField.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c", None))
        self.pushButton_setCalibrationImagesDirectory.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c \u0441\u043e \u0432\u0442\u043e\u0440\u043e\u0439 \u043a\u0430\u043c\u0435\u0440\u044b (\u0441\u0442\u0435\u0440\u0435\u043e\u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430)", None))
        self.pushButton_setCalibrationImagesDirectorySecondCamera.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_chessboardSize_Setting.setTitle(QCoreApplication.translate("Widget", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0430\u0445\u043c\u0430\u0442\u043d\u043e\u0439 \u0434\u043e\u0441\u043a\u0438", None))
        self.label_chessboardSize_Setting_WidthTitle.setText(QCoreApplication.translate("Widget", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.label_chessboardSize_Setting_HeightTitle.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0438\u043c\u0435\u0447\u0435\u043d\u0438\u0435: \u0432 \u0440\u0430\u0437\u043c\u0435\u0440\u0435 \u0448\u0430\u0445\u043c\u0430\u0442\u043d\u043e\u0439 \u0434\u043e\u0441\u043a\u0438 \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u043f\u0435\u0440\u0435\u043a\u0440\u0435\u0441\u0442\u0438\u0439 \u043f\u043e \u0448\u0438\u0440\u0438\u043d\u0435 \u0438 \u0432\u044b\u0441\u043e\u0442\u0435 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e", None))
        self.pushButton_calibrationProcessStart.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.textBrowser_calibrationProcessLogs.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rubik'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">&lt;PROCESSING LOGS HERE&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">process started...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-si"
                        "ze:9pt;\">some exception skipped</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">it's all going on, keep calm</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">deleting windows...</span></p></body></html>", None))
        self.groupBox_calibrationSteps_4_ButtonField.setTitle("")
        self.pushButton_calibrationSteps_4_returnToTipsButton.setText(QCoreApplication.translate("Widget", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.groupBox_ImageDotsCreatorField.setTitle(QCoreApplication.translate("Widget", u"\u0420\u0430\u0437\u043c\u0435\u0442\u043a\u0430 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.groupBox_dotsCreatorImagePreviewField.setTitle("")
        self.label_imageDotsCreator_ImageName.setText(QCoreApplication.translate("Widget", u"<<image name>>", None))
        self.groupBox_imageDotsCreator_ButtonsField.setTitle("")
        self.pushButton_imageDotsCreator_getPreviousImage.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0435\u0435", None))
        self.pushButton_imageDotsCreator_getNextImage.setText(QCoreApplication.translate("Widget", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435", None))
        ___qtablewidgetitem = self.tableWidget_imageDotsCreator_DotsData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_imageDotsCreator_DotsData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"X", None));
        ___qtablewidgetitem2 = self.tableWidget_imageDotsCreator_DotsData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Y", None));
        self.groupBox_calibrationSteps_5_doneMain.setTitle(QCoreApplication.translate("Widget", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0430!", None))
        self.label_calibrationSteps_5_done_resultsTitle.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:", None))
        self.textBrowser_calibrationResultsData.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Rubik'; font-size:14pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.groupBox_calibrationSteps_5_doneContinueOptions.setTitle("")
        self.pushButton_cancelCalibration.setText(QCoreApplication.translate("Widget", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_saveCalibrationResults.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

