# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time


# Здесь пишем код
def func_log(file_log='log.txt'):
    '''
    Декоратор дозаписывает в файл имя вызываемой функции, дату и время вызова
    :param file_log: Путь до файла
    :return: Файл содержит в себе название и время вызова функции
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            run = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
            with open(file_log, encoding='utf-8', mode='a') as new_file:
                new_file.write(f'{func.__name__} вызвана {run}')
                new_file.close()
            return result
        return wrapper
    return decorator




@func_log()
def call():
    '''
    Функция вызова файла
    :return: После применения декоратора в файле указано время вызова
    '''
    with open('log.txt', mode='r') as file:
        file.read()
        file.close()
call()

