dias_da_semana = {"dia1":"domingo", "dia2":"segunda", "dia3":"terça", "dia4":"quarta", "dia5":"quinta", "dia6":"sexta", "dia8":"sábado"}

dias_da_semana.popitem()
dias_da_semana.popitem()

del(dias_da_semana["dia2"])

print(dias_da_semana.keys())
print(dias_da_semana.values())

print(dias_da_semana)