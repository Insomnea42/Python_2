# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число N: '))
i = 1
res = 1
while i <= n:
    res *= i
    i += 1
    print(f'{res},')
