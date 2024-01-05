#Início: Importar biblioteca
from tkinter import *
from tkinter import ttk
import os

texto2 = None



def janela2():
    global texto2
    aba2 = Toplevel()
    aba2.title('Bloco de notas')
    aba2.geometry('860x670')
    aba2.resizable(width=False, height=False)


    def fechar_janela2():
        aba2.destroy()
    botão_sair2 = Button(aba2,text='Sair', width=7, height=1, highlightbackground='black', command=fechar_janela2)
    botão_sair2.place(x=703, y=0)
    
    texto2 = Text(aba2, wrap=WORD, width=87, height=30, highlightbackground='black', bd=4)
    texto2.place(x=79, y=40)

    salvar2 = Button(aba2, text='Salvar', width=7, height=1, highlightbackground='black',command=botao_salvar2)
    salvar2.place(x=615, y=0)


def botao_salvar2():
    if texto2:
        conteudo = texto2.get("1.0", END+ '-1c')
        caminho = "/home/sadak/códigos"
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        caminho_arquivo = os.path.join(caminho, "arquivo_salvo.txt")
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(conteudo)
    else:
        print('erro....')    



def botao_salvar():
    conteudo = texto.get("1.0","end-1c")
    caminho = "/home/sadak/códigos"
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    caminho_arquivo = os.path.join(caminho, "arquivo_salvo2.txt")
    with open(caminho_arquivo,'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

        



janela = Tk()

janela.geometry('860x670')
janela.resizable(width=False, height=False)
janela.title('Bloco de notas')

#Agora que criamos a janela básica, façamos uma para colocar o nosso texto
texto = Text(janela, wrap=WORD, width=87, height=30, highlightbackground='black', bd=4)
texto.place(x=79, y=40)
texto.tag_configure('center', justify='center')

#Fazer botão  de sair
sair = Button(janela, text='Sair' ,width=7, height=1, highlightbackground='black', overrelief=RIDGE,command=exit)
sair.place(x=703, y=0)

#Fazer botão de nova aba
nova_aba = Button(janela, text='Nova Janela', width=7, height=1, highlightbackground='black', overrelief=RIDGE, command=janela2)
nova_aba.place(x=528, y=0)

#Fazer Botão salvar
salvar = Button(janela, text='Salvar', width=7, height=1, highlightbackground='black', overrelief=RIDGE, command=botao_salvar)
salvar.place(x=615, y=0)



janela.mainloop()
