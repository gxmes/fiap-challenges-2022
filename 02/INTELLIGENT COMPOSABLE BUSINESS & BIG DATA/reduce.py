def reduce(entrada, sort=True):

    palavra_atual = None
    acumulador_atual = 0
    palavra = None
    resultados = []

    # Ordena as palavras para que economize tempo
    # de execucao.
    if sort:
        entrada.sort()

    for linha in entrada:
        palavra, acumulador = linha.split("\t", 1)

        try:
            acumulador = int(acumulador)
        except ValueError:
            print("Acumulador invalido.")
        # Caso a palavra atual seja a palavra da linha
        # o acumulador sera incrementado.
        if palavra_atual == palavra:
            acumulador_atual += acumulador
        else:
            # Caso a palavra da linha nao seja a palavra atual (da linha anterior)
            # sera adicionada a lista de resultado.
            if palavra_atual:
                resultados.append("%s\t%s\n" % (palavra_atual, acumulador_atual))
            palavra_atual = palavra
            acumulador_atual = acumulador

    # Isso e necessario para computar o ultimo item.
    if palavra_atual == palavra:
        resultados.append("%s\t%s\n" % (palavra_atual, acumulador_atual))

    return resultados
