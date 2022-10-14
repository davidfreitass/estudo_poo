class Animal:
    raca: str
    cor: str
    sexo: str


class Pet(Animal):
    nome: str
    idade: int
    vacinado: bool = False

    def __init__(self, nome: str, idade: int, raca: str, cor: str, sexo: str):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.cor = cor
        self.sexo = sexo

    def vacinou(self) -> bool:
        self.vacinado = True
        return self.vacinado


class Pessoa:
    nome: str
    idade: int
    pet: Pet

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def new_pet(self, pet: Pet):
        self.pet = pet


pessoa = Pessoa("David", 21)
meu_pet = Pet("Zé", 2, "siames", "bege", "M")
meu_pet.vacinou()
pessoa.new_pet(meu_pet)

print(pessoa.nome)
print(pessoa.pet.nome)
print(pessoa.pet.vacinado)
