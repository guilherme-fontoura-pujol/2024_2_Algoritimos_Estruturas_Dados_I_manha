from Automovel import Automovel
class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, partidaEletrica, velocidade = 0):
        Automovel.__init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade = 0)
        if partidaEletrica == True:
            partidaEletrica = "Elétrica"
        else:
            partidaEletrica == "A Pedal"
    def imprimirInformacoes(self):
        txt = super().imprimirInformacoes()
        txt += "\nPartida: " + self.partidaEletrica
        print(txt)