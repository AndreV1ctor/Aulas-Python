#classes - montar os objetos (aproximar real das estruturas do mundo digital)
#A função __init__, também chamada de"método construtor", é o construtor da classe. Responsável por toda vez que criar um novo objeto da classe (Veiculo), dizer o que precisamos pra construir a classe.
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
        
carro = Veiculo('carro', '4f8sd94f9sd84f98sd4f', 'MarcaX', 'X001', '2012')
objeto_aviao = Aviao('Carga', 'Quadrimotor', 'SoulCode Airlines', 'Airbus a380', '2010')
