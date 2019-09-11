import json

from fundamentus import get_data
from day import get_dia
from datetime import datetime

global lista, dia

# First update
lista, dia = dict(get_data()), datetime.strftime(get_dia(), '%m-%d-%Y')
lista_json = json.dumps(lista)

#print(dia)
print(lista_json)

"""
# Then only update once a day
if dia == datetime.strftime(datetime.today(), '%d'):
    print(dia)
else:
    lista, dia = dict(get_data()), datetime.strftime(get_dia(), '%d')
    print(dia)
"""
