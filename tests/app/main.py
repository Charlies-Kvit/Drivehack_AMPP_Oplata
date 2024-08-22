import sys
from interfaces.main import Ui_MainWindow as Main
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainApp(QMainWindow, Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.send.clicked.connect()

    """def get_event(self):
        auto_number"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    App = MainApp()
    App.show()
    sys.exit(app.exec_())
