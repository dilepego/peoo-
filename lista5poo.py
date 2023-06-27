import datetime

class Paciente:
    def __init__(self, nome, fone, nasc, cpf):
        self.nome = nome
        self.fone = fone
        self.nasc = nasc
        self.cpf = cpf

    def idade(self):
        data_atual = datetime.datetime.now()
        anos = data_atual.year - self.nasc.year
        meses = data_atual.month - self.nasc.month

        if data_atual.day < self.nasc.day:
            meses -= 1

        if meses < 0:
            anos -= 1
            meses += 12

        return f"{anos} anos e {meses} meses"

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.fone}\nData de Nascimento: {self.nasc.strftime('%d/%m/%Y')}"
