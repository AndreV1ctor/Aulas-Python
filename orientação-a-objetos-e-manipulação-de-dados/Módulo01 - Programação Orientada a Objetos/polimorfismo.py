#polimofismo é uma das propriedades da programação orientada a objetos e existe diversas formas de polimorfismo quando trabalhado
#com outro tipo de linguagem de programação (como Java e c#).
#Porém no Python só exista um tipo de polimorfismo que é a sobreposição
#(quando você tem classes que são derivadas de outras classes, podendo utilizar o mesmo metodo da classe pai 
#mas fazendo uma assinatura diferente (se comportando de maneira diferente)).

from abc import ABC, abstractmethod

#RESUMO: criação de uma classe abstrata(A), posteriormente criou duas classes filhas da classe abstrata que utiliza o mesmos metodos da classe principal.

class A(ABC):       #A classe A é a abstrata que vai fazer com que utilize o método que vai ser usado pelas suas filhas que são a B e a C
    @abstractmethod
    def fala(self, msg):
        pass

class B(A):     #essa classe B é uma filha da classe A (passando a classe A como parametro)
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):     #tambem derivada da classe "A"
    def fala(self, msg):
        print(f'C está falando {msg}')

#Vale resaltar que, não pode-se criar um objeto "A" por ser uma classe abstrata, sendo assim, nao pode-se instaciar

b = B()
c = C()
b.fala('de skate')
c.fala('de futebol')