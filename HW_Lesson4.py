# Домашнее задание к занятию №4
# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
from random import choices

def F(names, N):
    return choices(names, k=N)

list_names = F(['Harry', 'Oliver', 'Jack', 'Charlie', 'Thomas', 'Jacob', 'Alfie', 'Riley', 'William', 'James', 'Amelia', 'Olivia', 'Jessica', 'Emily', 'Lily', 'Ava', 'Heather', 'Sophie', 'Mia', 'Isabella'], N=100)
print(list_names)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
def most_offer(names):
    word = {}
    for name in names:
        word[name] = word.get(name, 0) + 1
    word = list(word.items())
    word.sort(key=lambda x: x[1], reverse=True)
    return word[0][0]

print(most_offer(list_names))

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def rare_letter(names):
    letters = {}
    for name in names:
        for char in name:
            letters[char] = letters.get(char, 0) + 1
    letters = sorted(list(letters.items()), key=lambda x: x[1])
    return letters[0][0]

print(rare_letter(list_names))

# 4.  В файле с логами найти дату самого позднего лога (по метке времени):
from datetime import datetime # загрузить модуль DateTime<<<импортировать модуль работающий с датами

with open('C:/Users/alex_/OneDrive/Documents/Python/My_project/Py_Lesson_1.1/log','r', encoding='utf-8') as file:       # открыть файл
    last_date = 0                                                                                                       # создание переменной
    for line in file:                                                                                                   # цикл проверяющий на последнюю дату
        if not last_date:
            last_date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
            continue
        date = datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
        if date > last_date:                                                                                            # условие присваивающее переменной значение факт. даты, если первое условие не выполнено
            last_date = date
print(last_date)
