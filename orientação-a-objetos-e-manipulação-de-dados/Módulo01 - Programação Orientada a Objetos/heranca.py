class Veiculo():
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindrada):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindrada = cilindrada

v = Veiculo('carro', '5S68T9F1C2C3D5R', 'Ferrari', 'F112', '2020')
print(vars(v))
m = Motocicleta('motocicleta', '4256F5B2B7BR8', 'Honda', 'CG', '2010', 150)
print(vars())