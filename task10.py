# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, ]
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. 
# Стороны монеты вводятся построчно или в одну строку, если умеете.

# Пример
# Ввод: 1 1 0 0 0 -> Вывод: 2
n = int (input('Сколько всего монет = '))
length = []
positive = 0
negative = 0
if n>1:
    for i in range(n):
        length.append (int(input('Введите цифру обозначающую сторону монеты - "0" или "1" - ')))
        print (length)
        if length[i] >1:
            print ("Введено не верное значение")
            break
        if length[i] == 1:
            positive +=1
        else: 
            negative +=1
    if negative>positive or negative==positive:
        print (f"Необходимо перевернуть минимум {positive} монет")
    else:
        print (f"Необходимо перевернуть минимум {negative} монет")
else:
    print ("Неверно указано количество монет")






