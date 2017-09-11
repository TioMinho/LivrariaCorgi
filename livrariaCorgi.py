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
	file = open("statusLoja.txt", 'r')
	
	lucroT 		= int(file.readline())
	custoT 		= int(file.readline())
	receitaT 	= int(file.readline())
	qtdProdutos = int(file.readline())
	
	file.close()

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

			print("###############    Adicionar Produto    ###############")
			print("Código:", qtdProdutos + 1)

			titulo 		= input("Título: ")
			autor 		= input("Autor: ")
			descricao 	= input("Descrição: ")
			precoUni 	= input("Preço Unitário: ")
			estoqueMax 	= input("Máximo de Estoque: ")
			custoRepo 	= input("Custo de Reposição: ")

			confirm = input("Adicionar este produto no Banco de Dados? (S - Sim | N - Não): ")
			confirm = confirm.lower()
			
			if(confirm == 's'):
				qtdProdutos = qtdProdutos + 1

				nomeArquivo = 'database/' + str(qtdProdutos)
				file = open(nomeArquivo, 'w')
				
				file.write(str(qtdProdutos) + '\n')
				file.write(titulo + '\n')		
				file.write(autor + '\n')
				file.write(descricao + '\n')
				file.write(precoUni + '\n')
				file.write(estoqueMax + '\n')
				file.write(custoRepo + '\n')
				file.write('0' + '\n')
				
				file.close()


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

				file = open("statusLoja.txt", "w")
				file.write(str(lucroT) + '\n')
				file.write(str(custoT) + '\n')
				file.write(str(receitaT) + '\n')
				file.write(str(qtdProdutos) + '\n')
				file.close()

				time.sleep(2)	
				os.system("reset")

				break;


# ------------------