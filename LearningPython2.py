# import random
#
# s1 = random.randrange(1,10) # генерация случайного числа от 1 до 9
# s2 = random.randrange(5) # генерация случайного числа от 0 до 4
#print(s1, s2)
# while True:
#     answer = input('введите положительное число либо с точкой: ')
#     test = answer.replace('.', '', 1)
#
#     if not test.isdigit():
#         print('нужно ввести целое положительное число либо с точкой')
#     else:
#         break
# if answer == test:
#     answer = int(answer)
#     print('Это число ', answer)
# else:
#     answer = float(answer)
#     print("а это float", answer)
#======================================
# Угадай число

import random
i=0
num = random.randrange(10)
while True:
    answer = input('Введите целое число ')
    if not answer.isdigit():
        print('Нужно ввести целое число')
        continue
    answer = int(answer)
    if num > answer:
        print('Число больше')
    elif num < answer:
        print('Число меньше')
    else:
        print('Угадано')
        break



