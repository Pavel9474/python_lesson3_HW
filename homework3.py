# Задача 1. Создайте файл. Запишите в него N первых
# элементов последовательности Фибоначчи.

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число членов последовательности:"))
data = open('fibonachi.txt', 'a') 
for i in range(n+1):
    data.write((str(fibonacci(i))))
data.write('\n')
data.close()

