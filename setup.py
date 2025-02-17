import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.setWindowTitle("Minha Primeira Janela")
        self.setGeometry(100, 100, 400, 300)  # Posição x, y e tamanho largura x altura

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Cria a aplicação
    janela = MinhaJanela()  # Cria a instância da janela
    janela.show()  # Exibe a janela
    sys.exit(app.exec_())  # Executa o loop da aplicação
