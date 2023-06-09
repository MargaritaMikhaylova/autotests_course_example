# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generate_random_name():
    while True:
        letters = string.ascii_lowercase
        first_part = ''
        second_part = ''
        for i in range(random.randint(1, 15)):
            first_part += ''.join(random.choice(letters))
        for i in range(random.randint(1, 15)):
            second_part += ''.join(random.choice(letters))
        yield first_part + ' ' + second_part


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Здесь пишем код
