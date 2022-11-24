from design import *
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.botaoEscolheArquivo.clicked.connect(self.escolher_imagem)

    def escolher_imagem(self):
        imagem, _ = QFileDialog.getSaveFileName(self.centralwidget, 'Escolher Imagem',
                                                'C:\\Users\\rozas\\OneDrive\\Imagens\\',
                                                options=QFileDialog.DontUseNativeDialog)
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
