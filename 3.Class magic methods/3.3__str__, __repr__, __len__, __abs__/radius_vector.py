class RadiusVector:
    def __init__(self, *args):
        self.coords = [0]*args[0] if len(args) == 1 else [*args]

    def set_coords(self, *coords):
        ln = len(coords) if len(self.coords) > len(coords) else len(self.coords)
        self.coords[:ln] = coords[:ln]

    def get_coords(self):
        return self.coords

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum([i**2 for i in self.coords])**0.5


# Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат). Объекты этого класса должны создаваться командами:

# # создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
# vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0

# # создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
# vector = RadiusVector(1, -5, 3.4, 10)
# То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора. Если же передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.

# Класс RadiusVector должен содержать методы:

# set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
# get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).

# Также с объектами класса RadiusVector должны поддерживаться следующие функции:

# len(vector) - возвращает число координат радиус-вектора (его размерность);
# abs(vector) - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ... + coord_N*coord_N) - корень квадратный из суммы квадратов координат).

# Пример использования класса RadiusVector (эти строчки в программе писать не нужно):

# vector3D = RadiusVector(3,2, 1)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(*(3, -5.6, 8, 10, 11)) # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D) # res_len = 3
# res_abs = abs(vector3D)
# P.S. На экран ничего выводить не нужно, только объявить класс RadiusVector