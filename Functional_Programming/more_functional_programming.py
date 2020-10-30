# filter(function, values)

numbers = [5, 18, 7, 9, 14, 6, 1]

# predicate function
def greater_than_eight(number):
    return number >= 8

def mystery_function(number):
    return number % 2 == 1

results = list(filter(mystery_function, numbers))
print(results)





# reduce(function, values)

from functools import reduce


def adder(a, b):
    print("Received a:", a, "b:", b)
    return a + b

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -20]

answer = reduce(adder, values)
print(answer)






# Partial functions
from functools import partial

# partial() converts other functions to smaller, partial functions

add_5 = partial(adder, 5)
add_7 = partial(adder, 7)


print(add_5(12))
print(add_7(19))




x = int("11010", base=2)
print(x, type(x))

# base =10
# 1000   100   10     1
#    1     3    7     2
# 1*1000 + 3*100 + 7*10 + 2*1

# base 7
# 343    49     7      1
#   2     0     3      4  == 733
#  2*343 + 0*49 + 3*7 + 4*1

# base 2
#  16    8    4    2    1
#   1    1    0    1    0  == 26

_11010 = partial(int, "11010")
print(_11010(base=36))

binary = partial(int, base=2)
hexadecimal = partial(int, base=16)
print(binary("1010110110011100"))

print(adder)
print(hexadecimal("0x000002CBF1AFD5E0"))

print("\n\n\n\n\n")


import math
from random import randint

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

player = [4, 4]
enemies = [[randint(-50, 50), randint(-50, 50)] for _ in range(20)]

# Imperative
print("Imperative")
closest = 999999
closest_enemy = None
for enemy in enemies:
    d = distance(player, enemy)
    if d < closest:
        closest = d
        closest_enemy = enemy
print(closest_enemy, closest)

# Functional
print("Functional")

distance_from_player = partial(distance, player)
closest = min(enemies, key=distance_from_player)
enemies_by_distance = sorted(enemies, key=distance_from_player, reverse=True)

print(enemies_by_distance)





# pipelines

def pipeline(list_of_functions, starting_data):
    def apply(data, function):
        return function(data)
    
    result = reduce(apply, list_of_functions, starting_data)
    return result

functions = [str.upper, reversed, list]
data = "hello world"

result = pipeline(functions, data)
print(result)