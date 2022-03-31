from abc import ABC, abstractmethod #classe abstrata serve como molde para criação de outras classes 
                                    #podendo inserir vários metodos diferentes, pórem, não pode instanciar diretamente
                                    #(nao pode criar um objeto a partir dessa classe, pode-se criar um objeto de uma classe filha dessa classe abstrata)

class letras():
    @abstractmethod
    def mostrarTipo(self):
        print('Eu sou uma classe abstrata!') #um texto da class abstrata

class A(letras):
    def __init__(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print("Aqui é um método diferente!") #um texto da class A

letraa = A("Letra A")
letraa.mostrarTipo()
letraa.imprimir()