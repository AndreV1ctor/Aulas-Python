class Funcionario():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_salario(self):
        print("Meu salário é: ", self.salario)

    def get_bonificacao(self):
        return self.salario * 0.15

andre = Funcionario('André', '7884659421', 5000)
andre.get_salario()
print(andre.get_bonificacao())