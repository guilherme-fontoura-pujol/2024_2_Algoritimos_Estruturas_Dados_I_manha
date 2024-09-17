from Veiculo import Veiculo
class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade = 0):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade = 0)
        self.potenciaDoMtor = potenciaDoMotor
    def imprimirInformacoes(self):
        txt = super().imprimirInformacoes()
        txt += "\nPotência do Motor: " + str(self.potenciaDoMotor) + "cv"
        print(txt)