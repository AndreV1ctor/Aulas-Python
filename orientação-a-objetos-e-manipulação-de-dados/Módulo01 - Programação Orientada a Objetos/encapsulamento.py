class Funcionarios():
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0 #atributo private
        self.__horas_trabalhadas = 0 #atributo private
    
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossível alterar salário iretamente. Use a função calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

andre = Funcionarios('André', 'Programador', 50)
andre.salario = 10000