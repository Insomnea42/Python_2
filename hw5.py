# Реализуйте алгоритм перемешивания списка.

from random import randint, shuffle

n = int(input('Введите число N: '))
list = [0]*n
i = 0

while i < n:
    list[i] = randint(-42, 42)
    i += 1
print(f'Исходный список: {list}')
shuffle(list)
print(f'Перемешанный список: {list}')
