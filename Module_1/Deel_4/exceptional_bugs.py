import random

# Select 2 numbers
num1 = random.randint(1, 10)
num2 = random.randint(5, 15)

# Ask for an answer
number = int(input(f'Weet jij wat {num1} + {num2} is? '))

# Check the user's answer
try:
     if int(number == num1+num2):
        print('Dat is juist')
except:
        print('Dat is geen nummer!')
try:
    if int(number != num1+num2):
         print('Nee dat klopt niet')
except:
        print('Dat is geen nummer!')
