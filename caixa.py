import sys
#importar os componentes para a construção da janela
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QTableWidget,QHBoxLayout, QVBoxLayout 
from PyQt5.QtGui import QPixmap 
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
        self.Label_coluna_esquerda.setStyleSheet("QLabel{background-color:#8b5e34; color:#fff; font-size: 20px}")
        #Label da direita 
        self.Label_coluna_direita = QLabel()
        self.Label_coluna_direita.setStyleSheet("QLabel{background-color:#fc0;}")

        #cRIAR O CONTEUDO DA COLUNA DA ESQUERDA
        self.V_Layout_esquerda = QVBoxLayout()

        #vAMOS CRIAR UMA LABEL PARA ADICIONAR O LOGO DA NOSSA LOJA 
        self.Logo_Label = QLabel()
        
        self.Logo_Label.setPixmap(QPixmap("C:/Users/nicoli.sbatista/Documents/janelaCaixa/.venv/logo.png"))
        #Ajuda a label e a imagem a ficar do tamanho ideal
        self.Logo_Label.setScaledContents(True)
        self.Logo_Label.setFixedHeight(80)
        self.Logo_Label.setFixedWidth(110)

        #Adicionar a label com imagem na tela 
        self.V_Layout_esquerda.addWidget(self.Logo_Label)



        #Vamos criar as labels e as linesEdits que ficarão na coluna da esquerda, dentro do
        #layout vertical da esquerda 
        self.Codigo_Produto_Label = QLabel("Código do produto: ")
        #self.Codigo_Produto_Label.setStyleSheet("QLabel{font-size:13px; color: grey}")
        self.Codigo_Produto_Edit = QLineEdit()
        self.V_Layout_esquerda.addWidget(self.Codigo_Produto_Label)
        self.V_Layout_esquerda.addWidget(self.Codigo_Produto_Edit)

        self.Nome_Produto_Label = QLabel("Nome do produto: ")
        self.Nome_Produto_Edit = QLineEdit()
        self.V_Layout_esquerda.addWidget(self.Nome_Produto_Label)
        self.V_Layout_esquerda.addWidget(self.Nome_Produto_Edit)


        self.Descricao_Produto_Label = QLabel("Descrição do produto: ")
        self.Descricao_Produto_Edit = QLineEdit()
        self.V_Layout_esquerda.addWidget(self.Descricao_Produto_Label)
        self.V_Layout_esquerda.addWidget(self.Descricao_Produto_Edit)


        
        self.Quantidade_Produto_Label = QLabel("Quantidade do produto: ")
        self.Quantidade_Produto_Edit = QLineEdit()
        self.V_Layout_esquerda.addWidget(self.Quantidade_Produto_Label)
        self.V_Layout_esquerda.addWidget(self.Quantidade_Produto_Edit)

        
        self.Preco_Produto_Label = QLabel("Preço unitário do produto: ")
        self.Preco_Produto_Edit = QLineEdit()
        self.V_Layout_esquerda.addWidget(self.Preco_Produto_Label)
        self.V_Layout_esquerda.addWidget(self.Preco_Produto_Edit)

        self.Subtotal_Produto_Label = QLabel("Sub total: ")
        self.Subtotal_Produto_Edit = QLineEdit()
        self.V_Layout_esquerda.addWidget(self.Subtotal_Produto_Label)
        self.V_Layout_esquerda.addWidget(self.Subtotal_Produto_Edit)

        #Adicionar o layout vertical da esquerda com todos os controles: Label e lineEdit
        #dentro da coluna da esquerda que é a label_coluna_esquerda
        self.Label_coluna_esquerda.setLayout(self.V_Layout_esquerda)


        #----------------------------------------------- CONTROLES: DIREITA ---------------------------------
        self.V_Layout_direita = QVBoxLayout()
        #CRIAR UMA TABELA E ADICIONAR A COLUNA DA DIREITA. ESSA TABELA TERÁ OS NOMES DOS CAMPOS 
        #QUE ESTARÃO AO LADO ESQUERDO
        Colunas = ["Cod.Produto", "Nome do produto", "Descrição", "Quantidade", "Preço unitário", "Subtotal"]
        self.Tabela =   QTableWidget()
        self.Tabela.setColumnCount(6)
        self.Tabela.setHorizontalHeaderLabels(Colunas)
        self.Tabela.setRowCount(10)
        self.V_Layout_direita.addWidget(self.Tabela)


        self.Total_Pagar_Label = QLabel("Total a pagar: ")
        self.Total_Pagar_Edit = QLineEdit("0,00")
        self.V_Layout_direita.addWidget(self.Total_Pagar_Label)
        self.V_Layout_direita.addWidget(self.Total_Pagar_Edit)

        self.Label_coluna_direita.setLayout(self.V_Layout_direita)



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
