"""Generator strong password with the regular expressions"""
import random

'''Strong passwor requirements
    1 - must have eight marks
    2 - minimum one special character @,!,%,# itd.
    3 - have small or big expressions
'''
'''chr od 33 do 126'''

password = ''
for i in range(8):
    losowa = random.randint(33, 126)
    password += chr(losowa)
if len(password) == 8:
    print('Wygenerowane hasło to:', password)
else:
    print('Wygenerowane hasło nie posiada wymaganych znaków lub jest za krótkie')
