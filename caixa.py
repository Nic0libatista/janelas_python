import sys
#importar os componentes para a construção da janela
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTableView,QHBoxLayout, QVBoxLayout
#CONSTRUÇÃO DA CLASSE JANELA COM O NOME DE CAIXA 
class caixa(QWidget):
    #Criação do metodo __init__ que inicia a janela e exibe ela em tela
    def __init__(self):
        super().__init__()
        #Vamos definir a posição e o tamanho da tela
        self.setGeometry(0,30,1000,800)

        #vAMOS DEFINIR O TITULO DA NOSSA JANELA
        self.setWindowTitle("Caixa da loja")

        #Vamos criar as labels que representam as colunas esquerda e direita
        #Label da esquerda
        self.Label_coluna_esquerda = QLabel()
        self.Label_coluna_esquerda.setStyleSheet("QLabel{background-color:#0c0}")
        #Label da direita 
        self.Label_coluna_direita = QLabel()
        self.Label_coluna_direita.setStyleSheet("QLabel{background-color:#56d}")

        #Criar o layout horizontal para as colunas 
        self.H_Layout = QHBoxLayout()
        
        #Vamos adicionar as colunas
        #Esquerda e direita ao layout horizontal
        self.H_Layout.addWidget(self.Label_coluna_esquerda)
        self.H_Layout.addWidget(self.Label_coluna_direita)
        #Adicionar o layout na tela
        self.setLayout(self.H_Layout)

app = QApplication(sys.argv)
cx = caixa()
cx.show()
app.exec_()
