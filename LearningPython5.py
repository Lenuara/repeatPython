# 1 способ работы с файлами
#f = open('test.txt', 'r+', encoding='utf-8')
#f.close()
# # 2 способ работы с файлами c автозакрытием после выхода из блока
# with open('test.txt', 'r+', encoding='utf-8') as f:
#     #print(f.read(10))
#     # print(f.readline())
#     s = f.readline() # читаем построчно
#     while s:
#         print(s)
#         s = f.readline()

# 3 способ работы с файлами c автозакрытием после выхода из блока
# with open('test.txt', 'r+', encoding='utf-8') as f:
#     lines = f.readlines() # получили сразу список строк
# print(lines)

# with open('test.txt', 'r+', encoding='utf-8') as f:
#     for line in f:
#         print(line)

# with open('test.txt', 'a', encoding='utf-8') as f:
#     pass #f.write('\nLine six')
#     print(f.closed) # закрыт или открыт файл True/False
#     print(f.mode) # в каком режиме открыт файл
#     print(f.name) #получить имя файла

#import csv
# with open('data.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter = ',')
#     for line in reader:
#         print(line)

# with open('data.csv', 'a', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter = ',')
#     writer.writerow([])
#     writer.writerow(['Sara', 'Parker', 25])

import os

print(os.getcwd())
print(os.path.exists('text.txt'))
print(os.listdir())







