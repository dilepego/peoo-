class Viagem:
    def __init__(self):
        self.__tempo = 0
        self.__distancia = 0

    def set_distancia(self, distancia):
        self.__distancia = distancia

    def set_tempo(self, tempo):
        self.__tempo = tempo
    
    def get_distancia(self):
        return self.__distancia
    
    def get_tempo(self):
        return self.__tempo
    
    def velocidade_media(self):
        vm = self.__distancia / self.__tempo
        return vm

viagem = Viagem()
viagem.set_distancia(float(input('Quantos quilômetros percorridos?: ')))
viagem.set_tempo(float(input('Tempo que levou: ')))

resultado = viagem.velocidade_media()
print('A velocidade média é:', resultado)