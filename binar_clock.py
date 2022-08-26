# binar clock

import datetime as dt

now = dt.datetime.now()
 
def hour (x,y,z):
    g = x
    m = y
    s = z
    if x  == 0 or y == 0 or z == 0:
        return '0'
    b = ''
    c = ''
    d = ''
    while x != 0:
        b = str(x % 2) + b
        x = int(x / 2)
    while y != 0:
        c = str(y % 2) + c
        y = int(y / 2)
    while z != 0:
        d = str(z % 2 ) + d
        z = int(z / 2)
    print('Godzina', g, ':', b, '\nMinuta', m, ':', c, '\nSekunda', s, ':', d)
    
conv = now.strftime('%I : %M : %S')

hours = int(conv[0:2])
minutes = int(conv[5:7])
sekunds = int(conv[10:12])

hour(hours, minutes, sekunds)
