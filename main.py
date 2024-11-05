import sys
import os
from ui import Ui_Widget
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QPlainTextEdit, QMessageBox, QFileDialog, QTextEdit, QCheckBox
import subprocess
from datetime import datetime
import shutil



class MainWindow(QMainWindow, Ui_Widget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # Set up the UI

        # Connect buttons to their functions
        self.sign_certificate_pushButton.clicked.connect(self.sign_certificate)
        self.pushButton.clicked.connect(self.spoof_extension)
        self.upload_icon_pushButton.clicked.connect(self.upload_icon)
        self.payload_path_pushButton.clicked.connect(self.select_payload_path)
        self.pushButton.clicked.connect(self.spoof_extension)
        self.upload_icon_pushButton.clicked.connect(self.upload_icon)
        self.extspoof_option_checkBox.stateChanged.connect(self.toggle_extension_spoofer_tab)
        self.ev_certificate_option_checkBox.stateChanged.connect(self.toggle_custom_certificate_tab)
        self.custom_icon_option_checkBox.stateChanged.connect(self.toggle_custom_icon_tab)
        self.initialize_stats_display()
        self.certificate_common_name_comboBox.currentIndexChanged.connect(self.update_console_output)
        self.certificate_orginization_comboBox.currentIndexChanged.connect(self.update_console_output)
        self.certificate_organizational_unit_comboBox.currentIndexChanged.connect(self.update_console_output)
        self.certificate_locality_comboBox.currentIndexChanged.connect(self.update_console_output)
        self.state_certificate_comboBox.currentIndexChanged.connect(self.update_console_output)
        self.certificate_country_comboBox.currentIndexChanged.connect(self.update_console_output)
        self.disable_specific_tabs()
        self.payload_binding_pushButton.clicked.connect(self.bind_payload)
        self.update_settings_display()  # Initial update
        
        # Connect to relevant signals
        self.payload_path_textedit.textChanged.connect(self.update_settings_display)
        self.certificate_common_name_comboBox.currentTextChanged.connect(self.update_settings_display)
        self.certificate_orginization_comboBox.currentTextChanged.connect(self.update_settings_display)



    def bind_payload(self):
        # Open a file dialog to select an EXE file
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        exe_file, _ = QFileDialog.getOpenFileName(self, "Select EXE File", "", "Executable Files (*.exe);;All Files (*)", options=options)
        
        if exe_file:
            # Set the selected EXE file path in payload_binding_textEdit
            self.payload_binding_textEdit.setPlainText(exe_file)

            # Display current settings in binding_console_textEdit
            cn = self.certificate_common_name_comboBox.currentText() or '[Not Set]'
            org = self.certificate_orginization_comboBox.currentText() or '[Not Set]'
            ou = self.certificate_organizational_unit_comboBox.currentText() or '[Not Set]'
            locality = self.certificate_locality_comboBox.currentText() or '[Not Set]'
            state = self.state_certificate_comboBox.currentText() or '[Not Set]'
            country = self.certificate_country_comboBox.currentText() or '[Not Set]'

            settings_message = (
                f"Settings:\n"
                f"Common Name (CN): {cn}\n"
                f"Organization (O): {org}\n"
                f"Organizational Unit (OU): {ou}\n"
                f"Locality (L): {locality}\n"
                f"State (ST): {state}\n"
                f"Country (C): {country}\n"
                f"Payload Path: {exe_file}"
            )

            self.binding_console_textEdit.setPlainText(settings_message)
        else:
            QMessageBox.warning(self, "No File Selected", "Please select a valid EXE file.")



    def initialize_stats_display(self):
        # Create the formatted output for initial display with HTML formatting
        stats_info = (
            "<b>------------- L33T Cryptic ---------------</b><br>"
            "<font color='red'><b>File Path:</b></font> [Not Selected]<br>"
            "<font color='red'><b>File Name:</b></font> [Not Selected]<br>"
            "<font color='red'><b>File Extension:</b></font> [Not Selected]<br><br>"
            "<b>------------- L33T Options ---------------</b><br>"
            "<font color='red'><b>Custom Certificate:</b></font> [Not Set]<br>"
            "<font color='red'><b>Custom Extension Spoofing:</b></font> [Not Set]<br>"
            "<font color='red'><b>Custom Icon:</b></font> [Not Set]<br>"
            "<br><font color='yellow'><b>Waiting...</b></font><br>"
        )
    
        # Display the formatted stats in the current_stats_QFrame_textEdit
        self.current_stats_QFrame_textEdit.setHtml(stats_info)  # Use setHtml for HTML formatting
    
    def select_payload_path(self):
        # Open a file dialog to select an executable file
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Executable", "", "Executable Files (*.exe);;All Files (*)", options=options)
    
        if file_path:
            # Get the current text in the QTextEdit
            current_text = self.payload_path_textedit.toPlainText()
    
            # Check if the file path is already in the QTextEdit
            if file_path not in current_text.splitlines():
                # Append the new file path to the QTextEdit
                self.payload_path_textedit.append(file_path)
    
                # Extract file name and extension
                file_name = os.path.basename(file_path)
                file_extension = os.path.splitext(file_name)[1]  # Get the file extension
    
                # Create the formatted output with HTML formatting
                stats_info = (
                    "<b>------------- L33T Cryptic ---------------</b><br>"
                    f"<font color='lime'><b>File Path:</b></font> {file_path}<br>"
                    f"<font color='lime'><b>File Name:</b></font> {file_name}<br>"
                    f"<font color='lime'><b>File Extension:</b></font> {file_extension}<br><br>"
                    "<b>------------- L33T Options ---------------</b><br>"
                    "<font color='red'><b>Custom Certificate:</b></font> [Not Set]<br>"
                    "<font color='red'><b>Custom Extension Spoofing:</b></font> [Not Set]<br>"
                    "<font color='red'><b>Custom Icon:</b></font> [Not Set]<br>"
                    "<br><font color='yellow'><b>Waiting...</b></font><br>"
                )
    
                # Display the formatted stats in the current_stats_QFrame_textEdit
                self.current_stats_QFrame_textEdit.setHtml(stats_info)  # Use setHtml for HTML formatting
            else:
                QMessageBox.warning(self, "Duplicate Entry", "This file path is already listed.")



    def toggle_extension_spoofer_tab(self, state):
        if state == 2:  # 2 means CHECKED
            self.features_qtabwidget.setTabEnabled(self.features_qtabwidget.indexOf(self.extension_spoofer_tab_settings), True)
        else:
            self.features_qtabwidget.setTabEnabled(self.features_qtabwidget.indexOf(self.extension_spoofer_tab_settings), False)

    def toggle_custom_certificate_tab(self, state):
        if state == 2:  # 2 means CHECKED
            # Enable the custom certificate tab
            index = self.features_qtabwidget.indexOf(self.custom_certificate_tab_settings)
            self.features_qtabwidget.setTabEnabled(index, True)
    
            # Get current values from all combo boxes with default fallbacks
            cn = self.certificate_common_name_comboBox.currentText() or '[Not Set]'
            org = self.certificate_orginization_comboBox.currentText() or '[Not Set]'
            ou = self.certificate_organizational_unit_comboBox.currentText() or '[Not Set]'
            locality = self.certificate_locality_comboBox.currentText() or '[Not Set]'
            state_value = self.state_certificate_comboBox.currentText() or '[Not Set]'
            country = self.certificate_country_comboBox.currentText() or '[Not Set]'
    
            # Prepare output message in HTML format
            output_message = (
                "<b>------------- L33T Certificate Information ---------------</b><br>"
                f"<font color='{'green' if cn != '[Not Set]' else 'red'}'><b>Common Name (CN):</b></font> {cn}<br>"
                f"<font color='{'green' if org != '[Not Set]' else 'red'}'><b>Organization (O):</b></font> {org}<br>"
                f"<font color='{'green' if ou != '[Not Set]' else 'red'}'><b>Organizational Unit (OU):</b></font> {ou}<br>"
                f"<font color='{'green' if locality != '[Not Set]' else 'red'}'><b>Locality (L):</b></font> {locality}<br>"
                f"<font color='{'green' if state_value != '[Not Set]' else 'red'}'><b>State (ST):</b></font> {state_value}<br>"
                f"<font color='{'green' if country != '[Not Set]' else 'red'}'><b>Country (C):</b></font> {country}<br>"
            )
    
            # Set HTML content in the custom certificate console text edit
            if hasattr(self, 'custom_certificate_console_textEdit'):
                self.custom_certificate_console_textEdit.setHtml(output_message)
    
        else:
            # Disable the custom certificate tab
            index = self.features_qtabwidget.indexOf(self.custom_certificate_tab_settings)
            self.features_qtabwidget.setTabEnabled(index, False)
    
            # Optionally clear or reset the console text edit if needed
            if hasattr(self, 'custom_certificate_console_textEdit'):
                self.custom_certificate_console_textEdit.clear()  # Clear text when unchecked
    
            # Reset label color back to red if unchecked
            output_message = (
                "<b>------------- L33T Certificate Information ---------------</b><br>"
                "<font color='red'><b>Common Name (CN):</b></font> [Not Set]<br>"
                "<font color='red'><b>Organization (O):</b></font> [Not Set]<br>"
                "<font color='red'><b>Organizational Unit (OU):</b></font> [Not Set]<br>"
                "<font color='red'><b>Locality (L):</b></font> [Not Set]<br>"
                "<font color='red'><b>State (ST):</b></font> [Not Set]<br>"
                "<font color='red'><b>Country (C):</b></font> [Not Set]<br>"
            )
    
            # Update custom certificate console text edit with reset message
            if hasattr(self, 'custom_certificate_console_textEdit'):
                self.custom_certificate_console_textEdit.setHtml(output_message)



    def toggle_custom_icon_tab(self, state):
        if state == 2:  # 2 means CHECKED
            self.features_qtabwidget.setTabEnabled(self.features_qtabwidget.indexOf(self.custom_icon_tab_settings), True)
        else:
            self.features_qtabwidget.setTabEnabled(self.features_qtabwidget.indexOf(self.custom_icon_tab_settings), False)

    def log_message(self, message):
        """Append a message to the custom log console."""
        self.custom_certificate_console_textEdit.append(message)

    def sign_certificate(self):
        # Retrieve user inputs for the certificate
        cn = self.certificate_common_name_comboBox.currentText()
        org = self.certificate_orginization_comboBox.currentText()
        ou = self.certificate_organizational_unit_comboBox.currentText()
        locality = self.certificate_locality_comboBox.currentText()
        state = self.state_certificate_comboBox.currentText()
        country = self.certificate_country_comboBox.currentText()
    
        # Get the payload path from the text edit
        payload_path = self.payload_path_textedit.toPlainText().strip()
    
        # Validate the payload path
        if not payload_path or not os.path.isfile(payload_path) or not payload_path.lower().endswith('.exe'):
            QMessageBox.warning(self, "Invalid Payload", "Please provide a valid EXE file path in the payload path text edit.")
            return
    
        # Create date-based directory structure
        current_date = datetime.now().strftime("%Y%m%d")
        base_directory = "Signed_Payloads"
        date_directory = os.path.join(base_directory, current_date)
        original_directory = os.path.join(date_directory, "Original")
        signed_directory = os.path.join(date_directory, "Signed")
        certificate_directory = os.path.join(date_directory, "Certificate")
    
        # Create all necessary directories
        os.makedirs(original_directory, exist_ok=True)
        os.makedirs(signed_directory, exist_ok=True)
        os.makedirs(certificate_directory, exist_ok=True)
    
        # Copy the original payload to the Original directory
        try:
            self.log_message("Copying original payload...")
            original_payload_path = os.path.join(original_directory, os.path.basename(payload_path))
            shutil.copy(payload_path, original_payload_path)
            self.log_message(f"Original payload copied to: {original_payload_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to copy original payload:\n{str(e)}")
            return
    
        # Define paths for private key and CSR
        private_key_path = os.path.join(certificate_directory, "private.key")
        csr_path = os.path.join(certificate_directory, "request.csr")
        cert_file_path = os.path.join(certificate_directory, "certificate.crt")
        pfx_file_path = os.path.join(certificate_directory, "certificate.pfx")
    
        # Step 1: Generate private key
        try:
            self.log_message("Generating private key...")
            subprocess.run(["openssl", "genrsa", "-out", private_key_path, "2048"], check=True)
            self.log_message("Private key generated successfully.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to generate private key:\n{e.stderr}")
            return
    
        # Step 2: Create CSR
        try:
            self.log_message("Creating Certificate Signing Request (CSR)...")
            openssl_cmd = [
                "openssl", "req", "-new", "-key", private_key_path, "-out", csr_path,
                "-subj", f"/C={country}/ST={state}/L={locality}/O={org}/OU={ou}/CN={cn}/emailAddress=noreply@example.com"
            ]
            subprocess.run(openssl_cmd, check=True)
            self.log_message("CSR created successfully.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to create CSR:\n{e.stderr}")
            return
    
        # Step 3: Generate Self-Signed Certificate
        try:
            self.log_message("Generating self-signed certificate...")
            subprocess.run(["openssl", "x509", "-req", "-days", "365", "-in", csr_path, "-signkey", private_key_path, "-out", cert_file_path], check=True)
            self.log_message("Self-signed certificate generated successfully.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to create self-signed certificate:\n{e.stderr}")
            return
    
        # Step 4: Combine private key and certificate into a .pfx file
        cert_password = "your_certificate_password"  # Set your certificate password
        try:
            self.log_message("Creating PFX file...")
            subprocess.run(["openssl", "pkcs12", "-export", "-out", pfx_file_path, "-inkey", private_key_path, "-in", cert_file_path, "-password", f"pass:{cert_password}"], check=True)
            self.log_message("PFX file created successfully.")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, "Error", f"Failed to create PFX file:\n{e.stderr}")
            return
    
        # Now you can use pfx_file_path with signtool
        signtool_command = [
            r"C:\Program Files (x86)\Microsoft SDKs\ClickOnce\SignTool\signtool.exe",
            "sign",
            "/f", pfx_file_path,
            "/p", cert_password,
            "/tr", "http://timestamp.digicert.com",
            "/td", "SHA256",
            "/fd", "SHA256",
            payload_path
        ]
    
        self.log_message("Starting the signing process...")
    
        try:
            # Execute the signing command
            result = subprocess.run(signtool_command, check=True, capture_output=True, text=True)
    
            # If successful, copy the signed executable to the Signed directory
            if result.returncode == 0:
                self.log_message("Signing completed successfully.")
    
                # Get the current time for the new filename
                current_time = datetime.now().strftime("%H%M%S")
                signed_exe_name = f"{current_time}_signed_{os.path.basename(payload_path)}"
                signed_exe_path = os.path.join(signed_directory, signed_exe_name)
    
                # Copy the signed executable to the Signed directory
                shutil.copy(payload_path, signed_exe_path)
                
                # Display paths
                message = (f"Successfully signed certificate.\n"
                        f"Signed EXE is located at:\n{signed_exe_path}\n"
                        f"Certificate file is located at:\n{cert_file_path}")
                QMessageBox.information(self, "Sign Certificate", message)
    
                # Log paths in the console
                self.log_message(f"Signed EXE Path: {signed_exe_path}")
                self.log_message(f"Certificate Path: {cert_file_path}")
    
            else:
                error_msg = f"Failed to sign the executable:\n{result.stderr}"
                self.log_message(error_msg)
                QMessageBox.critical(self, "Signing Error", error_msg)
    
        except subprocess.CalledProcessError as e:
            error_msg = f"An error occurred while signing:\n{e.stderr}"
            self.log_message(error_msg)
            QMessageBox.critical(self, "Signing Error", error_msg)

    def disable_specific_tabs(self):
        # Disable custom certificate tab
        self.features_qtabwidget.setTabEnabled(
            self.features_qtabwidget.indexOf(self.custom_certificate_tab_settings), False)
        
        # Disable custom icon tab
        self.features_qtabwidget.setTabEnabled(
            self.features_qtabwidget.indexOf(self.custom_icon_tab_settings), False)
        
        # Disable extension spoofer tab
        self.features_qtabwidget.setTabEnabled(
            self.features_qtabwidget.indexOf(self.extension_spoofer_tab_settings), False)
        
        # Disable host it tab (assuming it exists)
        if hasattr(self, 'host_it_tab'):
            self.features_qtabwidget.setTabEnabled(
                self.features_qtabwidget.indexOf(self.host_it_tab), False)



    def spoof_extension(self):
        # Functionality for spoofing file extensions
        selected_extensions = []
        if self.extspoof_xlxs_checkBox.isChecked():
            selected_extensions.append('.xlxs')
        if self.extspoof_pdf_checkBox.isChecked():
            selected_extensions.append('.pdf')
        if self.extspoof_jpg_checkBox.isChecked():
            selected_extensions.append('.jpg')
        if self.extspoof_jpeg_checkBox.isChecked():
            selected_extensions.append('.jpeg')
        if self.extspoof_php_checkBox.isChecked():
            selected_extensions.append('.php')
        if self.extspoof_slx_checkBox.isChecked():
            selected_extensions.append('.slx')
        if self.extspoof_doc_checkBox.isChecked():
            selected_extensions.append('.doc')

        # Placeholder for spoofing extensions
        QMessageBox.information(self, "Spoof Extensions", f"Spoofing the following extensions: {', '.join(selected_extensions)}")

    def upload_icon(self):
        # Functionality for uploading an icon
        # Placeholder code for icon upload functionality
        QMessageBox.information(self, "Upload Icon", "Icon upload functionality not implemented.")




    def update_console_output(self):
        # Get current values from all combo boxes
        cn = self.certificate_common_name_comboBox.currentText()
        org = self.certificate_orginization_comboBox.currentText()
        ou = self.certificate_organizational_unit_comboBox.currentText()
        locality = self.certificate_locality_comboBox.currentText()
        state_value = self.state_certificate_comboBox.currentText()  # Renamed to avoid conflict with 'state'
        country = self.certificate_country_comboBox.currentText()
    
        # Prepare output message in HTML format
        output_message = (
            "<b>------------- L33T Certificate Information ---------------</b><br>"
            f"<font color='{'green' if cn else 'red'}'><b>Common Name (CN):</b></font> {cn or '[Not Set]'}<br>"
            f"<font color='{'green' if org else 'red'}'><b>Organization (O):</b></font> {org or '[Not Set]'}<br>"
            f"<font color='{'green' if ou else 'red'}'><b>Organizational Unit (OU):</b></font> {ou or '[Not Set]'}<br>"
            f"<font color='{'green' if locality else 'red'}'><b>Locality (L):</b></font> {locality or '[Not Set]'}<br>"
            f"<font color='{'green' if state_value else 'red'}'><b>State (ST):</b></font> {state_value or '[Not Set]'}<br>"
            f"<font color='{'green' if country else 'red'}'><b>Country (C):</b></font> {country or '[Not Set]'}<br>"
        )
    
        # Set HTML content in the custom certificate console text edit
        if hasattr(self, 'custom_certificate_console_textEdit'):
            self.custom_certificate_console_textEdit.setHtml(output_message)
        

    def update_settings_display(self):
        # Get the file path from the payload_path_textedit
        file_path = self.payload_path_textedit.toPlainText().strip()
        
        if file_path:
            file_name = os.path.basename(file_path)
            file_extension = os.path.splitext(file_name)[1]
            original_stats_status = "✔"
        else:
            file_path = "[Not Selected]"
            file_name = "[Not Selected]"
            file_extension = "[Not Selected]"
            original_stats_status = "❌"
    
        # Get current values from all combo boxes
        cn = self.certificate_common_name_comboBox.currentText()
        org = self.certificate_orginization_comboBox.currentText()
        ou = self.certificate_organizational_unit_comboBox.currentText()
        locality = self.certificate_locality_comboBox.currentText()
        state_value = self.state_certificate_comboBox.currentText()
        country = self.certificate_country_comboBox.currentText()
    
        # Check certificate status
        cert_fields = [cn, org, ou, locality, state_value, country]
        if all(cert_fields):
            cert_status = "✔"
        elif any(cert_fields):
            cert_status = "⚠"
        else:
            cert_status = "❌"
    
        # Get custom certificate status
        custom_certificate_enabled = self.ev_certificate_option_checkBox.isChecked()
        custom_certificate = "Enabled" if custom_certificate_enabled else "Disabled"
        custom_certificate_status = "✔" if custom_certificate_enabled else "❌"
    
        # Get custom icon status
        custom_icon_enabled = self.custom_icon_option_checkBox.isChecked()
        custom_icon = "Enabled" if custom_icon_enabled else "Disabled"
        custom_icon_status = "✔" if custom_icon_enabled else "❌"
    
        # Get spoofing feature status
        spoofing_enabled = self.extspoof_option_checkBox.isChecked()
        spoofing_feature = "Enabled" if spoofing_enabled else "Disabled"
        spoofing_status = "✔" if spoofing_enabled else "❌"
    
        # Get self hosting status
        self_hosting_enabled = self.self_hosting_checkBox.isChecked()
        self_hosting = "Enabled" if self_hosting_enabled else "Disabled"
        self_hosting_status = "✔" if self_hosting_enabled else "❌"
    
        # L33T Options status
        l33t_options_status = "✔" if custom_certificate_enabled or custom_icon_enabled or spoofing_enabled or self_hosting_enabled else "❌"
    
        # Construct the display text in HTML format
        display_text = f"""
        <b> ----------- Original Payload {original_stats_status} ----------- </b><br>
        File Path: {file_path}<br>
        File Name: {file_name}<br>
        File Extension: {file_extension}<br><br>
    
        <b>------------ Basic Options {l33t_options_status} --------------</b><br>
        """
    
        # Custom Certificate
        if custom_certificate_enabled:
            display_text += f"<font color='blue'><b>Custom Certificate:</b> {custom_certificate} ✓</font><br>"
        else:
            display_text += f"<font color='{'green' if custom_certificate_enabled else 'red'}'><b>Custom Certificate:</b></font> {custom_certificate}<br>"
    
        # Custom Icon
        if custom_icon_enabled:
            display_text += f"<font color='blue'><b>Custom Icon:</b> {custom_icon} ✓</font><br>"
        else:
            display_text += f"<font color='{'green' if custom_icon_enabled else 'red'}'><b>Custom Icon:</b></font> {custom_icon}<br>"
    
        # Extension Spoofing
        if spoofing_enabled:
            display_text += f"<font color='blue'><b>Extension Spoofing:</b> {spoofing_feature} ✓</font><br>"
        else:
            display_text += f"<font color='{'green' if spoofing_enabled else 'red'}'><b>Extension Spoofing:</b></font> {spoofing_feature}<br>"
    
        # Self Hosting
        display_text += f"<font color='{'green' if self_hosting_enabled else 'red'}'><b>Self Hosting:</b></font> {self_hosting}<br><br>"
    
        display_text += f"""
        <b>------------- Certificate {custom_certificate_status} ---------------</b><br>
        """
    
        if custom_certificate_enabled:
            display_text += f"""
            <font color='{'green' if cn else 'red'}'><b>Common Name (CN):</b></font> {cn or '[Not Set]'}<br>
            <font color='{'green' if org else 'red'}'><b>Organization (O):</b></font> {org or '[Not Set]'}<br>
            <font color='{'green' if ou else 'red'}'><b>Organizational Unit (OU):</b></font> {ou or '[Not Set]'}<br>
            <font color='{'green' if locality else 'red'}'><b>Locality (L):</b></font> {locality or '[Not Set]'}<br>
            <font color='{'green' if state_value else 'red'}'><b>State (ST):</b></font> {state_value or '[Not Set]'}<br>
            <font color='{'green' if country else 'red'}'><b>Country (C):</b></font> {country or '[Not Set]'}<br>
            """
        else:
            display_text += "<font color='gray'>[Disabled]</font><br>"
    
        display_text += f"""
        <br>
        <b>-------------- Spoofing {spoofing_status} ----------------</b><br>
        """
        if spoofing_enabled:
            display_text += f"Spoofing Feature: {spoofing_feature}<br>"
        else:
            display_text += "<font color='gray'>[Disabled]</font><br>"
    
        display_text += f"""
        <br>
        <b>------------ Custom Icon {custom_icon_status} ---------------</b><br>
        """
        if custom_icon_enabled:
            display_text += f"Custom Icon: {custom_icon}<br>"
        else:
            display_text += "<font color='gray'>[Disabled]</font><br>"
    
        display_text += f"""
        <br>
        <b>------------- Self Hosting {self_hosting_status} ---------------</b><br>
        """
        if self_hosting_enabled:
            display_text += f"Self Hosting: {self_hosting}"
        else:
            display_text += "<font color='gray'>[Disabled]</font>"
    
        # Update the settings_totality_textEdit with HTML content
        self.settings_totality_textEdit.setHtml(display_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())