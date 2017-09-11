# Bibliotecas
import time
import os

# -----------

# Funções Auxiliares
def getProduto(codigo):
	nomeArquivo = "database/" + str(codigo)
	file = open(nomeArquivo, 'r')
	
	titulo 		= file.readline().rstrip()
	autor 		= file.readline().rstrip()
	descricao 	= file.readline().rstrip()
	preco 		= int(file.readline().rstrip())
	estoqueMax	= int(file.readline().rstrip())
	custoRepo	= int(file.readline().rstrip())
	estoque 	= int(file.readline().rstrip())

	file.close()

	return titulo, autor, descricao, preco, estoqueMax, custoRepo, estoque

def setProduto(codigo, titulo, autor, descricao, preco, estoqueMax, custoRepo, estoque):
	nomeArquivo = 'database/' + str(codigo)
	file = open(nomeArquivo, 'w')
	
	file.write(str(titulo) + '\n')		
	file.write(str(autor) + '\n')
	file.write(str(descricao) + '\n')
	file.write(str(precoUni) + '\n')
	file.write(str(estoqueMax) + '\n')
	file.write(str(custoRepo) + '\n')
	file.write(str(estoque) + '\n')
	
	file.close()

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

	# Parte 2: Menu Principal de Comandos
	while 1:
		time.sleep(2)
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

			print("###############    Vender Produto    ###############")
			codigo = input("Digite o código do produto: ")

			if(codigo > qtdProdutos): 
				print("Produto Inexistente!")
			else:
				titulo, autor, descricao, precoUni, estoqueMax, custoRepo, estoque = getProduto(codigo)

				print("Título:", titulo)
				print("Autor:", autor)
				print("Descrição:", descricao)
				print("Preço:", precoUni)
				print("Estoque:", estoque)

				if(estoque > 0):
					confirma = input("\nConfirmar compra? (S - Sim | N - Não: ")
					confirma = confirma.lower()

					if(confirma == 's'):
						receitaT = receitaT + precoUni
						lucroT = lucroT + precoUni
						estoque = estoque - 1

						setProduto(codigo, titulo, autor, descricao, precoUni, estoqueMax, custoRepo, estoque)
				else:
					print("Estoque indisponível para esse produto!")

		# Opção: Consultar Database
		elif(comando == 2):
			print("Aguarde...")
			time.sleep(1)	
			os.system("reset")

			codigo = 1
			while(codigo != 0 and qtdProdutos > 0):
				time.sleep(1)	
				os.system("clear")
				print("###############    Vender Produto    ###############\n")
				titulo, autor, descricao, precoUni, estoqueMax, custoRepo, estoque = getProduto(codigo)

				print("Codigo:\t", codigo)
				print("Título:\t", titulo)
				print("Autor:\t", autor)
				print("Descrição:\t", descricao)
				print("Preço:\t", precoUni)
				print("Estoque Máximo:\t", estoqueMax)
				print("Custo de Reposição:\t", custoRepo)
				print("Estoque:\t", estoque)

				acao = input("\n(A - Anterior | P - Próximo | C - Pesquisar por Código | S - Voltar ao Menu): ")
				acao = acao.lower()

				if(acao == 'a' and codigo > 1):
					codigo -= 1
				elif(acao == 'p' and codigo < qtdProdutos):
					codigo += 1
				elif(acao == 'c'):
					codigo = eval(input("Digite o Código para Pesquisar: "))
					
					if(codigo > qtdProdutos):
						print("Código Inválido!")
						codigo = 1

				elif(acao == 's'):
					print("Aguarde...")
					codigo = 0

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

			confirm = input("\nAdicionar este produto no Banco de Dados? (S - Sim | N - Não): ")
			confirm = confirm.lower()
			
			if(confirm == 's'):
				qtdProdutos = qtdProdutos + 1

				setProduto(qtdProdutos, titulo, autor, descricao, precoUni, estoqueMax, custoRepo, 0)

				print("O produto foi adicionado no Banco de Dados com sucesso!")

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