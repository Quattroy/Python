# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# st = str(input("Введите значения строки: ").split(""))
# print(st)


sp = input().split()
sl = {}
res = ''
for i in sp:
    if i not in sl:
        res += i + ' '
        sl[i] = 1
    else:
        res += i + '_' + str(sl[i]) + ' '
        sl[i] += 1
print(res)



# sp = input().split()
# sl = {}
# res = ''
# for i in sp:
#     if i not in sl:
#         res += f"{i} "
#     else:
#         res += f"{i}_{sl[i]} "
#     sl[i] = sl.get(i, 0) + 1
# print(res.strip())