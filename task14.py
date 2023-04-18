# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16
n = int(input("До какого числа нужно показать список квадратов? "))
array_square = []
i=0
num1=1
array_square.append (num1)
while array_square[i]<n:
    i+=1
    array_square.insert(i, 2**i)
array_square.pop()
print (array_square)
    
