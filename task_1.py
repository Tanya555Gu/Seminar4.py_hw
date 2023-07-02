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
list_n = []
for i in range(n):
    list_n.append(randint(1, 10))
print(list_n)
list_m = []
for i in range(m):
    list_m.append(randint(1, 10))
print(list_m)
list_dif = []
for i in list_n:
    for j in list_m:
        if i == j and (i not in list_dif):
            list_dif.append(i)
# print(list_dif)
for i in range(len(list_dif)):
    minPos = i
    for j in range(i, len(list_dif)):
        if list_dif[j] < list_dif[minPos]:
            minPos = j
    x = list_dif[i]
    list_dif[i] = list_dif[minPos]
    list_dif[minPos] = x
print(list_dif)


