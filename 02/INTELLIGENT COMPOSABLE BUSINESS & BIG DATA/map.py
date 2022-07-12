# Parametro excluir define uma lista ou um caractere em especifico
# para excluir no processo de map.
def map(entrada, excluir=None):

    resultados = []

    for linha in entrada:

        # Remove varios espacos em branco deixando apenas um
        # no inicio e fim de cada palavra.
        linha.strip()

        # Exclui uma lista de caracteres ou apenas um caractere.
        if excluir:
            if type(excluir) == list:
                for item in excluir:
                    if item in linha:
                        linha = linha.replace(item, "")
            else:
                linha = linha.replace(excluir, "")

        # Separa as palavras e as armazena numa lista.
        palavras = linha.split()

        # Adiciona a palavra e 1 ao lado
        # o 1 servira para o acumulador
        # de reduce().
        for palavra in palavras:
            resultados.append("%s\t%s\n" % (palavra, 1))

    return resultados
