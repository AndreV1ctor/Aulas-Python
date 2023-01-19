class Funcionario():
   def __init__(self, nome, cargo, valor_hora_trabalhada):
      self.nome = nome
      self.cargo = cargo
      self.valor_hora_trabalhada = valor_hora_trabalhada
      self.__salario = 0 #atributo private (__salario), por já ter atribuido o valor (0) dentro da classe, não precisa passar ele dentro dos atributos, porque ninguem vai passar ele, por ser privado.
      self.__horas_trabalhadas = 0 #private
      
   @property #estrutura de fator de encapsulamento, 
   def salario(self):
       return self.__salario
    
   @salario.setter #atribuição de um novo salário
   def salario(self, novo_salario): #na tentativa fazer uma atribuição de salario, receberá a mensagem de erro por conta do salario ser privado
       raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")


   def registra_hora_trabalhada(self): #funções que realmente alteram o salario
         self.__horas_trabalhadas += 1

      def calcula_salario(self):
         self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada

   andre = Funcionario('André', 'Programador', 50)
   andre.salario = 100000 
   
   #Exemplo classico de encapsulamento, onde se utiliza um atributo  e impede que seja acessado por fora da classe
   #só podendo ser acessado por estruturas pertecentes da classe.
