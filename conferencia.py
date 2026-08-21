# projeto para auxiliar na bipagem dos produtos e criar uma lista com os sku, ean
# e quantidade somadas e essa lista ser colocada no app de movimentacao da valenro

print("===Bem vindo ao sistema de conferencia===")
print("Escolha a opção desejada:")
print("1 - iniciar conferencia")
op=int(input("Digite a opção: "))
if op==1:
    print("iniciando conferencia...")
    ean_list=[]
    ean = input("Bipe o ean do produto: ")
    ean_list.append(ean)
    print("EAN adicionado com sucesso!")
    print("Deseja adicionar produtos em massa? (s/n)")
    resp = input("Resposta: ")
    if resp == "s":

        produtos={}

        while True:
        
            ean = input("Bipe o ean do produto ou digite \"fim\" para finalizar: ")

            if ean == "fim": #verifica se o usuário digitou "fim" para encerrar a entrada de produtos
                print("Lista de produtos finalizada com sucesso!")
                break

            if ean in produtos:
                produtos[ean] += 1 #incrementa a quantidade do produto existente
            else:
                produtos[ean] = 1 #adiciona o produto com quantidade 1
            print("EAN adicionado com sucesso!")

        print("Resultado da conferência:")
        for ean, quantidade in produtos.items():
            print(f"EAN: {ean}, Quantidade: {quantidade}")

            

