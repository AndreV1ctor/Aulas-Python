# Atributos - caracteristicas que as classes recebem nas suas contruções
# metodos - ações que essas classes executam

class funcionarios():
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    def get_salario(self):
        print("Meu salario é: ", self.salario)

    def get_bonificacao(self):
        return self.salario * 0.15


jose = funcionario('José', '789987456', 5000)
jose.get_salario()
jose.get_bonificacao()