agenda = {40408021:"José", 87541236:"Heloise", 78945612:"Carlos", 36925874:"Claudio"}
print (agenda)
#del(agenda[40408021]) #<-- o del deleta/elimina por chave
#print(agenda)

print(agenda.keys()) #retorna as chaves
print(agenda.values()) #retorna os valores
print(len(agenda)) #medir tamanho do dicionario exemplo, temos uma agenda com 4 keys e 4 values (retorna numero 4)

print(agenda.popitem()) #popitem remove o ultimo item do dicionario/agenda. 
print(agenda.popitem()) #A cada pop, ele remove o ULTIMO elemento
print(agenda)