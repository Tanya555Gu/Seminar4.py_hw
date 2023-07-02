# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


from random import randint
n = int(input('Введите количество элементов 1-ого множества -> '))
m = int(input('Введите количество элементов 2-ого множества -> '))
N = []
for i in range(n):
    N.append(randint(1, 10))
print(N)
M = []
for i in range(m):
    M.append(randint(1, 10))
print(M)
Dif = []
for i in N:
    for j in M:
        if i == j and (i not in Dif):
            Dif.append(i)
# print(Dif)
for i in range(len(Dif)):
    minPos = i
    for j in range(i, len(Dif)):
        if Dif[j] < Dif[minPos]:
            minPos = j
    x = Dif[i]
    Dif[i] = Dif[minPos]
    Dif[minPos] = x
print(Dif)


