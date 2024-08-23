import requests
import sys
from interfaces.main import Ui_MainWindow as Main
from PyQt5.QtWidgets import QMainWindow, QApplication
from config import ip, port, protocol


class MainApp(QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer.setReadOnly(True)
        self.setStyleSheet('background-color: #67c33a;')
        self.send.clicked.connect(self.get_event)

    def get_event(self):
        auto_number = self.auto_number.text()
        answer = requests.get(f"{protocol}://{ip}:{port}/api/{auto_number}")
        event = bool(answer.json()['event'])
        if event:
            message = answer.json()['message']
        else:
            message = "no notification"
        self.answer.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    App = MainApp()
    App.show()
    sys.exit(app.exec_())
