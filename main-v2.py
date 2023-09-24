"""
Desenvolvido por George Fábio Fonseca
E-mail: georgefcfonseca@gmail.com
Data: 2023-09-22
Sempre: Faça, Fuce, Force
"""

import sys
import os
import csv
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Carregar URLs e valores de zoom do arquivo CSV
urls_zoom = []
with open('urls.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for line in reader:
        if line and line[0].startswith('http'):  # Processa apenas linhas que começam com "http"
            urls_zoom.append((line[0], float(line[1])))

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

        # Crie visualizações da web com base no número real de URLs e aplique zoom
        for i, (url, zoom) in enumerate(urls_zoom):
            view = QWebEngineView(self)
            view.load(QUrl(url))
            view.setZoomFactor(zoom)
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
