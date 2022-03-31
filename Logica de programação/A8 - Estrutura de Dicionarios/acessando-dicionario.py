dicionario = {"a":"letraA", "b":"letraB", "c":"letraC"}
print (dicionario["a"])
print (dicionario.get('d', 'Valor não encontrado.')) #caso o usuario tente acessar uma chave inexistente (como por exemplo, a letra 'd', emitirá uma mensagem de erro)