import datetime

class Amigo:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def calcular_idade(self):
        data_atual = datetime.date.today()
        idade = data_atual.year - self.data_nascimento.year
        if data_atual.month < self.data_nascimento.month or (data_atual.month == self.data_nascimento.month and data_atual.day < self.data_nascimento.day):
            idade -= 1
        return idade

amigos = []
for i in range(10):
    nome = input(f"Digite o nome do amigo {i+1}: ")
    data_nascimento_str = input(f"Digite a data de nascimento do amigo {i+1} (formato: DD/MM/AAAA): ")
    data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
    amigo = Amigo(nome, data_nascimento)
    amigos.append(amigo)

amigo_mais_novo = None
idade_mais_novo = float('inf')

for amigo in amigos:
    idade = amigo.calcular_idade()
    if idade < idade_mais_novo:
        idade_mais_novo = idade
        amigo_mais_novo = amigo

print(f"O amigo mais novo é {amigo_mais_novo.nome} com {idade_mais_novo} anos.")
