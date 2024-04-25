from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QGridLayout, QWidget, QPushButton, \
    QMessageBox
from gerar import gerar_senha


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Senhas")
        self.setGeometry(500, 500, 500, 500)
        self.setStyleSheet("MainWindow {background-color: #A9A9A9;}")

        self.label_tamanho_da_senha = QLabel(self)
        self.label_tamanho_da_senha.setText("Tamanho da Senha")
        self.label_senha_gerada = QLabel(self)
        self.label_senha_gerada.setText("Senha Gerada: ")

        self.input_tamanho_da_senha = QLineEdit(self)
        self.input_tamanho_da_senha.setPlaceholderText("Digite o tamanho da senha")

        self.button_gerar_senha = QPushButton(self)
        self.button_gerar_senha.setText("Gerar Senha")
        self.button_gerar_senha.clicked.connect(self.gerar_senha)

        layout = QGridLayout(self)
        layout.addWidget(self.label_tamanho_da_senha, 0, 0)
        layout.addWidget(self.input_tamanho_da_senha, 0, 1)
        layout.addWidget(self.button_gerar_senha, 1, 0, 1, 2)
        layout.addWidget(self.label_senha_gerada, 2, 0, 1, 2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def gerar_senha(self):
        try:
            self.label_senha_gerada.setText(f"Senha Gerada: {gerar_senha(int(self.input_tamanho_da_senha.text()))}")
        except TypeError:
            QMessageBox.warning(self, "Erro", "Digite apenas números inteiros")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Digite apenas números inteiros")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
