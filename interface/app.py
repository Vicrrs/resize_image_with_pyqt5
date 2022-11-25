from design import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.botaoEscolheArquivo.clicked.connect(self.escolher_imagem)
        self.botaoRedimensionar.clicked.connect(self.redimensionar)
        self.botaoSalvar.clicked.connect(self.salvar)

    def escolher_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Escolher Imagem',
                                                'C:\\Users\\rozas\\OneDrive\\Imagens\\',
                                                options=QFileDialog.DontUseNativeDialog)
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(self.centralwidget, 'Salvar Imagem',
                                                'C:\\Users\\rozas\\OneDrive\\Imagens\\',
                                                options=QFileDialog.DontUseNativeDialog)
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
