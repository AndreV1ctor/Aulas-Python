from tkinter import W


lista = ['a', 'x', 's', 'w', 'd', 'a', 'n', 'a']
#lista.reverse()    <-- #metodo de reversão da lista
lista.sort() #sort utilizado para organizar os elementos

for i in range(len(lista)):
    print(lista[i])

l = lista.count('a') #o count irá contabilizar quantas letras 'a'(elementos) tem na lista em ordem e em seguida dirá em numeros o resultado
print(l)