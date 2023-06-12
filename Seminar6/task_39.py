# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

N = int(input("Введите количество элементов в массиве N: "))
first = []
for i in range(N):
    first.append(input(f"Введите {i + 1} элемент множества: "))
print(first)

M = int(input("Введите количество элементов в массиве M: "))
second = []
for i in range(M):
    second.append(input(f"Введите {i + 1} элемент множества: "))
print(second)

unique_second = set(second)

result = []
for el in first:
    if el not in unique_second:
        result.append(el)
print(f"Элементы первого массива, которых нет во втором: {', '.join(result)}")





# n = int(input('Введите n: '))
# lst_one = [int(input(f'Введите {i + 1}-е число первого массива: ')) for i in range(n)]
# m = int(input('Введите m: '))
# lst_two = [int(input(f'Введите {i + 1}-е число: второго массива')) for i in range(m)]

# print(*[num for num in lst_one if num not in lst_two])




# from random import randint
# from typing import List


# def get_list(number: int) -> List[int]:
#     return [randint(1, 10) for _ in range(number)]


# num_1 = int(input('введите число элементов 1-го массива: '))
# numbers_1 = get_list(num_1)
# print(numbers_1)

# num_2 = int(input('введите число элементов 2-го массива: '))
# numbers_2 = get_list(num_2)
# print(numbers_2)

# for elem in numbers_1:
#     if elem not in numbers_2:
#         print(elem, end=' ')