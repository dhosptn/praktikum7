import math
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))
