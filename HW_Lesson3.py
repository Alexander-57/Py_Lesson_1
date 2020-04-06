 # Домашее задание к уроку №3
 # В файле содержится текст. Считать/скопировать текст из файла и выполнить

# 1) методами строк очистить текст от знаков препинания;
file = open('C:/Users/alex_/OneDrive/Documents/Python/My_project/Py_Lesson_1.1/ThirdLessonText.txt','r', encoding='utf-8')
file = file.read()
file = file.replace('.', ' ')
file = file.replace(',', ' ')
file = file.replace('—', ' ')
file = file.replace('!', ' ')
file = file.replace('?', ' ')
file = file.replace('«', ' ')
file = file.replace('»', ' ')
file = file.replace(':', ' ')
file = file.replace(';', ' ')
file = file.replace('(', ' ')
file = file.replace(')', ' ')

print(file) #вывод на экран содержимого файла

# 2) сформировать list со словами (split);
file_list = file.split()
print(file_list)

# 3) привести все слова к нижнему регистру (map);
file_lower = file.lower()
print(file_lower)

# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
file_dict = {}
for i in range (len(file_list)):
    count = 0
    word = file[i]
    for i in range (len(file_list)):
        if word == file_list[i]:
            count = count + 1
    file_dict[word] = count
print(file_dict)

# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
file_values = list(file_dict.values())
file_values.sort()
print('Наиболее часто встречающиеся слова: ')
for i in range (5):
    a = int(len(file_values))-1-i
    b = file_values[a]
    for word, count in file_dict.items():
        if count == b:
            print ('слово:', word, 'встречается', count, 'раз')
print('количество разных слов в тексте:', len(file_values))

# 5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

for word in file_list:
    p = morph.parse(word)[0]
    print(p.normal_form)