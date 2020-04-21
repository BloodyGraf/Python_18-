# Попробуйте написать следующую игру:
# Классическая игра на условных конструкциях: угадай, какое число.
# Пользователя вначале спрашивают, какой уровень сложности он готов выбрать: низкий, средний и высокий.
# На низком уровне у человека будет 12 попыток,  на среднем - 9, на высоком - только 6.
# Если человек вводит слишком большое число, ему говорится, что “нужно поменьше”,
# если маленькое - пишет “ нужно побольше”.
# Если человек угадал, тогда ему нужно написать, что он победил. Если проиграл, утешить.

import random

print("Hi, I'm program and I want to play a little game")
print("Choose game difficulty:")
print("1. Easy")
print("2. Normal")
print("3. Hard")
print("4. Nightmare")

difficulty = 0
correctInput = False
while not correctInput:
    difficultInput = input()
    if difficultInput.isnumeric():
        difficulty = int(difficultInput)
        if 0 < difficulty < 5:
            correctInput = True
    else:
        print("Please, try choose a difficulty by select number")

maxTryCount = {
    1: 12,
    2: 9,
    3: 6,
    4: 0
}.get(difficulty, -1)
print("Ok, lets start, your have to guess a number and you have " + str(maxTryCount) + " attempts")
randomNumber = random.randint(1, 10)
win = False
while maxTryCount > 0:
    print("Make your guess")
    guessInput = input()
    if guessInput.isnumeric():
        maxTryCount = maxTryCount - 1
        guess = int(guessInput)
        if guess > randomNumber:
            print("Nope, choose a number little smaller")
        elif guess < randomNumber:
            print("Nope, try a bigger number")
        else:
            win = True
            maxTryCount = -1
    else:
        print("Hey man, a number please")

if win:
    print("Congratulations, You Win!!!")
else:
    print("Sorry man, your lose, don't worry, your luck will come back next time")