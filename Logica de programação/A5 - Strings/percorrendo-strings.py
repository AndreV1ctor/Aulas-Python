nome = 'python'

#percorrer com for
for i in nome:
    print(i)

print('--------------------------------')

#percorrer com while
i = 0
while i < len(nome):     #len é uma propriedade da string que irá contar (verificar o tamanho de uma string) quantos itens possui na string (no caso, quantidade de nome)
    print(nome[i])       #aplicando indexação e fatiamento de string
    i+=1

print('--------------------------------')

#percorrer com for / enumerate
for k, v in enumerate(nome):  # criar duas variaveis, onde uma vai assumir o numero e a outra assumir o valor (numero)
    print(k,v)