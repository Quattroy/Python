# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

# num = int(input())
# i = 1
# factor = 1
# while ( i <= num):
#     factor *= i
#     i += 1
# print(factor)

n = int(input('Введите целое число'))
factorial = 1
 
for i in range(2, n+1):
    factorial *= i
 
print(i, '->',  factorial)