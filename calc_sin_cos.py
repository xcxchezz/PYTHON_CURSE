import math
from typing import Dict, Any


sinu_col = {math.sin(math.pi / 2): '1',
            math.sin(math.pi / 3): '(3**0.5)/2',
            math.sin(math.pi / 4): '(2**0.5)/2',
            math.sin(math.pi / 6): '1/2'}

cosinus_col = {math.cos(math.pi / 2): '0',
               math.cos(math.pi / 3): '1/2',
               math.cos(math.pi / 4): '(2**0.5)/2',
               math.cos(math.pi / 6): '(3**0.5)/2'}


def cos_found(cosinus_col=cosinus_col, *args):
    n = int(input('Введите n(x = cos(pi/n): '))
    res_cos = math.cos(math.pi / n)
    for i in cosinus_col:
        if i == res_cos:
            print(cosinus_col.get(res_cos))
        else:
            continue


def sin_found(*args):
    n = int(input('Введите n(x = sin(pi/n): '))
    res_sin = math.sin(math.pi / n)
    for k in sinu_col:
        if k == res_sin:
            print(sinu_col.get(res_sin))
        else:
            continue


def start_prog():
    while True:
        choice = str(input('Что вы хотите вычислить sin или cos?(радианы): '))
        if choice == 'cos':
            cos_found()
        elif choice == 'sin':
            sin_found()
        else:
            print("Некоректный ввод, введите 'sin' или 'cos'")
            return


while 1 == 1:
    start_prog()
