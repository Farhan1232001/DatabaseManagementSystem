from PyQt5.QtWidgets import QVBoxLayout, QTextEdit
import sys

class ConsoleWidget(QTextEdit):
    """Console is where output is generated."""
    def __init__(self):
        super().__init__()
        
    
    def setup_ui(self):
        """Set up the console widget"""
        # Disable editing
        self.setReadOnly(True)

    def write(self, text):
        """Method called when printing to stdout"""
        # Append the text to the QTextEdit
        #self.append(text)
        self.setText(text)
        
