class veiculo(): #instanciando a classe veiculo
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Aviao(): 
    def __init__(self, tipo, motor, linha_aerea, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_aerea
        self.modelo = modelo
        self.ano = ano

carro = veiculo('carro', '12342424566666', 'MarcaX', 'x001', '2022')
print(vars(carro))
objeto_aviao = Aviao('Carga', "Quatrimotor", 'SoulCode Airlines', 'Airbus a380', '2010')
print(vars(objeto_aviao))