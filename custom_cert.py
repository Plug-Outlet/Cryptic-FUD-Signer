def toggle_custom_certificate_tab(self, state):
    if state == 2:  # 2 means CHECKED
        # Enable the custom certificate tab
        index = self.features_qtabwidget.indexOf(self.custom_certificate_tab_settings)
        self.features_qtabwidget.setTabEnabled(index, True)

        # Change label color to yellow and set status
        custom_cert_label_html = "<font color='yellow'>Custom Certificate:</font> <i>[Setting In Place...]</i><br>"
        stats_info = f"<b>------------- L33T Options ---------------</b><br>{custom_cert_label_html}<font color='red'>Waiting...</font>"
        self.current_stats_QFrame_textEdit.setHtml(stats_info)

        # Start flashing effect for the custom certificate tab
        if not self.flashing:
            self.flashing_timer.start(500)  # Flash every 500 ms
            self.flashing = True  # Set flashing state to active

    else:
        # Disable the custom certificate tab
        index = self.features_qtabwidget.indexOf(self.custom_certificate_tab_settings)
        self.features_qtabwidget.setTabEnabled(index, False)

        # Reset label color back to red if unchecked
        custom_cert_label_html = "<font color='red'>Custom Certificate:</font> <i>[Not Set]</i><br>"
        stats_info = f"<b>------------- L33T Options ---------------</b><br>{custom_cert_label_html}<font color='red'>Waiting...</font>"
        self.current_stats_QFrame_textEdit.setHtml(stats_info)

        # Stop flashing effect and reset tab appearance
        if self.flashing:
            self.flashing_timer.stop()
            self.reset_custom_certificate_tab()  # Reset tab appearance