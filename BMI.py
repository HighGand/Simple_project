# BMI calculate
import pyinputplus as pyip

print('Please give me your weight in kilogram: ')   
weight = int(input())        

print('Please give me your height in meter: ')
height = float(input())

def bmi_calculate(weight, height):
    BMI = round((weight / height**2), 1)
    print('Your BMI is: {}'.format(BMI))
    print()
    print('''BMI < 16 - wygłodzenie
16 - 16.99 - wychudzenie
17 - 18.49 - niedowaga
18.5 - 24.99 - waga prawidłowa
25.0 - 29.99 - nadwaga
30.0 - 34.99 - I stopień otyłości
35.0 - 39.99 - II stopień otyłości
BMI > 40.0 - III stopień otyłości zwany otyłością skrajną.''')

bmi_calculate(weight, height)
input()
