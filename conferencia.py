# projeto para auxiliar na bipagem dos produtos e criar uma lista com os sku, ean
# e quantidade somadas e essa lista ser colocada no app de movimentacao da valenro
def gerar_numero_conferencia():
    try:
        with open("numero_conferencia.txt", "r") as arquivo:
            numero = int(arquivo.read())
    except FileNotFoundError:
        numero = 1

    with open("numero_conferencia.txt", "w") as arquivo:
        arquivo.write(str(numero + 1))
    return numero
def salvar_conferencia(produtos, numero_conferencia):
    with open(f"conferencias.txt", "a") as arquivo:
        arquivo.write("\n")
        arquivo.write("=" * 40 + "\n")
        arquivo.write(f"CONFERÊNCIA: {numero_conferencia:04d}\n")
        arquivo.write("=" * 40 + "\n")
        for ean, quantidade in produtos.items():
            arquivo.write(f"{ean},{quantidade}\n")
        

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

        numero_conferencias = gerar_numero_conferencia()

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
            print("Produto adicionado com sucesso!")

        print(f"\n=== CONFERÊNCIA {numero_conferencias:04d} ===")
        for ean, quantidade in produtos.items():
            print(f"EAN: {ean}, Quantidade: {quantidade}")
        salvar_conferencia(produtos, numero_conferencias)
        print(f"Conferência {numero_conferencias:04d} salva com sucesso!")


    

            

