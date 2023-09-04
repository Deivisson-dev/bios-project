'''
Neste arquivo são definidas 
'''
# imports
import os
import sys
import platform
import psutil

from datetime import date
from pynput import keyboard
from colored import fore, back, style
from colored import style

from advanced import get_usar_senha
from advanced import set_usar_senha

from boot import get_disp1
from boot import get_disp2
from boot import get_disp3
from boot import save_boot


menu_ativo = 0
enter = 0
item_tela  = 0


disp1 = get_disp1()
disp2 = get_disp2()
disp3 = get_disp3()


color: str = f"{fore('black')}{back('cyan')}"
color_ativo: str = f"{fore('red')}{back('black')}"
color_inativo: str = f"{fore('light_gray')}{back('blue')}"
color_selecionado: str = f"{fore('blue')}{back('light_gray')}"
color_editavel: str = f"{fore('white')}{back('black')}"
color_movendo: str = f"{fore('blue')}{back('black')}"	
color_tela: str = f"{fore('black')}{back('light_gray')}"



def limpar_tela() :
	os.system("cls")

def end():
	print("\033[0m")

def atualizar() :
	limpar_tela()
	tela()
	end()

def titulo() :
	print(color + "Projeto BIOS".center(80))


def menu() :
	print(f"{color_inativo}{''.ljust(80)}")
	main_menu()
	advanced_menu()
	boot_menu()
	exit_menu()

def main_menu() :
	main_string = " Main ".center(12)
	cursor = "\033[2;2H"
	if (menu_ativo == 0) :
		print(f"{cursor}{color_selecionado}{main_string}", end="")
	if (menu_ativo != 0) :
		print(f"{cursor}{color_inativo}{main_string}", end="")

def advanced_menu() :
	advanced_string = " Advanced ".center(12)
	cursor = "\033[2;12H"
	if (menu_ativo == 1) :
		print(f"{cursor}{color_selecionado}{advanced_string}", end="")
	if (menu_ativo != 1) :
		print(f"{cursor}{color_inativo}{advanced_string}", end="")

def boot_menu():
	boot_string = "Boot".center(12)
	cursor = "\033[2;22H"
	if (menu_ativo == 2) :
		print(f"{cursor}{color_selecionado}{boot_string}", end="")
	if (menu_ativo != 2) :
		print(f"{cursor}{color_inativo}{boot_string}", end="")

def exit_menu() :
	exit_string = "Exit".center(12)
	cursor = "\033[2;32H"
	if (menu_ativo == 3) :
		print(f"{cursor}{color_selecionado}{exit_string}")
	if (menu_ativo != 3) :
		print(f"{cursor}{color_inativo}{exit_string}")

def rodape() :
	cursor = "\033[22;0H"
	texto_enter_setas = 'Enter: Selecionar menu   \u2191\u2193 (setas): Navegar valores   \u2190\u2192 (setas): Navegar menus'
	texto_mais = "+ -: Alterar valores   q: Sair"
	print(f"{cursor}{color}{texto_enter_setas.ljust(80)}")
	cursor = "\033[23;0H"
	print(f"{cursor}{color}{texto_mais.ljust(80)}")


def tela() :
	global menu_ativo
	titulo()
	menu()
	if (menu_ativo == 0):
		main_tela()
	if (menu_ativo == 1):
		advanced_tela()
	if (menu_ativo == 2):
		boot_tela()
	if (menu_ativo == 3):
		mexit_tela()
	rodape()


def main_tela() :
	for i in range(1,21) :
		print(f"{color_tela}{''.ljust(80)}")
	cursor = "\033[5;5H"
	data_atual = date.today()
	data_formatada = data_atual.strftime('%d/%m/%Y')
	print(f"{cursor}{color_tela} Data: {data_formatada}")
	cursor = "\033[8;0H"
	print(f"{cursor} Computer network name: {color_tela}{platform.node()}")
	cursor = "\033[9;0H"
	print(f"{cursor} Machine type: {color_tela}{platform.machine()}")
	cursor = "\033[10;0H"
	print(f"{cursor} Processor type: {color_tela}{platform.processor()}")
	cursor = "\033[11;0H"
	print(f"{cursor} Platform type: {color_tela}{platform.platform()}")
	cursor = "\033[12;0H"
	print(f"{cursor} Operating system: {color_tela}{platform.system()}")
	cursor = "\033[13;0H"
	print(f"{cursor} Operating system release: {color_tela}{platform.release()}")
	cursor = "\033[14;0H"
	print(f"{cursor} Operating system version: {color_tela}{platform.version()}")
	cursor = "\033[15;0H"
	memoria = psutil.virtual_memory()
	memoria_total = round(memoria.total/(1024*1024*1024), 2)
	print(f"{cursor} Memória RAM instalada: {color_tela}{memoria_total} GB")


