''' Provides random greetings '''
import random
sayings = ('Hello', 'Hi', 'Hey', 'Aloha')

def greet():
    return random.choice(sayings)

def test_greet():
    for loop in range(8):
        print(greet())
    print('\nGreetings Test Completed')

if __name__ == '__main__':
    print(greet())
