# самодокументированный код
# from typing import List, Dict, Tuple
# def foo(a: int, b: int) -> bool:
#     return a > b
# def fn(a: str, b: str, c: str) -> List:
#     pass
# lst: List[int]
# dct: Dict[str,int]
# tpl: Tuple[int]
# t: List[Tuple[int,int]]

import re
# regexp = 'a'
# str1 = 'VasyA@mail.ru'
#match = re.match(regexp, str1) # Проверка, начинается ли str1 с буквы regexp
#print(match.group(0))
#match = re.search(regexp, str1) # Проверка, есть ли в str1  буквa regexp
#print(match.group(0), match.start(), match.end())
#print('позиция найденного элемента -', str1.find('l'))
#match = re.findall(regexp, str1, re.I) # Список вхождений буквы, независимо от регистра
#print("Список вхождений", regexp, match)
#split = re.split('-', '20-100-982-999', maxsplit=2)
#print(split)
#subn = re.subn('a','b', str1)
#print('Замена а на b в', str1, sub)
# pattern = re.compile(regexp,re.I)
# print(pattern.match(str1))
# print(pattern.search(str1))
# print(pattern.findall(str1))
# print(pattern.subn('b', str1))
#========================================================
# #===== Регулярные выражения========
str2 = 'Python programming. For Absolute Beginner'
# r = re.findall(r'.', str2) # '.' - абсолютно все буквы, '\.' - именно точку, r - исключает обработку пайтоном
# print(r)
# r = re.findall(r'\w', str2) # Без пробелов
# print(r)
# r = re.findall(r'[for]', str2) # класс символов
# print(r)
# r = re.findall(r'[^for]', str2) # исключение класса символов из строки
# print(r)
# r = re.findall(r'[a-zA-Z0-9]', str2) # все символы и цифры, оно же \w
# print(r)
# r = re.findall(r'\w+', str2) # Квантификатор - минимум одно вхождение, оно же w{1,}
# print(r)
# r = re.findall(r'\w*', str2) # Квантификатор - вообще все с пробелами оно же w{0,}
# print(r)
# r = re.findall(r'\w{3}', str2) # Квантификатор - группирут по 3 символа
# print(r)
# r = re.findall(r'\w{3} ', str2) # Квантификатор - группирут где по 3 символа и пробел
# print(r)
# r = re.findall(r'^\w+', str2) # Квантификатор - одно первое вхождение
# print(r)
r = re.findall(r'\w+$', str2) # Квантификатор - одно последнее вхождение
print(r)
str3 = 'abc.test@gmail.com'
r = re.findall(r'@\w+.\w+', str3)
# [a-zA-Z0-9] ->\w  ^[a-zA-Z0-9] ->\W
# [0-9] -> \d  ^[0-9] -> \D
# {1,} +
# {0,} *
# {}
print(r)
r = re.findall(r'\.\w+$', str3)
print(r)
str4 = 'asd 45-1234 1-12-2017, qwe 34-8765 30-8-2019, zxc 66-9876 12-05-2020'
# Выбрать даты
r = re.findall(r'\d{1,2}-\d\d?-\d{4}', str4)
print(r)
r = re.findall(r'\d{1,2}-\d\d?-(\d{4})', str4) # группировка
print(r)