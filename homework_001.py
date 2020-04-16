# сколько тебе будет лет в таком то году?
# Программа,  которая спрашивает сколько тебе лет, потом ты вбиваешь год. Программа отвечает сколько тебе лет.
#
import datetime

print("Hi, I'm program which tell how many years will you be in some year")
print("What is your name: ")
name = input().strip().lower().title()
print("Nice to meet you " + name + "!")
print("How old are you?")
age = int(input())
yearnow = datetime.datetime.now().year
print("In what year you want to know your age?")
futureyear = int(input())
print()
futureage = age + futureyear - yearnow
if futureage < 0:
    print("In " + str(futureyear) + " you don't even born")
elif futureage > 60:
    print("In " + str(futureyear) + " you will be dead already")
else:
    print("Your age in " + str(futureyear) + " will be " + str(futureage))


