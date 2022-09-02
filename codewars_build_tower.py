# codewars 6 kyu
# Build Tower
# Build a pyramid-shaped tower given a positive integer number of floors.
# A tower block is represented with "*" character.

def tower_builder(n_floors):
    list_out = []
    last_str_length = n_floors * 2 - 1
    for i in range(0, n_floors):
        list_out.append(("*" * i + "*" + "*" * i).center(last_str_length))
    return list_out


print(tower_builder(5))
