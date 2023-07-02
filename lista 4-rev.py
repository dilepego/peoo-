class Jogador:
    def __init__(self, nome, camisa, gols):
        self.nome = nome
        self.camisa = camisa
        self.gols = gols

class Time:
    def __init__(self):
        self.jogadores = []

    def inserir_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.jogadores:
            print(f"Nome: {jogador.nome} | Camisa: {jogador.camisa} | Gols: {jogador.gols}")

    def artilheiro(self):
        if not self.jogadores:
            return None

        jogador_artilheiro = max(self.jogadores, key=lambda jogador: jogador.gols)
        return jogador_artilheiro

# Criando um novo time
time = Time()

# Solicitando as informações dos jogadores ao usuário
num_jogadores = int(input("Quantos jogadores deseja cadastrar? "))

for i in range(num_jogadores):
    print(f"\nJogador {i+1}:")
    nome = input("Nome: ")
    camisa = int(input("Número da camisa: "))
    gols = int(input("Número de gols: "))

    jogador = Jogador(nome, camisa, gols)
    time.inserir_jogador(jogador)

# Listando jogadores cadastrados
print("\nJogadores cadastrados:")
time.listar_jogadores()

# Obtendo o artilheiro do time
artilheiro = time.artilheiro()
if artilheiro:
    print(f"\nO artilheiro do time é {artilheiro.nome} com {artilheiro.gols} gols.")
else:
    print("\nNão há jogadores cadastrados.")
