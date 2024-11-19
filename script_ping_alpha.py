from os import system


while True:
    
    ip = input('Digite o endereço ip: ')
    system(f'ping -a -n 10 {ip}')
    
    
    opcao = input('Deseja continuar?:[s/n] ').strip().lower()[0]
    if opcao == 's' or opcao == 'S':
        continue
    elif opcao == 'n' or opcao == 'N':
        break
        
        
# código melhorado
# obs: instale o kali linux e teste este código nele, se possível fazer no windows tbm faça
# Obs2: tente colocar com o nmap tanto windows quanto kali linux

