from PyQt5.QtWidgets import QVBoxLayout, QTextEdit
import sys

class ConsoleWidget(QTextEdit):
    """Console is where output is generated."""
    def __init__(self, parent = None):
        super(ConsoleWidget, self).__init__()

        # Get table widget from parent (parent of StudentTableWidget is MainWindow)
        self.console = parent.ui.console_textEdit

        # Connect signals and slots
        # self.console.cellChanged.connect(self.on_item_changed)
        
    
    def setup_ui(self):
        """Set up the console widget"""
        # Disable editing
        self.console.setReadOnly(True)

    def println(self, text):
        """Method called when printing to stdout"""
        # Append the text to the QTextEdit
        self.console.append(text+'\n')
        #self.console.setText(text)
        
