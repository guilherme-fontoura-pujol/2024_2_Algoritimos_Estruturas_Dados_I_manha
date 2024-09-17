class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
    def imprimirInformacoes(self):
        print("Marca do Veículo: " + str(self.marca))
        print("Quantidade de Rodas do Veículo: " + str(self.qtdRodas))
        print("Modelo do Veículo: " + str(self.modelo))
        print("Velocidade atual do Veículo: " + str(self.velocidade) + "km/h")
    def acelerar(self, valor):
        if isinstance(valor, int):
            self.velocidade += valor
            print("O Veículo foi acelerado em " + valor + "km/h.")
            print("A Velocidade atual do Veículo é de " + str(self.velocidade) + "km/h.")
        else:
            print("Por favor, utilize apenas valores inteiros.")
    def frear(self, valor):
        if isinstance(valor, int) and velocidade >= valor:
            self.velocidade -= valor
            print("O Veículo foi desacelerado em " + valor + "km/h.")
            print("A Velocidade atual do Veículo é de " + str(self.velocidade) + "km/h.")
        elif isinstance(valor, int) and velocidade <= valor:
            print("Não foi possível desacelerar o veículo pois o valor informado excede a atual velocidade do veículo.")
            print("Utilize um valor igual ou inferior a " + str(self.velocidade))
        else:
            print("Por favor, utilize apenas valores inteiros.")