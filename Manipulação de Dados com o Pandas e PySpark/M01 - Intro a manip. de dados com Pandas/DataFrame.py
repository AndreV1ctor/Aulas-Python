#A base de um DataFrame #

import numpy as np
import pandas as pd

df = pd.DataFrame({ 'Aluno':["André", "Victor", "Luan", "Manu", "Bolinho"],
                    'Faltas':[3,4,2,4,3],
                    'Prova':[2,7,8,5.5,9.2],
                    'Seminario':[8.5,5,8.2,6,9.5]})

print(df)