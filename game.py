'''
Author: Daniel Frederick
Date: November 6, 2018
'''

# a fight between characters
class Fight:
    def __init__(self):
        pass


# idk yet
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100

    def __str__(self):
        return 'Name: {}. Health: {}. Inventory: {}.'.format(self.name, self.health, self.inventory)

    # adds an item to character's inventory, returns true or false
    def addItem(self, item):
        # if issubclass(type(item), Item):
        self.inventory.append(item)
        print("Added {} to {}'s inventory.".format(item.name, self.name))

    # removes an item from character's inventory, returns true or false
    def removeItem(self, item):
        if type(item) == 'Item':
            self.inventory.pop(item)
            return True5
        else:
            return False

    # runs items action method if character has item, returns true or false
    def useItem(self, item):
        if item in self.inventory:
            item.action()
            return True
        else:
            return False


class Item:
    def __init__(self, name, act):
        self.name = name

    def __str__(self):
        return 'Name: {}.'.format(self.name)

    def __repr__(self):
        return 'Basic Item: (Name: {}.)'.format(self.name)

    def action(self):
        print(act)


class Weapon(Item):
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg

    def __str__(self):
        return 'Sword: (Name: {}. Damage: {}.)'.format(self.name, self.dmg)

    def __repr__(self):
        return 'Sword: (Name: {}. Damage: {}.)'.format(self.name, self.dmg)


class Sword(Weapon):
    '''
    def __init__(self, name, dmg):
        self.name = name
        self.dmg = dmg
    '''


class Bow(Weapon):
    def __init__(self, name, dmg, range):
        self.name = name
        self.dmg = dmg
        self.range = range

    def __str__(self):
        return 'Bow: (Name: {}. Damage: {}. Range: {}.)'.format(self.name, self.dmg, self.range)

    def __repr__(self):
        return 'Bow: (Name: {}. Damage: {}. Range: {}.)'.format(self.name, self.dmg, self.range)


class Helper:
    def __init__(self):
        pass

    # returns string name
    def getName(self):
        while True:
            try:
                x = str(input('Enter name for character --> '))
                break
            except ValueError:
                print('Please enter only letters for the name')
        return x

    # asks user question, and gives them options from ar options. Returns int corresponding to choice in options
    def getAnswer(self, question, options=['Yes', 'No']):
        print(question)
        for i in range(0, len(options)):
            print('Press {} for {}.'.format(i, options[i]))
        while True:
            choice = input('--> ')
            choice = int(choice)
            if choice < len(options):
                return choice
            else:
                print('Sorry, that is not an acceptable answer. Try again')


class Game(Helper):
    def __init__(self):
        self.mc = Character(self.getName())
        y = ['Sword', 'Bow']
        x = self.getAnswer('Do you want to start with a sword or a bow?', y)
        if x == 1:
            self.mc.addItem(Sword('Trustee Sword', 10))
        elif x == 2:
            self.mc.addItem(Bow('Trustee Bow', 10, 5))

        print(self.mc)

        self.story(1)


    def story(self, part):
        if part == 1:
            print('The lights turn on. You see a pedestal.')
            print('You see a book in front of you on the pedistal.')
            print('You open the book and start to read:')
            print('Once upon a time, in a land far away...')
            print('There lived a knight named {}.'.format(self.mc.name))
            print('With the help of his {}, he saved the kingdom many times over.'.format(self.mc.inventory[0]))
            print('You put the book down, and look around the room.')
            print('You see a window, a staircase, and a door.')
            y = ['Look out the window.', 'Go down the staircase.', 'Try the door.']
            choice = self.getAnswer('What do you do?', y)


temp = Game()
