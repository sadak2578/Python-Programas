from tkinter import *
from time import sleep
def ação_janela_numero():
    try:
        numero = int(janela_numero.get())
        label.config(text=f'você escolheu o número: {numero}')
        botão1.place_forget()
        botão3.place_forget()
        janela_numero.place_forget()
        botão2.place(x=130, y=60)
        
    except ValueError:
        label.config(text='Porfavor insira um número verdadeiro')

def créditos():
    label.config(text='Todos os créditos vão para Sadak_who')
    label.place(x=20,y=0)
    label.update()
    botão3.place_forget()
    botão1.place_forget()
    janela_numero.destroy()
    sleep(5)
    exit()

    

def sair():
    
    label.config(text='Saindo....')
    label.place(x=130,y=0)
    label.update()
    
    sleep(1)
    
    janela_numero.destroy()
 
    exit()



janela = Tk()

janela.geometry("340x210")
janela.resizable(width=False, height=False)

label = Label(text='Entre com seu número:', font=('Arial 12'))
label.place(x=80, y=0)

janela_numero = Entry(janela, highlightbackground='black', bd=4)
janela_numero.place(x=80,y=20)

botão1 = Button(text='continuar', width=5, height=2, highlightbackground='black', bd=2,command=ação_janela_numero)
botão1.place(x=80,y=60)



botão2 = Button(text='Sair', width=5, height=2, highlightbackground='black',bd=2, command=sair)
botão2.place_forget()

botão3 = Button(text='Créditos',  width=5, height=2, highlightbackground='black',bd=2, command=créditos )
botão3.place(x=160, y=60)

janela.mainloop()
