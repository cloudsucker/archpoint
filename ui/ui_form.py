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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)

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
        self.page_calibrationChoice = QWidget()
        self.page_calibrationChoice.setObjectName(u"page_calibrationChoice")
        self.gridLayout_3 = QGridLayout(self.page_calibrationChoice)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_calibration_options = QGroupBox(self.page_calibrationChoice)
        self.groupBox_calibration_options.setObjectName(u"groupBox_calibration_options")
        self.groupBox_calibration_options.setFlat(True)
        self.gridLayout_2 = QGridLayout(self.groupBox_calibration_options)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_calibration_from_file = QGroupBox(self.groupBox_calibration_options)
        self.groupBox_calibration_from_file.setObjectName(u"groupBox_calibration_from_file")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_calibration_from_file)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_calibration_from_file_title = QLabel(self.groupBox_calibration_from_file)
        self.label_calibration_from_file_title.setObjectName(u"label_calibration_from_file_title")
        font6 = QFont()
        font6.setFamilies([u"Rubik"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_calibration_from_file_title.setFont(font6)

        self.verticalLayout_4.addWidget(self.label_calibration_from_file_title)

        self.label_calibration_from_file_icon = QLabel(self.groupBox_calibration_from_file)
        self.label_calibration_from_file_icon.setObjectName(u"label_calibration_from_file_icon")
        font7 = QFont()
        font7.setFamilies([u"Rubik"])
        font7.setPointSize(20)
        font7.setBold(False)
        self.label_calibration_from_file_icon.setFont(font7)

        self.verticalLayout_4.addWidget(self.label_calibration_from_file_icon)

        self.pushButton_calibration_from_file = QPushButton(self.groupBox_calibration_from_file)
        self.pushButton_calibration_from_file.setObjectName(u"pushButton_calibration_from_file")
        self.pushButton_calibration_from_file.setFont(font5)

        self.verticalLayout_4.addWidget(self.pushButton_calibration_from_file)


        self.gridLayout_2.addWidget(self.groupBox_calibration_from_file, 0, 0, 1, 1)

        self.groupBox_calibration_start = QGroupBox(self.groupBox_calibration_options)
        self.groupBox_calibration_start.setObjectName(u"groupBox_calibration_start")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_calibration_start)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_calibration_start_title = QLabel(self.groupBox_calibration_start)
        self.label_calibration_start_title.setObjectName(u"label_calibration_start_title")
        self.label_calibration_start_title.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_calibration_start_title)

        self.label_calibration_start_icon = QLabel(self.groupBox_calibration_start)
        self.label_calibration_start_icon.setObjectName(u"label_calibration_start_icon")
        font8 = QFont()
        font8.setFamilies([u"Rubik"])
        font8.setPointSize(20)
        self.label_calibration_start_icon.setFont(font8)

        self.verticalLayout_5.addWidget(self.label_calibration_start_icon)

        self.pushButton_calibration_start = QPushButton(self.groupBox_calibration_start)
        self.pushButton_calibration_start.setObjectName(u"pushButton_calibration_start")
        self.pushButton_calibration_start.setFont(font5)

        self.verticalLayout_5.addWidget(self.pushButton_calibration_start)


        self.gridLayout_2.addWidget(self.groupBox_calibration_start, 0, 1, 1, 1)

        self.groupBox_calibration_skip = QGroupBox(self.groupBox_calibration_options)
        self.groupBox_calibration_skip.setObjectName(u"groupBox_calibration_skip")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_calibration_skip)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_calibration_skip_title = QLabel(self.groupBox_calibration_skip)
        self.label_calibration_skip_title.setObjectName(u"label_calibration_skip_title")
        self.label_calibration_skip_title.setFont(font6)

        self.verticalLayout_6.addWidget(self.label_calibration_skip_title)

        self.label_calibration_skip_text = QLabel(self.groupBox_calibration_skip)
        self.label_calibration_skip_text.setObjectName(u"label_calibration_skip_text")
        self.label_calibration_skip_text.setFont(font)
        self.label_calibration_skip_text.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_calibration_skip_text)

        self.label_calibration_skip_icon = QLabel(self.groupBox_calibration_skip)
        self.label_calibration_skip_icon.setObjectName(u"label_calibration_skip_icon")
        font9 = QFont()
        font9.setFamilies([u"Rubik"])
        font9.setPointSize(20)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_calibration_skip_icon.setFont(font9)

        self.verticalLayout_6.addWidget(self.label_calibration_skip_icon)

        self.pushButton_calibration_skip = QPushButton(self.groupBox_calibration_skip)
        self.pushButton_calibration_skip.setObjectName(u"pushButton_calibration_skip")

        self.verticalLayout_6.addWidget(self.pushButton_calibration_skip)


        self.gridLayout_2.addWidget(self.groupBox_calibration_skip, 1, 0, 1, 2)


        self.gridLayout_3.addWidget(self.groupBox_calibration_options, 1, 0, 1, 1)

        self.verticalSpacer_calibrationChoiceOptionsBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_calibrationChoiceOptionsBottom, 2, 0, 1, 1)

        self.verticalSpacer_calibrationChoiceOptionsTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_calibrationChoiceOptionsTop, 0, 0, 1, 1)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationChoice)
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
        self.groupBox_processingProcessMain.setFlat(True)
        self.verticalLayout_22 = QVBoxLayout(self.groupBox_processingProcessMain)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.groupBox_imagesPath = QGroupBox(self.groupBox_processingProcessMain)
        self.groupBox_imagesPath.setObjectName(u"groupBox_imagesPath")
        self.groupBox_imagesPath.setFlat(True)
        self.verticalLayout_23 = QVBoxLayout(self.groupBox_imagesPath)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_imagesDirectoryFieldTitle = QLabel(self.groupBox_imagesPath)
        self.label_imagesDirectoryFieldTitle.setObjectName(u"label_imagesDirectoryFieldTitle")

        self.verticalLayout_23.addWidget(self.label_imagesDirectoryFieldTitle)

        self.groupBox = QGroupBox(self.groupBox_imagesPath)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_imagesDirectoryField = QLineEdit(self.groupBox)
        self.lineEdit_imagesDirectoryField.setObjectName(u"lineEdit_imagesDirectoryField")
        self.lineEdit_imagesDirectoryField.setFont(font10)

        self.horizontalLayout_11.addWidget(self.lineEdit_imagesDirectoryField)

        self.pushButton_imagesDirectoryChoose = QPushButton(self.groupBox)
        self.pushButton_imagesDirectoryChoose.setObjectName(u"pushButton_imagesDirectoryChoose")
        self.pushButton_imagesDirectoryChoose.setFont(font4)

        self.horizontalLayout_11.addWidget(self.pushButton_imagesDirectoryChoose)


        self.verticalLayout_23.addWidget(self.groupBox)


        self.verticalLayout_22.addWidget(self.groupBox_imagesPath)

        self.pushButton_processingStart = QPushButton(self.groupBox_processingProcessMain)
        self.pushButton_processingStart.setObjectName(u"pushButton_processingStart")
        self.pushButton_processingStart.setFont(font3)

        self.verticalLayout_22.addWidget(self.pushButton_processingStart)

        self.graphicsView_dotsVisualization = QGraphicsView(self.groupBox_processingProcessMain)
        self.graphicsView_dotsVisualization.setObjectName(u"graphicsView_dotsVisualization")

        self.verticalLayout_22.addWidget(self.graphicsView_dotsVisualization)

        self.progressBar_processingProgressBar = QProgressBar(self.groupBox_processingProcessMain)
        self.progressBar_processingProgressBar.setObjectName(u"progressBar_processingProgressBar")
        self.progressBar_processingProgressBar.setFont(font)
        self.progressBar_processingProgressBar.setValue(24)

        self.verticalLayout_22.addWidget(self.progressBar_processingProgressBar)

        self.textBrowser_processingLogs = QTextBrowser(self.groupBox_processingProcessMain)
        self.textBrowser_processingLogs.setObjectName(u"textBrowser_processingLogs")
        self.textBrowser_processingLogs.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_22.addWidget(self.textBrowser_processingLogs)

        self.groupBox_exportOptions = QGroupBox(self.groupBox_processingProcessMain)
        self.groupBox_exportOptions.setObjectName(u"groupBox_exportOptions")
        self.groupBox_exportOptions.setFlat(True)
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_exportOptions)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_exportAsDotsCloud = QPushButton(self.groupBox_exportOptions)
        self.pushButton_exportAsDotsCloud.setObjectName(u"pushButton_exportAsDotsCloud")

        self.horizontalLayout_10.addWidget(self.pushButton_exportAsDotsCloud)

        self.horizontalSpacer_exportOptions_buttonsBetween = QSpacerItem(374, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_exportOptions_buttonsBetween)

        self.pushButton_exportAsObjectFile = QPushButton(self.groupBox_exportOptions)
        self.pushButton_exportAsObjectFile.setObjectName(u"pushButton_exportAsObjectFile")

        self.horizontalLayout_10.addWidget(self.pushButton_exportAsObjectFile)


        self.verticalLayout_22.addWidget(self.groupBox_exportOptions)


        self.verticalLayout_21.addWidget(self.groupBox_processingProcessMain)

        self.stackedWidget_workSpace.addWidget(self.page_processingProcess)
        self.page_calibrationSteps_1_3 = QWidget()
        self.page_calibrationSteps_1_3.setObjectName(u"page_calibrationSteps_1_3")
        self.verticalLayout_13 = QVBoxLayout(self.page_calibrationSteps_1_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox_calibrationSteps_1_3_main = QGroupBox(self.page_calibrationSteps_1_3)
        self.groupBox_calibrationSteps_1_3_main.setObjectName(u"groupBox_calibrationSteps_1_3_main")
        self.groupBox_calibrationSteps_1_3_main.setFont(font6)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_calibrationSteps_1_3_main)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_calibrationPreparingStep1 = QGroupBox(self.groupBox_calibrationSteps_1_3_main)
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

        self.groupBox_calibrationPreparingStep2 = QGroupBox(self.groupBox_calibrationSteps_1_3_main)
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

        self.groupBox_calibrationPreparingStep3 = QGroupBox(self.groupBox_calibrationSteps_1_3_main)
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

        self.verticalSpacer_underSteps = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_underSteps)

        self.groupBox_calibrationStartFromPreparing = QGroupBox(self.groupBox_calibrationSteps_1_3_main)
        self.groupBox_calibrationStartFromPreparing.setObjectName(u"groupBox_calibrationStartFromPreparing")
        self.groupBox_calibrationStartFromPreparing.setFlat(True)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_calibrationStartFromPreparing)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_calibrationStartFromPreparing = QSpacerItem(494, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_calibrationStartFromPreparing)

        self.pushButton_calibrationStartFromPreparing = QPushButton(self.groupBox_calibrationStartFromPreparing)
        self.pushButton_calibrationStartFromPreparing.setObjectName(u"pushButton_calibrationStartFromPreparing")
        self.pushButton_calibrationStartFromPreparing.setFont(font3)

        self.horizontalLayout_4.addWidget(self.pushButton_calibrationStartFromPreparing)


        self.verticalLayout_9.addWidget(self.groupBox_calibrationStartFromPreparing)


        self.verticalLayout_13.addWidget(self.groupBox_calibrationSteps_1_3_main)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_1_3)
        self.page_calibrationSteps_4 = QWidget()
        self.page_calibrationSteps_4.setObjectName(u"page_calibrationSteps_4")
        self.verticalLayout_15 = QVBoxLayout(self.page_calibrationSteps_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox_calibrationSteps_4 = QGroupBox(self.page_calibrationSteps_4)
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
        font12 = QFont()
        font12.setFamilies([u"Rubik"])
        font12.setPointSize(10)
        font12.setBold(False)
        self.progressBar_calibrationProcessProgress.setFont(font12)
        self.progressBar_calibrationProcessProgress.setValue(24)

        self.verticalLayout_14.addWidget(self.progressBar_calibrationProcessProgress)

        self.textBrowser_calibrationProcessLogs = QTextBrowser(self.groupBox_calibrationSteps_4)
        self.textBrowser_calibrationProcessLogs.setObjectName(u"textBrowser_calibrationProcessLogs")
        self.textBrowser_calibrationProcessLogs.setMaximumSize(QSize(16777215, 120))
        self.textBrowser_calibrationProcessLogs.setFont(font3)

        self.verticalLayout_14.addWidget(self.textBrowser_calibrationProcessLogs)


        self.verticalLayout_15.addWidget(self.groupBox_calibrationSteps_4)

        self.stackedWidget_workSpace.addWidget(self.page_calibrationSteps_4)
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
        self.pushButton_continueWithoutSavingCalibrationResults = QPushButton(self.groupBox_calibrationSteps_5_doneContinueOptions)
        self.pushButton_continueWithoutSavingCalibrationResults.setObjectName(u"pushButton_continueWithoutSavingCalibrationResults")
        self.pushButton_continueWithoutSavingCalibrationResults.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_continueWithoutSavingCalibrationResults)

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
        self.stackedWidget_workSpace.setCurrentIndex(3)


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
        self.pushButton_settings.setText(QCoreApplication.translate("Widget", u"\u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0418", None))
        self.pushButton_themeToggle.setText(QCoreApplication.translate("Widget", u"\u0422\u0415\u041c\u0410", None))
        self.groupBox_workspace.setTitle("")
        self.groupBox_calibration_options.setTitle("")
        self.groupBox_calibration_from_file.setTitle("")
        self.label_calibration_from_file_title.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.label_calibration_from_file_icon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_calibration_from_file.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_calibration_start.setTitle("")
        self.label_calibration_start_title.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.label_calibration_start_icon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_calibration_start.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_calibration_skip.setTitle("")
        self.label_calibration_skip_title.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.label_calibration_skip_text.setText(QCoreApplication.translate("Widget", u"\u0411\u0435\u0437 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u043c\u043e\u0436\u0435\u0442 \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u043d\u0438\u0437\u0438\u0442\u044c\u0441\u044f.", None))
        self.label_calibration_skip_icon.setText(QCoreApplication.translate("Widget", u"<ICON>", None))
        self.pushButton_calibration_skip.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
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
        self.pushButton_newProjectCreatingSubmit.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox_processingProcessMain.setTitle("")
        self.groupBox_imagesPath.setTitle("")
        self.label_imagesDirectoryFieldTitle.setText(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c", None))
        self.groupBox.setTitle("")
        self.pushButton_imagesDirectoryChoose.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
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
        self.groupBox_calibrationSteps_1_3_main.setTitle(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0430 \u043a \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0435", None))
        self.groupBox_calibrationPreparingStep1.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 1. \u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0439\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438.", None))
        self.label_calibrationPreparingStep1_info.setText(QCoreApplication.translate("Widget", u"\u0428\u0430\u0431\u043b\u043e\u043d \u043d\u0443\u0436\u0435\u043d \u0434\u043b\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.groupBox_calibrationPreparingStep2.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 2. \u0412\u043a\u043b\u044e\u0447\u0438\u0442\u0435 \u043e\u0441\u0432\u0435\u0449\u0435\u043d\u0438\u0435 \u0438 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u044c\u0442\u0435 \u043a\u0430\u043c\u0435\u0440\u0443.", None))
        self.label_calibrationPreparingStep2_info.setText(QCoreApplication.translate("Widget", u"\u041e\u0441\u0432\u0435\u0449\u0435\u043d\u0438\u0435 \u0434\u043e\u043b\u0436\u043d\u043e \u0431\u044b\u0442\u044c \u0440\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u044b\u043c, \u043f\u043e\u0441\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u0438\u0437\u0431\u0435\u0436\u0430\u0442\u044c \u0442\u0435\u043d\u0435\u0439 \u043d\u0430 \u0448\u0430\u0431\u043b\u043e\u043d\u0435.", None))
        self.groupBox_calibrationPreparingStep3.setTitle(QCoreApplication.translate("Widget", u"\u0428\u0430\u0433 3. \u041e\u0442\u0441\u043d\u0438\u043c\u0438\u0442\u0435 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b", None))
        self.label_calibrationPreparingStep3_info.setText(QCoreApplication.translate("Widget", u"\u0421\u0434\u0435\u043b\u0430\u0439\u0442\u0435 \u043c\u0438\u043d\u0438\u043c\u0443\u043c 20 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u043d\u0438\u0439 \u0448\u0430\u0431\u043b\u043e\u043d\u0430 \u0441 \u0440\u0430\u0437\u043d\u044b\u0445 \u0441\u0442\u043e\u0440\u043e\u043d. \u0421\u0442\u0430\u0440\u0430\u0439\u0442\u0435\u0441\u044c \u0441\u043e\u0431\u043b\u044e\u0434\u0430\u0442\u044c \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u043e\u0435 \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043e\u0442 \u043a\u0430\u043c\u0435\u0440\u044b \u0434\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430. \u041f\u043e\u0441\u043b\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430 \u0441\u0444\u043e\u0440\u043c\u0438\u0440\u0443\u0439\u0442\u0435 \u0435\u0434\u0438\u043d\u044b\u0439 \u0434\u0430\u0442\u0430\u0435\u0442 \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u0434\u043b\u044f \u043f"
                        "\u0435\u0440\u0435\u0445\u043e\u0434\u0430 \u043a \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c\u0443 \u044d\u0442\u0430\u043f\u0443.", None))
        self.groupBox_calibrationStartFromPreparing.setTitle("")
        self.pushButton_calibrationStartFromPreparing.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0443", None))
        self.groupBox_calibrationSteps_4.setTitle(QCoreApplication.translate("Widget", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.groupBox_calibrationImagesDirectoryField.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c", None))
        self.pushButton_setCalibrationImagesDirectory.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.groupBox_calibrationImagesDirectoryFieldSecondCamera.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c \u0441\u043e \u0432\u0442\u043e\u0440\u043e\u0439 \u043a\u0430\u043c\u0435\u0440\u044b (\u0441\u0442\u0435\u0440\u0435\u043e\u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430)", None))
        self.pushButton_setCalibrationImagesDirectorySecondCamera.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
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
        self.pushButton_continueWithoutSavingCalibrationResults.setText(QCoreApplication.translate("Widget", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435\n"
"\u0431\u0435\u0437 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton_saveCalibrationResults.setText(QCoreApplication.translate("Widget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

