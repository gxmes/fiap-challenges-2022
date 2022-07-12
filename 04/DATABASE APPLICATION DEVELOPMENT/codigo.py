from codigo03 import Cliente


try:
    with open("produtos_e_pesos.txt", "r") as f:
        linhas = f.readlines()
except FileNotFoundError:
    print("Arquivo não encontrado")
    exit(1)


def media(lista, produtos):
    resultado = []
    for item in lista:
        resultado.append(produtos[item])
    return round(sum(resultado) / len(resultado), 3)

produtos = {}
# [1:] para remover o cabeçalho
for linha in linhas[1:]:
    produto, peso= linha.split(",")
    produtos[produto] = float(peso)

clientes = [
    Cliente(
        nome = "Antonio dos Santos",
        cpf = "239887202-00",
        conta = "3451 23845-7",
        produtos = ["Conta corrente", "Leasing", "Emprestimo consignado"]
    ),
    Cliente(
        nome = "Nevia Solomon",
        cpf = "838485346-21",
        conta = "3451 75773-7 ",
        produtos = ["Conta corrente", "Safrapay", "CDB Super"] 
    )
]

for cliente in clientes:
    print(
        f"{cliente.nome} | {cliente.cpf} | {cliente.conta} | {cliente.produtos} | {media(cliente.produtos, produtos)}"
    )