# projeto para auxiliar na bipagem dos produtos e criar uma lista com os sku, ean
# e quantidade somadas e essa lista ser colocada no app de movimentacao da valenro
def gerar_numero_conferencia():
    try:
        with open("numero_conferencia.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        if linhas:
            numero=int(linhas[-1].strip()) + 1
        else:
            numero = 1
    except FileNotFoundError:
        numero = 1

    with open("numero_conferencia.txt", "a") as arquivo:
        arquivo.write(f"{numero}\n")

    return numero

def salvar_conferencia(produtos, numero_conferencia):
    with open(f"conferencias.txt", "a") as arquivo:
        arquivo.write("\n")
        arquivo.write("=" * 40 + "\n")
        arquivo.write(f"CONFERÊNCIA: {numero_conferencia:04d}\n")
        arquivo.write("=" * 40 + "\n")
        for ean, quantidade in produtos.items():
            arquivo.write(f"{ean},{quantidade}\n")

def listar_conferencias():
    try:
        with open("conferencias.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        conferencias = []

        for linha in linhas:
            if linha.startswith("CONFERÊNCIA:"):
                numero_conferencia = int(linha.split(":")[1].strip())
                conferencias.append(numero_conferencia)
        return conferencias
    
    except FileNotFoundError:
        print("Nenhuma conferência encontrada.")

    return conferencias

print("===Bem vindo ao sistema de conferencia===")
print("Escolha a opção desejada:")
print("1 - iniciar conferencia")
print("2 - Consultar conferencia")
op=int(input("Digite a opção: "))

if op==1:
    numero_conferencias = gerar_numero_conferencia()
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
            print("Produto adicionado com sucesso!")

        print(f"\n=== CONFERÊNCIA {numero_conferencias:04d} ===")
        for ean, quantidade in produtos.items():
            print(f"EAN: {ean}, Quantidade: {quantidade}")
        salvar_conferencia(produtos, numero_conferencias)
        print(f"Conferência {numero_conferencias:04d} salva com sucesso!")

elif op == 2:

    print("\n=== CONSULTAR CONFERÊNCIA ===")

    conferencias = listar_conferencias()

    if not conferencias:
        print("Nenhuma conferência encontrada.")

    else:
        print("\nConferências disponíveis:")

        for conferencia in conferencias:
            print(f"Conferência: {conferencia:04d}")

        numero_consulta = input("\nDigite o número da conferência que deseja consultar: ")