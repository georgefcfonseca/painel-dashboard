"""
Desenvolvido por George Fábio Fonseca
E-mail: georgefcfonseca@gmail.com
Data: 2022-01-22
Sempre: Faça, Fuce, Force
"""

import sys
import os
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Carregar URLs do arquivo
with open('urls.txt', 'r') as f:
    urls = [line.strip() for line in f.readlines()]

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Painel Gerencial')

        # Crie layouts verticais e horizontais
        vlayout1 = QVBoxLayout()
        vlayout2 = QVBoxLayout()
        hlayout = QHBoxLayout(self)

        # Crie visualizações da web com base no número real de URLs
        for i, url in enumerate(urls):
            view = QWebEngineView(self)
            view.load(QUrl(url))
            if i % 2 == 0:
                vlayout1.addWidget(view)
            else:
                vlayout2.addWidget(view)

        # Adicione os layouts verticais ao layout horizontal
        hlayout.addLayout(vlayout1)
        hlayout.addLayout(vlayout2)

        # Defina o modo de tela cheia
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
