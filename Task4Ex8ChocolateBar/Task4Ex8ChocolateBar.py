# Задача 4: Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# Импортирование функции для прекращения работы программы.

import sys

# Введение данных.

heigh = int(input('Введите первый размер шоколадки: '))
long = int(input('Введите второй размер шоколадки: '))
piece = int(input('Введите искомую часть шоколадки: '))

# Поиск общего размера шоколадки.

chocoBarSize = heigh * long

# Поиск наименьшей возможной части.
# Проверка на ноль.

if heigh == 0 or long == 0:
    sys.exit('Такой шоколадки БЫТЬ НЕ МОЖЕТ!')

# Поиск большей и меньшей стороны.

smallestPiece = 0
if long >= heigh:
    smallestPiece = heigh
    biggestPiece = long
else:
    smallestPiece = long
    biggestPiece = heigh 

# Проверка размера искомой части.
if piece < smallestPiece or piece >= chocoBarSize:
    sys.exit('Такую часть НЕВОЗМОЖНО отломить одним разломом!')

# Основная проверка возможности поиска искомого размера одним надломом.
# ----- Создание временных переменных.
temp1 = heigh
temp2 = long
gradeNum = heigh * long
# ----- Создание сверяемых списков.
possiblePieces1 = []
possiblePieces2 = []
# ----- Поиск размера списков.
lenNumList1 = len(possiblePieces1)
lenNumList2 = len(possiblePieces2)
# ----- Создание списка множителей к первой стороне шоколадки.
for i in range(heigh, gradeNum, heigh):
    possiblePieces1.append(temp1 * (temp2))
    temp2 = temp2 - 1
possiblePieces1 = possiblePieces1[::-1]
# ----- Создание списка множителей ко второй стороне шоколадки.
for i in range(long, gradeNum, long):
    possiblePieces2.append(long * (heigh))
    heigh = heigh - 1
possiblePieces2 = possiblePieces2[::-1]
# ----- Возврашение переменным их первоначальных значений.
# ----- Избежать этого я не смог, как и не продумал возможность цикла в цикле...
heigh = temp1

# Основное сравнение c проверкой на шоколадку из двух частей с искомой одной частью!

if heigh == 1 and long == 2 and piece == 1:
    print('Такую часть ВОЗМОЖНО отломить одним разломом!')
elif heigh == 2 and long == 1 and piece == 1:
    print('Такую часть ВОЗМОЖНО отломить одним разломом!')
elif piece in possiblePieces1:
    print('Такую часть ВОЗМОЖНО отломить одним разломом!')
elif piece in possiblePieces2:
    print('Такую часть ВОЗМОЖНО отломить одним разломом!')
else:
    sys.exit('Такую часть НЕВОЗМОЖНО отломить одним разломом!')
    
