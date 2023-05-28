class Frete:
    def __init__(self, distancia, peso):
        self.distancia = distancia
        self.peso = peso
        
        if self.distancia <= 0 or self.peso <= 0:
            raise ValueError("A distância e o peso devem ser positivos.")
    
    def set_distancia(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser positiva.")
        
        self.distancia = distancia
    
    def set_peso(self, peso):
        if peso <= 0:
            raise ValueError("O peso deve ser positivo.")
        
        self.peso = peso
    
    def get_distancia(self):
        return self.distancia
    
    def get_peso(self):
        return self.peso
    
    def calc_frete(self):
        return self.peso * self.distancia * 0.01
    
    def __str__(self):
        return "Distância: {} Km / Peso: {} Kg".format(self.distancia, self.peso)


if __name__ == "__main__":
    # Exemplo de uso da classe Frete

    # Criar um objeto Frete com valores iniciais
    frete = Frete(100, 80)

    # Interagir com o usuário para obter novos valores de distância e peso
    nova_distancia = float(input("Digite a nova distância em Km: "))
    frete.set_distancia(nova_distancia)

    novo_peso = float(input("Digite o novo peso em Kg: "))
    frete.set_peso(novo_peso)

    # Calcular e exibir o valor do frete
    valor_frete = frete.calc_frete()
    print("O valor do frete é: R$ {:.2f}".format(valor_frete))

    # Exibir os atributos do objeto
    print(frete)

   
