# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число N: '))

i=1
sum = 0
res=0
while i<=n:
    res = (i+(1//i))**i
    print(f'{i}: {res},') 
    i+=1
    sum+=res
print(sum)