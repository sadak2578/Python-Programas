from tkinter import *
from time import sleep

def resposta():
    usuário = nome.get()
    label.config(text=f"Seja bem vindo, {usuário}!")
    botão_avançar.place_forget()
    nome.place_forget()
    botão_sair.place(x=150, y=80)

def sair():
    
    janela.destroy
    sleep(1)
    exit()

janela = Tk()
janela.geometry('410x340')
janela.resizable(width=False, height=False)
janela.title('Bem vindo')

#Mostrar menssagem na tela
label = Label(text='Bem vindo, insira seu nome abaixo:', font=('Ivy 10'))
label.pack()

#Mostrar a janela para colocar o nome
nome = Entry(janela,bd=5)

nome.pack(pady=12)

#Criar o botão
botão_avançar = Button(text='Avançar', width=9, height=3, command=resposta,highlightbackground='black',bd=4,relief=RAISED, overrelief=RIDGE)
botão_avançar.place(x=150, y=80)

#Criar botão de sair
botão_sair = Button(text='Quit', width=9, height=3, command=sair ,highlightbackground='black',bd=4,relief=RAISED, overrelief=RIDGE)
botão_sair.place_forget()





janela.mainloop()
