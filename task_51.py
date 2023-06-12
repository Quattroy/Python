# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    first = characteristic(objects[0])
    lst = [characteristic(i) == first for i in objects]  
    return (False, True)[len(lst) == sum(lst)]


values = [0, 2, 10, 6, 5]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')




# values = [4, 5, 4]


# def same_by(characteristic, objects):
#     return len(set([characteristic(obj) for obj in objects])) <= 1  


# if same_by(lambda x: x % 3, values):
#     print('same')
# else:
#     print("different")