"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

10 -> 1 2 4 8

пользователь будет вводить каждое число на новой строке для задач 10, 12.
"""
n = int(input('Введите число '))
myList = []
count = 1
while n > count:
    myList.append(count)
    count *= 2
print(myList)