def advanced_tela() :
	senha = get_usar_senha()
	for i in range(1,21) :
		print(f"{color_tela}{''.ljust(80)}")
	cursor = "\033[8;0H"
	if (enter != 1) :
		if (senha == True):
			print(f"{cursor}{color_tela}Usar senha: {color_ativo}Off")
			cursor = "\033[9;0H"
			print(f"{cursor}{color_tela}Senha: {color_editavel}{'    '}")
		if (senha == False):
			print(f"{cursor}{color_tela}Usar senha: {color_ativo}On")
			cursor = "\033[9;0H"
			print(f"{cursor}{color_tela}Senha: {color_editavel}1234")
	if (enter == 1):
		if (item_tela == 0):
			if (senha == True):
				print(f"{cursor}{color_tela}Usar senha: {color_ativo}Off")
				cursor = "\033[9;0H"
				print(f"{cursor}{color_tela}Senha: {color_editavel}{'    '}")
			if (senha == False):
				print(f"{cursor}{color_tela}Usar senha: {color_ativo}On")
				cursor = "\033[9;0H"
				print(f"{cursor}{color_tela}Senha: {color_editavel}1234")
		if (item_tela == 1):
			if (senha == True):
				print(f"{cursor}{color_tela}Usar senha: {color_ativo}Off")
				cursor = "\033[9;0H"
				print(f"{cursor}{color_tela}Senha: {color_movendo}{'    '}")
			if (senha == False):
				print(f"{cursor}{color_tela}Usar senha: {color_ativo}On")
				cursor = "\033[9;0H"
				print(f"{cursor}{color_tela}Senha: {color_movendo}1234")


def boot_tela() :
	global disp1
	global disp2
	global disp3
	for i in range(1,21) :
		print(f"{color_tela}{''.ljust(80)}")
	cursor = "\033[8;0H"
	if (enter != 2) :
		print(f"{cursor}{color_tela}1º dispositivo de boot: {color_editavel}{disp1}")
		cursor = "\033[9;0H"
		print(f"{cursor}{color_tela}2º dispositivo de boot: {color_editavel}{disp2}")
		cursor = "\033[10;0H"
		print(f"{cursor}{color_tela}3º dispositivo de boot: {color_editavel}{disp3}")
		cursor = "\033[11;0H"
	if (enter == 2):
		if (item_tela == 0):
			print(f"{cursor}{color_tela}1º dispositivo de boot: {color_movendo}{disp1}")
			cursor = "\033[9;0H"
			print(f"{cursor}{color_tela}2º dispositivo de boot: {color_editavel}{disp2}")
			cursor = "\033[10;0H"
			print(f"{cursor}{color_tela}3º dispositivo de boot: {color_editavel}{disp3}")
			cursor = "\033[11;0H"
		if (item_tela == 1):
			print(f"{cursor}{color_tela}1º dispositivo de boot: {color_editavel}{disp1}")
			cursor = "\033[9;0H"
			print(f"{cursor}{color_tela}2º dispositivo de boot: {color_movendo}{disp2}")
			cursor = "\033[10;0H"
			print(f"{cursor}{color_tela}3º dispositivo de boot: {color_editavel}{disp3}")
			cursor = "\033[11;0H"
		if (item_tela == 2):
			print(f"{cursor}{color_tela}1º dispositivo de boot: {color_editavel}{disp1}")
			cursor = "\033[9;0H"
			print(f"{cursor}{color_tela}2º dispositivo de boot: {color_editavel}{disp2}")
			cursor = "\033[10;0H"
			print(f"{cursor}{color_tela}3º dispositivo de boot: {color_movendo}{disp3}")
			cursor = "\033[11;0H"


def mexit_tela() :
	for i in range(1,21) :
		print(f"{color_tela}{''.ljust(80)}")
	cursor = "\033[8;0H"
	print(f"{cursor}{color_tela}Pressione ENTER para sair!")


def on_press(key):
	global menu_ativo
	global enter
	global item_tela
	global disp1
	global disp2
	global disp3

	try:
		if (key.char == 'q')  or (key.char == 'Q'):
			exit()
		if (key.char == '-') :
			if (enter == 1):
				set_usar_senha("1234")
			if (enter == 2):
				if (item_tela == 0):
					disp1, disp3 = disp3, disp1
				if (item_tela == 1):
					disp2, disp1 = disp1, disp2
				if (item_tela == 2):
					disp3, disp2 = disp2, disp3
				save_boot(disp1, disp2, disp3)
		if (key.char == '+') :
			if (enter == 1):
				set_usar_senha("")
			if (enter == 2):
				if (item_tela == 0):
					disp1, disp2 = disp2, disp1
				elif (item_tela == 1):
					disp2, disp3 = disp3, disp2
				elif (item_tela == 2):
					disp3, disp1 = disp1, disp3
				save_boot(disp1, disp2, disp3)
		else :
			pass
	except AttributeError:
		mod = 1
		if (enter == 0) :
			mod = 1	
		elif (enter == 1) :
			mod = 2
		elif (enter == 2) :
			mod = 3	

		if (key == keyboard.Key.up) : 
			if (mod < 3):
				item_tela = (item_tela - 1) % 2
			if (mod == 3):
				item_tela = (item_tela - 1) % 3
		if (key == keyboard.Key.down) :
			if (mod < 3):
				item_tela = (item_tela + 1) % 2
			if (mod == 3):
				item_tela = (item_tela + 1) % 3
		if (key == keyboard.Key.left) :
			menu_ativo = (menu_ativo - 1) % 4
		if (key == keyboard.Key.right) :
			menu_ativo = (menu_ativo + 1) % 4
		if (menu_ativo == 3) and (key == keyboard.Key.enter) :
			exit()
		if (key == keyboard.Key.enter) :
			enter     = menu_ativo
			item_tela = 0

			if (menu_ativo == 2) :
				save_boot(disp1, disp2, disp3)
			
	atualizar()

def on_release(key):
	if key == keyboard.Key.esc:
		return False



try:
	limpar_tela()
	tela()
	end()

	# Collect events until released
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()
except:
	limpar_tela()
	print("BIOS finalizada")