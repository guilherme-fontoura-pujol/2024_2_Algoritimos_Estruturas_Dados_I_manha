from Automovel import Automovel
class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, qtdPortas, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade = 0)
        qtdPortas = qtdPortas
    def imprimirInformacoes(self):
        txt = super().imprimirInformacoes()
        txt += "\nQuantidade de Portas: " + str(self.qtdPortas)
        print(txt)
