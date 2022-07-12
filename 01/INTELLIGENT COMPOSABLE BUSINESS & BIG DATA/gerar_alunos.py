import random as rd
import uuid

NUMERO_ALUNOS = 1000
NOMES = (
    "Maria",
    "Ana",
    "Francisca",
    "Antonia",
    "Adriana",
    "Juliana",
    "Marcia",
    "Fernanda",
    "Patricia",
    "Aline",
    "Sandra",
    "Camila",
    "Amanda",
    "Bruna",
    "Jessica",
    "Jose",
    "Joao",
    "Antonio",
    "Francisco",
    "Carlos",
    "Paulo",
    "Pedro",
    "Lucas",
    "Luiz",
    "Marcos",
    "Luis",
    "Gabriel",
    "Rafael",
    "Daniel",
    "Marcelo",
)

SOBRENOMES = (
    "Silva",
    "Souza",
    "Pereira",
    "Oliveira",
    "Costa",
    "Rodrigues",
    "Carvalho",
    "Lima",
    "Mendes",
    "Albuquerque",
    "Santos",
)

alunos = []
for i in range(NUMERO_ALUNOS + 1):
    alunos.append(
        f"{uuid.uuid4()},{rd.choice(NOMES)},{rd.choice(SOBRENOMES)},{rd.randint(18, 30)}\n"
    )

with open("alunos.txt", "w") as f:
    f.writelines(alunos)
