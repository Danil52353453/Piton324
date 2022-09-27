#6). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
N = int(input("Введите число : "))
size = 0
for i in range(N):
    size = (1+1/N)
    sum = size * N
    print(round(size,2) )
print (sum,)
    
