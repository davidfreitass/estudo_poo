"""
Criar uma estrutura de classes pensando-se em um cenário de vagas de emprego
"""


class Empresa:
    nome: str
    sede: str


class Vaga(Empresa):
    tipo: str
    quant: int

    def __init__(self, nome: str, sede: str, tipo: str, quant: int):
        self.nome = nome
        self.sede = sede
        self.tipo = tipo
        self.quant = quant


class Candidato:
    nome: str
    idade: int
    doc: str
    vaga: Vaga

    def __init__(self, nome: str, idade: int, doc: str):
        self.nome = nome
        self.idade = idade
        self.doc = doc

    def my_vaga(self, vaga: Vaga):
        self.vaga = vaga


vaga1 = Vaga("Distak", "Baraúnas", "Designer Gráfico", 1)
vaga2 = Vaga("Distak", "Shopping", "Recepcionista", 2)
candidato1 = Candidato("David", 21, "000.111.222-33")
candidato2 = Candidato("Raquel", 18, "111.444.555-66")
cadastro1 = Vaga("Distak", "Baraúnas", "Designer Gráfico", None)
cadastro2 = Vaga("Distak", "Shopping", "Recepcionista", None)
candidato1.my_vaga(cadastro1)
candidato2.my_vaga(cadastro2)

print("CANDIDATO 1: ")
print(candidato1.nome, ",", candidato1.idade)
print(candidato1.vaga.nome, "-", candidato1.vaga.sede)
print(candidato1.vaga.tipo)
print("-" * 20)
print("CANDIDATO 2: ")
print(candidato2.nome, ",", candidato2.idade)
print(candidato2.vaga.nome, "-", candidato2.vaga.sede)
print(candidato2.vaga.tipo)
