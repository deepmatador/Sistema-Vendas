from View.Uses.frmAdmin import Ui_FrmAdmin  # Importar interface de admin
from PyQt5.QtWidgets import QMainWindow



class FrmAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FrmAdmin()
        self.ui.setupUi(self)
























class WindowManager:
    SecondWindow = None  # Armazena referência global para evitar fechamento automático

    @classmethod
    def open_admin(cls):
        if cls.SecondWindow is None or not cls.SecondWindow.isVisible():
            cls.SecondWindow = FrmAdmin()
            cls.SecondWindow.show()

