class Veiculo():
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

carro = Veiculo('carro', '1515198987456', 'MarcaX', 'X001', '2022')
print(vars(carro))
objetos_aviao = Aviao('Carga', 'Quadrimotor', 'SoulCode Airlines', 'Airbus a380', '2020')
print(vars(objetos_aviao))