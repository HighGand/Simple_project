# lists shop

lists = {'Elektronieka': ['Telewizor', 'Pralka', 'Odkurzacz', 'Express'],
         'Zabawki': ['Gry', 'Wiatrówka', 'Suszarka_do_włosów'], 'Sport': ['Buty', 'Spodenki x 2', 'Bluzki x 2']}

def lista_zakupów(dict):
    print('Oto lista twoich zakupów')
    
    for k in lists.keys():
        print()
        print(k)
        print('-'*40)
        for v in lists[k]:
            print(v)
        print()
        
lista_zakupów(lists)
