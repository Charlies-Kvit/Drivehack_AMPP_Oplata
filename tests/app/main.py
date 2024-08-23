import requests
import sys
from interfaces.main import Ui_MainWindow as Main
from interfaces.login import Ui_Form as Login
from interfaces.register import Ui_Form as Reg
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
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

    def login(self):
        w = Login()
        w.show()


class Login(QWidget, Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signin_btn.clicked.connect(self.loging)

    def loging(self):
        if self.login.text() != "" and self.password.text() != "":
            js_data = {"phone_number": self.login.text(), "password": self.password.text()}
            answer = requests.post(f"{protocol}://{ip}:{port}/api/login", json=js_data)
            js_data = answer.json()
            if bool(js_data['event']):
                self.token = js_data['token']


class Registration(QWidget, Reg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.register_brn.clicked.connect(self.re)

    def re(self):
        if self.auto_num.text() != "" and self.login.text != '' and self.full_name.text() != "":
            js_data = {
                "login": self.full_name.text(),
                "auto_number": self.auto_num.text(),
                "phone_number": self.login.text()
            }
            requests.post(f"{protocol}://{ip}:{port}/api/registration")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    App = MainApp()
    App.show()
    sys.exit(app.exec_())
