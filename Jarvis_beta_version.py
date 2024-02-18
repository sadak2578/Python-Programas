import pyaudio
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime


rec = sr.Recognizer()
maquina = pyttsx3.init()
wikipedia.set_lang('pt')

maquina.setProperty('voice','brazil')


maquina.say('Bem vindo, chefe')
maquina.runAndWait()

def encerrar():
   
    maquina.say("Desligando programa, volte sempre, chefe")
    maquina.runAndWait()
    exit()

def pergunta1():
    maquina.say('''
    Eu posso fazer diversas coisas chefe, desde responder perguntas selecionadas, até mesmo dizer a hora e dia.
    A algo que o senhor gostaria que eu fizesse, mestre?''')
    maquina.runAndWait()

def dia():
    

    dia_da_semana = datetime.datetime.now()
    hoje = dia_da_semana.weekday()
    dias_da_semana = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo']
    dia_de_hoje = dias_da_semana[hoje] 
    dia_do_mes = dia_da_semana.day
    return dia_de_hoje, dia_do_mes

def procurar():
     
    procurar = frase.replace('procure por', ' ')
    pesquisa = wikipedia.summary(procurar,sentences = 2)
    maquina.say(pesquisa)
    maquina.runAndWait()

while True:
    try:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic, duration=1)
            print("Fale algo: ")

            audio = rec.listen(mic)

            frase = rec.recognize_google(audio,language="pt-BR")

            print(f"você disse: {frase}")

            

        if 'Jarvis' in frase:
            frase = frase.replace('Jarvis', '')

            
            maquina.say('Olá chefe, eu sou jarvis, como posso te ajudar hoje?')
            maquina.runAndWait()
                
            
        elif 'encerrar' in frase:
            
            encerrar()
            
        elif 'fazer' in frase:
            
            pergunta1()
        elif 'dia' in frase:

            dia_de_hoje, dia_do_mes = dia()
            maquina.say(f'Hoje é {dia_de_hoje} dia {dia_do_mes}')
            maquina.runAndWait()
        elif 'procure por' in frase:
            procurar()
        elif 'obrigado' in frase:

            maquina.say('Disponha, chefe, qualquer coisa estou aqui')
            maquina.runAndWait()            

        else:
            maquina.say('Desculpe não entendi')
            maquina.runAndWait()


    except sr.UnknownValueError:

        print("Não entendi")
        exit()
    
