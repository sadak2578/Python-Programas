from tkinter import *
from tkinter import ttk

def janela1():
    janela2 = Toplevel()

    janela2.title('Janela Nova')
    janela2.geometry('680x540')
    janela2.resizable(width=False, height=False)
    
    texto2 = Text(janela2, wrap=WORD, width=60, height=20, highlightbackground='black', bd=2)
    texto2.place(x=80, y=60)
    janela2.update()
    

janela = Tk()
notebook = ttk.Notebook(janela)
notebook.place(x=60, y=60)
janela.geometry('680x540')
janela.resizable(width=False, height=False)
texto = Text(janela, wrap=WORD, width=60, height=20, highlightbackground='black', bd=2)
texto.place(x=80, y=60)


botao_adicionar = Button(janela, text='+', width=7, height=1, highlightbackground='black', bd=2, command=janela1)
botao_adicionar.place(x=80, y=10)



janela.mainloop()
