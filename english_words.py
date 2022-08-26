# Słówka ang
# import random
words = {'cat': 'kot',
         'dog': 'pies',
         'parrot': 'papuga',
         'mouse': 'mysz',
         'rat': 'szczur',
         'elephant': 'słoń'
}


point = 0
bad_answer = 0

for i in words:
    print(i)
    print('Przetłumacz słowo na język polski')
    answer = input()
    if answer == words[i]:
        print('Gratulacje !')
        point += 1
    else:
        print('Niestety popełniłeś błąd ;(')
        bad_answer += 1
        
print('MIałeś {} poprawnych odpowiedzi i {}  błędnych'.format(point, bad_answer))
input()
