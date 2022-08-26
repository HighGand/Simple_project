sub = {'Angielski': [3, 3, 4, 5], 'Matematyka': [3, 5, 5, 4],
       'WF': [4, 5, 5, 4], 'Historia': [4, 3, 1, 5]}

#print('''Wybierz jedną z dostępnych opcji:
       #0 - Podgląd przedmiotów i ocen
       #1 - Dodanie oceny do przedmiotu
       #2 - Wyliczenie średniej
       #3 - zakończenie programu''')

#choice = input('Your choice: ')
#choices = int(choice)

while True:
       print('''Wybierz jedną z dostępnych opcji:
       0 - Podgląd przedmiotów i ocen
       1 - Dodanie oceny do przedmiotu
       2 - Wyliczenie średniej
       3 - zakończenie programu''')
       
       choice = int(input('Your choice: '))
       
       if choice == 0:
              for k, v in sub.items():
                     print(k, ':', v)
                     
       elif choice == 1:
              subject = input('Witch subject add mark?: ')
              if subject in sub.keys():
                     mark = int(input(('Witch mark you want add? ')))
                     sub[subject].append(mark)
                     print('Add the mark in the {}'.format(subject), sub[subject])

       elif choice == 2:
              schoolSub = input('Whitch item you want to calculate from? ')
              if schoolSub in sub.keys():
                     print(schoolSub, ':', sum(sub[schoolSub])/len(sub[schoolSub]))

       elif choice == 3:
              print('Program the finished')
              quit()

              
#print(sub['WF'])
#print(sub['WF'].append(3))
#print(sub['WF'])

#print(type(sub['Angielski']))
#print(sum(sub['Angielski'])/len(sub['Angielski']))

#print(sub.items())
#print(sub.values())
