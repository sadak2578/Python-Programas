from tkinter import *

#faz a soma dos dois números
def somar():
    
    try:

        vnumero1 = int(numero1.get())
        vnumero2 = int(numero2.get())

        s = vnumero1 + vnumero2

        label.config(text=f'{vnumero1} + {vnumero2} = {s}')
    except ValueError:
        label.config(text='Insira os valores corretos')
    
#Reseta as janelas para colocar os números
def resetar():
    
    global  numero1, numero2, soma,label
    numero1.delete(0, END)
    numero2.delete(0, END)
    
    
   

    label = Label(text='Entre com o segundo número em baixo ',font=('Arial 12'))
    label.place(x=0, y=70)
    numero2 = Entry(janela, highlightbackground='black', bd=3, width= 6)
    numero2.place(x=0, y=100)

    #Criar o botão de soma
    soma =  Button(text='+', width=5, height=3, highlightbackground='black', bd=2,command=somar)
    soma.place(x=310, y=20)
    
#Sai do software
def sair():
    quit.destroy()
    exit()



#configura a janela
janela = Tk()
janela.resizable(width=False, height=False)
janela.geometry('600x500')

janela.title('Mini calculadora')

#Primeiro: Criar as janelas de entrada de números
label = Label(text='Entre com o primeiro número em baixo:', font=('Arial 12'))
label.place(x=0, y=0)
numero1 = Entry(janela, highlightbackground='black', bd=3,width=6)
numero1.place(x=0, y=30)

#Segundo: Criar a segunda janela:

label = Label(text='Entre com o segundo número em baixo ',font=('Arial 12'))
label.place(x=0, y=70)
numero2 = Entry(janela, highlightbackground='black', bd=3, width= 6)
numero2.place(x=0, y=100)

#Criar o botão de soma
soma =  Button(text='+', width=5, height=3, highlightbackground='black', bd=2,command=somar)
soma.place(x=310, y=20)


#Criar botão sair
quit = Button(text='Sair', width=5, height=3, highlightbackground='black', bd=2, command=sair)
quit.place(x=390,y=20)

#Botão continuar:

continuar = Button(text='Continuar', width=5, height=3, highlightbackground='black', bd=2, command=resetar)
continuar.place(x=470, y=20)


janela.mainloop()


#Código feito por sadak_who 25/12/23
