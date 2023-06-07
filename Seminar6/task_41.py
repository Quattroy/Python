# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

N = int(input("Введите количество элементов в массиве N: "))
array = []
for i in range(N):
    array.append(input(f"Введите {i + 1} элемент множества: "))
print(array)
for i in range(len(array[1 : -1])):
    result = 0
    if array[i] > array[i-1] and array[i] > array[i+1]:
        result += 1
        i +=1
print(result)


# n = int(input('Введите n: '))
# lst = [int(input(f'Введите {i + 1}-е число массива: ')) for i in range(n)]

# print(len([i for i in range(1,len(lst)-1) if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]]))



# size = int(input("Size arr: "))
# n = [int(input(f"Enter {i + 1} number: ")) for i in range(size)]
# count = 0
# for i in range(len(n)-1):
#     if n[i] > n[i-1] and n[i] > n[i+1]:
#         count+=1
# print(count)