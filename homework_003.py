#  Вывести полную таблицу умножения, вместе с числами, которые учавствуют в операции,  в таком виде:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3

print("Hi, I'm program which print multiplication table. \r\nHere your go: \r\n")
for num1 in range(1, 10):
    for num2 in range(1, 10):
        print(str(num1) + ' * ' + str(num2) + ' = ' + str(num1 * num2))
    print()