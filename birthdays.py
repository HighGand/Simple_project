# Birthdays

import datetime

birthday = {'Karola':'08-27', 'Tosia':'08-26', 'Babcia':'08-21', 'Konrad':'10-21', 'Tooday':'08-04',
            'Karol': '08-26'}
today = datetime.datetime.now()
now = today.strftime('%m-%d')

for k, v in birthday.items():
    lista = []
    if v == now:
        lista.append(k)
    else:
        continue
    print('Dziś urodziny ma:', lista[0])
