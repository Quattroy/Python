# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

num=int(input())
maxim=minim=int(input())
for i in range(num-1):
    n=int(input())
    if minim>n:
        minim=n
    if maxim<n:
        maxim=n
print(f"max = {maxim}, min={minim}")


# n = int(input("Enter the number of watermelons: "))
# num = int(input("Enter weight: "))
# mX = num
# mN = num
# for i in range(n-1):
#     num = int(input("Enter weight: "))
#     mX = max(mX, num)
#     mN = min(mN, num)
# print(f"max={mX} min={mN}")