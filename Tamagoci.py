 #from random import randrange

class Tamagochi:
    '''The tamagochi game'''

    excitement_max = 10
    excitement_start = 5
    excitement_warning = 3
    full_max = 10
    full_start = 6
    full_warning = 2
    hygiene_max = 10
    hygiene_start = 4
    hygiene_warning = 3
    vocab = ['Hello']

    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.full = self.full_start
        self.vocab = self.vocab[:]
        self.hygiene = self.hygiene_start
        self.excitement = self.excitement_start
    def __subtraction(self):
        self.hygiene_start -= 1
        self.full_start -= 1
        self.excitement_start = -1

    def mood(self):
        if self.full > self.full_warning and self.excitement > self.excitement_warning and self.hygiene > self.hygiene_warning:
            return 'happy'
        elif self.full < self.full_warning:
            return 'Hungry'
        else:
            'Bored'

    def __str__(self):
        return 'Im' + self.name + 'I feel' + self.mood()

    def teach(self, word):
        self.vocab.append(word)
        self.__subtraction()

    def talk(self):
        print('Im', self.animal_type, 'named', self.name, 'I feel', self.mood())

    def feed(self):
        print('Crunch...')
        self.full += 2

        if self.full < 0:
            self.full = 0
            print('Im still hungry')
        elif self.full > self.full_max:
            self.full = self.full_max
            print('I am full')
        self.__subtraction()

    def hygienes(self):
        print('Plump...')
        self.hygiene += 3

        if self.hygiene < 0:
            self.hygiene = 0
            print('I am messy...')
        elif self.hygiene > self.hygiene_max:
            self.hygiene = self.hygiene_max
            print('Mmmm I am clean...')
        self.__subtraction()

    def play(self):
        print('Whoo...')
        self.excitement += 2

        if self.excitement < 0:
            self.excitement = 0
            print('I am bored')
        elif self.excitement > self.excitement_max:
            self.excetiment = self.excitement_max
            print('I am happy')
        self.__subtraction()

def main():
    pet_name = input('What do you want to name your pet? ')
    pet_type = input('What type of animal is your pet? ')

    my_pet = Tamagochi(pet_name, pet_type)

    print('Hello I am' + my_pet.name + 'and I am new here' + 'Please enter to start')

    choice = None
    while choice != 0:
        print('''
            INTERACT WITH YOUR PET
            1 - feed your pet
            2 - Talk with your pet
            3 - Teach your pet a new word
            4 - Play with your pet
            5 - Wash your pet
            0 - Quit
            ''')

        choice = input('Choice: ')
        if choice == '0':
            print('Bye Bye')
            quit()
        elif choice == '1':
            my_pet.feed()
        elif choice == '2':
            my_pet.talk()
        elif choice == '3':
            new_wrod = input('What do you want to teach your pet say: ')
            my_pet.teach(new_wrod)
        elif choice == '4':
            my_pet.play()
        elif choice == '5':
            my_pet.hygienes()
        else:
            print('Sorry, that is not a valid option')
main()
