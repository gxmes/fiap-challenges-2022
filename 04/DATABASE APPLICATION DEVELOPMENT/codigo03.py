import re


class Cliente:
    dados = {"nome": str, "cpf": str, "conta": str, "produtos": list}

    # Economia de memória
    __slots__ = tuple(dados.keys())

    def validar_cpf(self):
        padrao_cpf = re.compile(r"^([0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2})$")
        if not padrao_cpf.match(self.cpf):
            raise ValueError("CPF inválido")

    def __init__(self, nome, cpf, conta, produtos):
        self.nome = nome
        self.cpf = cpf
        self.validar_cpf()
        self.conta = conta
        self.produtos = produtos

        # Checar tipos de dados
        for chave, tipo in self.dados.items():
            if type(getattr(self, chave)) != tipo:
                raise TypeError(f"{chave} deve ser {tipo}")

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def __str__(self):
        return f"{self.nome} - {self.cpf} - {self.conta} - {self.produtos}"


print(
    Cliente(
        "João", "123.456.789-00", "123456789", ["Produto 1", "Produto 2", "Produto 3"]
    )
)
