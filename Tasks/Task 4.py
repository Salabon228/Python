# 4. Показать первую цифру дробной части числа
print('Введите десятичную дробь (разделение точкой!), я покажу вам первую цифру дробной части: ')
a = float(input())
print(int(a*10 % 10))