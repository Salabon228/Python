# 11. Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
a = random.randint(1, 99)
print(f'Рандомное число = {a}')
first_num = a // 10
secont_num = a % 10

if first_num > secont_num:
    print(f'наибольшая цифра = {first_num}')
else:
    print(f'наибольшая цифра = {secont_num}')