from os import system
from time import sleep

sleep(1)
print('''
===================================================
		    Ping teste
===================================================
opções de ping:
[1] - desktop
[2] - notebook
[3] - ip de impressora
[4] - Sair
''')


def ping_desktop(nome_maquina='', num_ip='',qtd_bytes_str='', qdt_bytes_int=0, num_buffer_str='', num_buffer_int=0):
	sleep(1)
	nome_maquina = input('Digite o nome do desktop: ')
	sleep(1)
	num_ip = input('Digite o número do ip: ')
	sleep(1)
	qtd_bytes_str = input('Digite a quantidade de Bytes: ')
	qdt_bytes_int = int(qtd_bytes_str)
	sleep(1)
	num_buffer_str = input('Especifique o número de Buffer: [32,64,128,...]: ')
	num_buffer_int = int(num_buffer_str)
	sleep(1)
	print(f'Máquina sendo pingada: {nome_maquina}')
	sleep(1)
	system(f'ping -a -n {qdt_bytes_int} -l {num_buffer_int} {num_ip}')

def finalizacao():
	opcao_finalizacao = input('Deseja realizar outros testes ou o mesmo teste novamente?: [S/N] ').strip().upper()[0]
	if opcao_finalizacao == 's' or opcao_finalizacao == 'S':
		print('''
		opções de ping:
		[1] - desktop
		[2] - notebook
		[3] - ip de impressora
		[4] - Sair
		''')

	else:
		sleep(1.9)
		print('saindo...')
		sleep(1.9)
		print('Obrigado por usar o programa...')
		sleep(2)
		print('Creditos do desenvolvedor: sadak2578 -> usuário no git hub')
		sleep(2)
		system(exit())

def ping_notebook(nome_note='', num_ip_note='',qtd_bytes_str='',qdt_bytes_int=0, num_buffer_str='',num_buffer_int=0):
	sleep(1)
	nome_note = input('Digite o nome do notebook: ')
	sleep(1)
	num_ip_note = input('Digite o número do ip do notebook: ')
	sleep(1)
	qtd_bytes_str = input('Quantidade de bytes que serão rodados: ')
	qtd_bytes_int = int(qtd_bytes_str)
	sleep(1)
	num_buffer_str = input('Especifique o número de Buffer: [32,64,128,...]: ')
	num_buffer_int = int(num_buffer_str)
	sleep(1)
	print(f'máquina que está sendo pinganda: {nome_note}')
	sleep(1)
	system(f'ping -a -n {qtd_bytes_int} -l {num_buffer_int} {num_ip}')

def ip_impressora(nome_impressora='',num_ip_impressora='',qtd_bytes_str='',qtd_bytes_int=0,num_buffer_str='',num_buffer_int=0):
	sleep(1)
	nome_impressora = input('Digite o nome da impressora: ')
	sleep(1)
	num_ip_impressora = input('Digite o número de ip da impresora: ')
	sleep(1)
	qtd_bytes_str = input('Quantidade de bytes que serão enviados: ')
	qdt_bytes_int = int(qtd_bytes_str)
	sleep(1)
	num_buffer_str = input('Especifique o número de Buffer: [32,64,128,...] ')

#ping_desktop_func = ping_desktop(nome_maquina=, num_ip,qtd_bytes_str=, qdt_bytes_int=, num_buffer_str=, num_buffer_int=) => este não funcionou
while True:
	opcao_primaria = input('Digite sua opção: ')
	if opcao_primaria == '1':
		ping_desktop(nome_maquina='', num_ip='',qtd_bytes_str='', qdt_bytes_int=0, num_buffer_str='', num_buffer_int=0)
		finalizacao()
		continue
	elif opcao_primaria == '2':
		ping_notebook(nome_note='', num_ip_note='',qtd_bytes_str='',qdt_bytes_int=0, num_buffer_str='',num_buffer_int=0)
		finalizacao()
		continue

		
	elif opcao_primaria == '4':
		sleep(1.5)
		print('saindo...')
		sleep(1.5)
		print('Obrigado por usar o programa...')
		sleep(2)
		print('Creditos do desenvolvedor: sadak2578 -> usuário no git hub')
		sleep(1.5)
		system(exit())
		


# Esse daqui ainda n ficou muito legal, mas preciso adicionar os administradores, para mexer com o programa, mais por segurança mesmo
# além disso vou colocar para ele pedir usuário e senha admin as opções de configuração, e separar melhor as opções de ping possíveis.
# colocar tbm as opções ty e except, para validação tanto de usuário administrador quanto das opções de ping e das opções de if/else/elif.
