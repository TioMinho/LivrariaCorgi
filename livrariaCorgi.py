# Bibliotecas
import time
import os

# -----------

# Programa Principal
if __name__=="__main__":
	# Parte 1: Carregando os status atuais da loja (ou status iniciais)
	print("\nBem-vindo ao sistema Livraria Corgi!")
	print("Resgatando os status da livraria...")

	# Carregar os status do arquivo statusLoja.py #

	time.sleep(1)

	# Parte 2: Menu Principal de Comandos
	while 1:
		os.system("reset")
		print("####################################################")
		print("###############    Livraria Corgi    ###############")
		print("####################################################")
		print("")
		print("Menu de Opções")
		print("\t1. Vender Produto")
		print("\t2. Consultar Database")
		print("\t3. Adicionar Produtos")
		print("\t4. Repor Estoque")
		print("\t5. Status da Loja")
		print("\t6. Logs")
		print("\t7. Sair")
		print("")

		comando = eval(input("Comando: "))

		# Opção: Vender Produto
		if(comando == 1):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

		# Opção: Consultar Database
		elif(comando == 2):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

		# Opção: Adicionar Produtos
		elif(comando == 3):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

		# Opção: Repor Estoque
		elif(comando == 4):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

		# Opção: Status da Loja
		elif(comando == 5):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

		# Opção: Logs
		elif(comando == 6):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

		# Opção: Sair
		elif(comando == 7):
			confirm = input("Você tem certeza que deseja sair? (S - Sim | N - Não): ")
			confirm = confirm.lower()

			while(confirm != "s" and confirm != "n"):
				confirm = input("Opção inválida! (S - Sim | N - Não): ")

			if(confirm == "s"):
				print("")
				print("Até logo! :)")
				print("Atualizando statusLoja.txt ...")

				time.sleep(2)	
				os.system("reset")

				break;


# ------------------