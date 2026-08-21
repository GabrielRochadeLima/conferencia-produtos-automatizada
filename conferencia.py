# projeto para auxiliar na bipagem dos produtos e criar uma lista com os sku, ean
# e quantidade somadas e essa lista ser colocada no app de movimentacao da valenro

print("===Bem vindo ao sistema de conferencia===")
print("Escolha a opção desejada:")
print("1 - iniciar conferencia")
op=int(input("Digite a opção: "))
if op==1:
    print("iniciando conferencia...")
    ean_list=[]
    bipe = input("Bipe o ean do produto: ")
    ean_list.append(bipe)
    print("EAN adicionado com sucesso!")
    print("Deseja adicionar produtos em massa? (s/n)")
    resp = input("Resposta: ")
    if resp == "s":
           
        while True:
        
            bipe = input("Bipe o ean do produto ou digite \"fim\" para finalizar: ")
            if bipe == "fim":
                print("Lista de produtos finalizada com sucesso!")
                break
            ean_list.append(bipe)

            print("EAN adicionado com sucesso!")

        print(ean_list)
            

