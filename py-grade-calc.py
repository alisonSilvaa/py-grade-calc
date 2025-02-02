import sys 
from PyQt5.QtWidgets import QLineEdit,QLabel,QWidget,QApplication,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtGui import QFont

# GERENCIAMENTO E CONEXÃO DO USUARIO COM SO

app = QApplication(sys.argv)
 
# CRIAÇÃO JANELA
janela = QWidget()
janela.setWindowTitle("teste")
janela.resize(1280,720)

# CRIAÇÃO DO LAYOUT
layout = QVBoxLayout()


# INPUT DO PYQT5

input = QLineEdit(janela)
input.setWindowTitle("Comando")
input.setFont(QFont("Arial",20))

'''
# CRIAÇÃO DO BOTÃO
botao = QPushButton("Clique Aqui",janela)
botao.setFont(QFont("Arial",20))
'''

# TEXTO CRIADO
resultado = QLabel("Digite 4 notas para calcular a média.",janela)
resultado.setFont(QFont("Arial",20))

titulo_programa = QLabel("Calculador de média")
titulo_programa.setFont(QFont("Arial",40))

#ORGANIZAÇÃO DO LAYOUT

layout.addWidget(titulo_programa)
layout.addWidget(resultado)
#layout.addWidget(botao)
layout.addWidget(input)

#FUNÇÃO

nota = []

def texto():

    text = input.text()
    input.clear()
   
    try:

        numero = int(text)
        if 0 <= numero <= 10: 
            nota.append(numero)
            resultado.setText(f"Notas registradas {len(nota)}/4")
        else: 
            resultado.setText("Erro! Digite um numero de 0 a 10")
    
        print(nota)

        if len(nota) == 4: 
            media = sum(nota)/4
            resultado.setText(f"A média do aluno: {media}")
            nota.clear()

    except ValueError: 
        resultado.setText("Erro! Digite numeros inteiros")

#CLIQUE DA FUNÇÃO

input.returnPressed.connect(texto)

#CONEXÃO GERAIS QUE FAZEM FUCIONA O SISTEMA DE JANELA E ETC.
janela.setLayout(layout)
janela.show() 
sys.exit(app.exec_())





