from numpy.random import seed
from numpy.random import shuffle

seed(1)


class Empresa:
    """
    Dados da empresa
    """

    nome: str
    sede: str


class Vaga(Empresa):
    """
    Dados da vaga
    """

    tipo: str
    quant: int

    def __init__(self, nome: str, sede: str, tipo: str, quant: int):
        self.nome = nome
        self.sede = sede
        self.tipo = tipo
        self.quant = quant

    def __repr__(self) -> str:
        return f"Vaga(nome={self.nome}, sede={self.sede}, tipo={self.tipo}, quant={self.quant})"


class Candidato:
    """
    Dados do candidato
    """

    nome: str
    idade: int
    doc: str
    vaga: Vaga

    def __init__(self, nome: str, idade: int, doc: str):
        self.nome = nome
        self.idade = idade
        self.doc = doc

    def my_vaga(self, vaga: Vaga):
        """
        Método para adicionar uma vaga ao candidato

        :param Vaga vaga: Instância da classe vaga para ser atrelado ao candidato
        """
        self.vaga = vaga

    @staticmethod
    def num_sorte() -> list:
        sequence = [i for i in range(1, 60)]
        shuffle(sequence)
        return sequence

    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}, Idade: {self.idade}\n"
            f"Vaga: {self.vaga.nome}, Sede: {self.vaga.sede}\n"
            f"Tipo: {self.vaga.tipo}"
        )


vaga1 = Vaga("Distak", "Baraúnas", "Designer Gráfico", 1)
vaga2 = Vaga("Distak", "Shopping", "Recepcionista", 2)
candidato1 = Candidato("David", 21, "000.111.222-33")
candidato2 = Candidato("Raquel", 18, "111.444.555-66")
cadastro1 = Vaga("Distak", "Baraúnas", "Designer Gráfico", None)
cadastro2 = Vaga("Distak", "Shopping", "Recepcionista", None)
candidato1.my_vaga(cadastro1)
candidato2.my_vaga(cadastro2)

print("CANDIDATO 1: ")
print(candidato1)
print("-" * 20)
print("CANDIDATO 2: ")
print(candidato2)
print("-" * 20)
print(vaga1)
print("-" * 20)
print(candidato1.num_sorte())
