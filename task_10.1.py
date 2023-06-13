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
# Здесь пишем код

# gen = str
def generate_random_name():
    def generate_name():
        return ''.join(random.sample(string.ascii_letters, random.randint(1, 15)))
    while True:
        yield f'{generate_name()} {generate_name()}'

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))