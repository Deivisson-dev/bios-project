'''
Neste arquivo devem ser implementadas funcoes para facilitar a execução
de ações necessarias no bios.py
'''
def get_disp1() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na primeira linha, sem o caractere especial \n
	Exemplo de retorno 'SSD/HDD'
	'''
	with open("boot.txt", "r") as arquivo:
		disp1 = arquivo.readline()
		disp1 = disp1.replace("\n", "")
	return disp1
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp1
	# fora da instrução with, retorne o conteúdo da variável 'disp1'

def get_disp2() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na segunda linha, sem o caractere especial \n
	Exemplo de retorno 'DVD-ROM'
	'''
	with open("boot.txt", "r") as arquivo:
		arquivo.readline()
		disp2 = arquivo.readline()
		disp2 = disp2.replace("\n", "")
	return disp2 
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# essa linha será ignorada
		# leia a segunda linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp2
	# fora da instrução with, retorne o conteúdo da variável 'disp2'


def get_disp3() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na terceira linha, sem o caractere especial \n
	Exemplo de retorno 'LAN'
	'''
	with open("boot.txt", "r") as arquivo:
		arquivo.readline()
		arquivo.readline()
		disp3 = arquivo.readline()
		disp3 = disp3.replace("\n", "")
	return disp3
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# essa linha será ignorada
		# leia a segunda linha do arquivo
		# essa linha será ignorada
		# leia a terceira linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp2
	# fora da instrução with, retorne o conteúdo da variável 'disp2'


def save_boot(disp1, disp2, disp3) :
	'''
	Essa função deve abrir o arquivo boot.txt e criar a lista de 
	dispositivos de boot, um por linha
	Exemplo de conteúdo do arquivos após a execução

	SSD/HDD
	DVD-ROM
	LAN
	'''
	with open("boot.txt", "w") as arquivo:
		arquivo.write(disp1 + "\n")
		arquivo.write(disp2 + "\n")
		arquivo.write(disp3 + "\n")
	# abra o arquivo "boot.txt" para escrita
	# dica: utilize a instrução with
		# dentro do bloco with escreva uma linha com disp1 e \n
		# escreva uma linha com disp2 e \n
		# escreva uma linha com disp3 e \n
