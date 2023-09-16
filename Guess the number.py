import random 
import sys

number = random.randint(1,100) 
running = True

while running:
    guess = int(input('Угадай число: '))
    
    if guess == number:
        print('Поздравляю ты молодец,угадал!')
        running = False
    elif guess < number:
        print('Ты близок,число больше этого :) ')
    else:
        print('Число по меньше ;)')
else:
    print('До встречи!')
print(sys.stdin.readline())
