
# def abc(a, b=2, c=3):
#     print(a,b,c)
# abc(100) # только первый параметр обязательный
# abc(100, c=200) # Явно указываем передачу значения конкретному параметру
#
# def fn(*params): # функция принимает неграниченное количество параметров(tuple)
#     for i in params:
#         print(i)
# fn(1,3,5,7,2,5)
#
# def fn2(**params): # функция принимает параметры в виде словаря
#     for k,v in params.items():
#         print(k,v)
# fn2(a=100,qwerty=90,fff='ff')
#=================================================================
# def area_of_disk(radius):
#     '''Эта описание фнкции для выдачи в помощи через help(area_of_disk)'''
#     return radius*2*3.14
# print(area_of_disk(2))
# help(area_of_disk)
# #=================================================================

# import math
# print(dir(math)) # список функций из модуля math
# import time

# from math import cos,sin # импорт отдельных функций из модуля
# print(cos(2), sin(3))
# from math import sqrt as math_sqrt #импорт функции под псевдонимом для избежания конфликтов
# print(math_sqrt(10))
#
# import sys
# print(sys.path) # пайтоновский список путей по умолчанию

if __name__ == '__main__': # Запускать только если в основном файле, кроме вызова в другом
    print("qwerty")
