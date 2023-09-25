"""
Desenvolvido por George Fábio Fonseca
E-mail: georgefcfonseca@gmail.com
Data: 2022-01-22
Sempre: Faça, Fuce, Force
"""

# Importando as bibliotecas necessárias
import sys
import csv
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Definindo o caminho para o arquivo CSV que contém as URLs e configurações
CSV_PATH = 'urls.csv'

# Função para carregar as URLs e configurações do arquivo CSV
def load_urls_from_csv():
    urls_zoom_refresh = []
    # Abre o arquivo CSV
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    # Filtra linhas que não começam com '#'
    valid_lines = [line for line in lines if not line.strip().startswith('#')]
    reader = csv.DictReader(valid_lines, delimiter=';')
    
    # Processa cada linha do arquivo CSV para obter URL, zoom e tempo de atualização
    for line in reader:
        url = line['URL']
        zoom = float(line['Zoom']) / 100.0
        refresh = int(line['Refresh'])
        urls_zoom_refresh.append((url, zoom, refresh))
    
    # Retorna a lista de URLs e configurações
    return urls_zoom_refresh

# Classe principal da aplicação
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # Função para carregar uma URL em uma view e configurar a atualização automática
    def loadViewUrl(self, view, url, refresh):
        view.load(QUrl(url))
        if refresh > 0:
            QTimer.singleShot(refresh * 1000, lambda: self.loadViewUrl(view, url, refresh))

    # Configuração da interface do usuário
    def initUI(self):
        self.setWindowTitle('Painel Gerencial')

        vlayout1 = QVBoxLayout()
        vlayout2 = QVBoxLayout()
        hlayout = QHBoxLayout(self)

        # Carrega cada URL em uma view
        for i, (url, zoom, refresh) in enumerate(load_urls_from_csv()):
            view = QWebEngineView(self)
            self.loadViewUrl(view, url, refresh)
            view.setZoomFactor(zoom)

            # Adiciona a view em um dos dois layouts verticais, alternando entre eles
            if i % 2 == 0:
                vlayout1.addWidget(view)
            else:
                vlayout2.addWidget(view)

        # Adiciona os layouts verticais ao layout horizontal
        hlayout.addLayout(vlayout1)
        hlayout.addLayout(vlayout2)

        # Exibe a aplicação em tela cheia
        self.showFullScreen()

    # Detecta quando a tecla F11 é pressionada para alternar entre tela cheia e modo normal
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()

# Ponto de entrada da aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

