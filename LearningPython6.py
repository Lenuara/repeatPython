# Отлавливаем ошибки по их видам в тексте кода

# try:
#     a = 10
#     b = 20
#     #c = bb*c
#     d = 'a'
#     d>b
# except NameError:
#     print('Ошибка в имени переменной')
# except TypeError:
#     print('Ошибка в типе переменной')
# except (NameError, TypeError): # Можно объдинять
#     print('Ошибки имени или типа переменной')
# except:
#     print('Какая-то другая ошибка')

#===========================================
# Отлавливаем ошибки из ввода

# try:
#     age= input("Введите свой возраст: ")
#     age = int(age)
#     print('Все хорошо, вы подходите по возрасту')
#     if age < 18:
#         raise Exception ('Не подходите по возрасту!')
# except ValueError as t:
#     print(t)
# except (KeyboardInterrupt, EOFError) as e:
#     #print(type(e))
#     if type(e) == KeyboardInterrupt:
#         print('Вы прервали ввод')
#     else:
#         print('EOFError')
# except Exception as e:
#     print(e)
# finally:
#     print(" ---The end!!!---")
#===========================================

# Поднимаем исключение на уровень выше

# try:
#     n=1
#     try:
#         s = 'q'
#         s>1
#     except:
#         print('Inner')
#         raise Exception ("From inner")
#     finally:
#         print('Ok')
# except:
#     print('outer')
# finally:
#     print('The end')
#===========================================
# Как отлавливать исключния в функциях

def foo():
    www ='a'
    #raise Exception ('fooooo')
def bar():
    pass #1<'w'
    #raise Exception('baaaar')
def fn():
    pass

try:
    foo()
    bar()
    fn()

except:
    print("!!!")
