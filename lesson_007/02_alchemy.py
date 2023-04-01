# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код


class Water():
    def __init__(self):
        self.name = 'Water'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Air):
            sub = Storm()
        elif isinstance(other, Fire):
            sub = Steam()
        elif isinstance(other, Earth):
            sub = Dirt()
        else:
            sub = None

        return sub


class Fire():
    def __init__(self):
        self.name = 'Fire'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            sub = Steam()
        elif isinstance(other, Air):
            sub = Lighting()
        elif isinstance(other, Dirt):
            sub = Lava()
        else:
            sub = None

        return sub


class Air():

    def __init__(self):
        self.name = 'Air'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            sub = Storm()
        elif isinstance(other, Fire):
            sub = Lighting()
        elif isinstance(other, Dirt):
            sub = Dust()
        else:
            sub = None

        return sub


class Earth():
    def __init__(self):
        self.name = 'Earth'

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Water):
            sub = Dirt()
        elif isinstance(other, Air):
            sub = Dust()
        elif isinstance(other, Fire):
            sub = Lava()
        else:
            sub = None

        return sub


class Storm():
    name = 'Storm'

    def __str__(self):
        return self.name


class Steam():
    name = 'Steam'

    def __str__(self):
        return self.name


class Dirt():
    name = 'Dirt'

    def __str__(self):
        return self.name


class Lighting():
    name = 'Lighting'

    def __str__(self):
        return self.name


class Dust():
    name = 'Dust'

    def __str__(self):
        return self.name


class Lava():
    name = 'Lava'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())




# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
