# Решение через список!

# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Импортирование функции для прекращения работы программы.

import sys

# Введение числа и создание списка.

threeDigitNum = int(input('введите трехзначное число: '))
threeDigitNumList = []

# Перевод элементов числа в список, по одному, с конца за счет .append 
# и возвращение правильного порядка для элементов.
# (хорошо бы сделать это через функции, но я пока не понимаю как...).

while threeDigitNum > 0:
    threeDigitNumList.append(threeDigitNum % 10)
    threeDigitNum = threeDigitNum // 10
threeDigitNumList = threeDigitNumList[::-1]

# Ввод переменных для суммы чисел и длинны списка.
# Поиск суммы элементов списка и проверка на 3-х значность.

singleDigitNumber = 0
listLength = len(threeDigitNumList)
if len(threeDigitNumList) == 3:
    for i in range(listLength):
        singleDigitNumber = singleDigitNumber + threeDigitNumList[i]
else:
    sys.exit('Вы ввели не трехзначное число!')

# Вывод результата.

print(f'{singleDigitNumber} - сумма элементов в списке')


