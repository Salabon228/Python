# 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

spis = [2, 3, 4, 5, 6]
result = []
for i in spis:
    result.append(spis[len(spis)-1]*i)
    spis.pop()


print(result)