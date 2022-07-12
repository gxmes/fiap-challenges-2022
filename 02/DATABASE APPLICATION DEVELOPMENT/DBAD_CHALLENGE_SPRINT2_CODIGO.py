def status(tempo):
    if tempo < 240:
        # Menor que 4 minutos
        return "Aceitável"
    elif tempo <= 360:
        # Entre 4 e 6 minutos
        return "Jornada Longa"
    else:
        # Maior que 6 minutos
        return "Jornada Ruim"


def imprimir(texto):
    separador = len(texto) - texto.count("\n")
    print("*" * separador)
    print(texto)
    print("*" * separador)


resultados = []
contador = 1
print("Para parar de enviar dados pressione ENTER.\n")

while 1:

    nome_de_usuario = input(f"[{contador}] Nome de usuário: ")
    if nome_de_usuario == "":
        print("Saindo...\n")
        break

    tempo_de_operacao = input(f"[{contador}] Tempo de operação em segundos: ")
    if tempo_de_operacao == "":
        print("Saindo...\n")
        break

    resultado = status(int(tempo_de_operacao))

    texto = f"\nUsuário: %s, tempo: %ss, status: %s.\n" % (
        nome_de_usuario,
        tempo_de_operacao,
        resultado,
    )

    imprimir(texto)

    resultados.append(resultado)

    contador += 1

usuarios = len(resultados)
aceitavel = resultados.count("Aceitável")
jornada_l = resultados.count("Jornada Longa")
jornada_r = resultados.count("Jornada Ruim")

if jornada_l + jornada_r >= usuarios / 2:
    print("Alerta")
elif jornada_l >= usuarios / 2:
    print("Alerta")
elif jornada_r >= usuarios / 2:
    print("Alerta")
else:
    print("Ok")

print(
    f"Aceitavel: {aceitavel}, longa: {jornada_l}, ruim: {jornada_r}, proporção: {aceitavel}:{jornada_l+jornada_r}\n"
)
