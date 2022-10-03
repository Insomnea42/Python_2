# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input('Введите число N: '))

list = [0] * n
pos = [0]
i = 0
j = 0
res = 1
while i < n:
    list[i] = randint(-n, n)
    i += 1
print(list)
way = str(input('Пропишите путь расположения file.txt: '))
file1 = open("/"+way+"/file.txt", "r")
# мой путь Users/vladelec/Desktop/python/Sems/sem2/HWs

while True:
    line = file1.readline()
    if not line:
        break
    posit = line.strip()
    pos.append(int(posit))
pos.remove(pos[0])

file1.close

for l in pos:
    if l < len(list):
        res *= list[l]
print(res)
