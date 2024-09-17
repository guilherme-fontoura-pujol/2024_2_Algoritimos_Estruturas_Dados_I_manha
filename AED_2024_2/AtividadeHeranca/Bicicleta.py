from Veiculo import Veiculo
class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade = 0)
        self.numMarchas = numMarchas
        if self.bagageiro == True:
            self.bagageiro = "Sim"
        else: self.bagageiro = "Não"
    def imprimirInformacoes(self):
        txt = super().imprimirInformacoes()
        txt += "\nNúmero de Marchas: "
        txt += "\nBagageiro: " + self.bagageiro
        print(txt)