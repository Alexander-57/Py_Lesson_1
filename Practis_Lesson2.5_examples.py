#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
for i in range(1, 6):
    print(i, str(0))
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
count = 0
for i in range(10):
    integer_number = int(input("Введите число = "))
    while integer_number > 0:
      number = integer_number%10
      if number == 5:
          count +=1
      integer_number//=10
print("Количество цифр 5 введенных пользователем =", count)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
    sum+=i
print(sum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
multiplication = 1

for i in range(1,11):
    multiplication*=i
print("Произведение цифр от 1 до 10 =", multiplication)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
integer_number = 2129

#print(integer_number%10,integer_number//10)

while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = int(input("Введите число = "))
sum = 0
while integer_number>0:
    a = integer_number%10
    integer_number = integer_number//10
    sum +=a
print("Сумма цифр этого числа равна ", sum)
'''
Задача 7
Найти произведение цифр числа.
'''
integer_number = int(input("Введите число = "))
multiplication = 1
while integer_number>0:
    a = integer_number%10
    integer_number = integer_number//10
    multiplication*=a
print("Произведение цифр этого числа равно ", multiplication)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''
Задача 9
Найти максимальную цифру в числе
'''
integer_number = int(input("Введите число: "))
a = integer_number%10
integer_number = integer_number//10
while integer_number > 0:
    if integer_number%10 > a:
        a = integer_number%10
    integer_number = integer_number//10
print("Максимальная цифра в числе =", a)
'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = int(input("Введите число = "))
count = 0
while integer_number > 0:
    number = integer_number%10
    if number == 5:
        count +=1
    integer_number//=10
print("Количество цифр 5 введенных пользователем =", count)
