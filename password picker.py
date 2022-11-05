import random 
import string

print(' welcome to password picker ')
print( )
while True:
    for i in range(3):
    # adjective
        adjectives = ['sleepy', 'weird', 'slow', 'wet'\
        'fat', 'yellow', 'flutty', 'blue', 'proud', 'brave'\
            'white', 'smelly']
    #noun 
        nouns = ['apple','dinosaur', 'toaster', 'dragon','duck','hammer'\
        'panda','goat','dragon','music','tears']

        number = random.randrange(0,100)
        special_char = random.choice(string.punctuation)

        adjective = random.choice(adjectives)
        noun = random.choice(nouns)

        password = adjective + noun + str(number) + special_char

        # print(f'your new password is {password}')
        print('password : %s' % password)
        print()

    generateAnother = input('Do you want another password ? (y/n) ')
    if (generateAnother == 'n' or 'N'):
        print(' Thank you ')
            
        break