# 1. Создайте список, заполненный десятью нулями: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list_1 = []
for i in range(1, 10):
    list_1.append("0")
print(list_1)

# 2. Создайте список из 10 первых натуральных чисел: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

list_2 = list(range(1, 11))
print(list_2)

# 3. Создайте список из 10 первых четных чисел: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18].

list_3 = list(range(0, 19, 2))
print(list_3)

# 4. Создайте список из 10 первых нечетных чисел: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].

list_4 = list(range(1, 20, 2))
print(list_4)

# 5. Создайте список, содержащий десять чисел, являющихся степенями числа 2: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512].

list_5 = []
for i in range(0, 10):
    list_5.append(2**i)
print(list_5)

# 6. Введите строку. Получите список из слов строки, которые начинаются с гласной буквы.

random_str = "Free online letter shuffler. Just load your letters and they will automatically get rearranged."
list_of_words = random_str.split()
list_6 = []
for word in list_of_words:
    if word[0] in "euioa":
        list_6.append(word)
print(list_6)

# 7. Задан список, хранящий значение температуры в градусах Цельсия.
arr_7 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# Получите список, содержащий значения температуры в градусах Фаренгейта.
# (0 °C × 9/5) + 32 = 32 °F


def celsius_to_fahrenheit(celsius_list):
    list_out = []
    for temperature_celsius in celsius_list:
        temperature_fahrenheit = round(temperature_celsius * 5 / 9 + 32, 2)
        list_out.append(temperature_fahrenheit)
    return list_out


print(celsius_to_fahrenheit(arr_7))


# 8. Заполните список 10 числами Фибоначчи. Первые два числа этой последовательности равны 0 и 1.
# А каждое следующее число, начиная с третьего, равно сумме двух предыдущих чисел: [0, 1, 1, 2, 3, 5, 8, 13, 21, 44]


def list_numbers_fibonatch(how_many_numbers):
    list_out = [0, 1]
    for index in range(2, how_many_numbers):
        list_out.append(list_out[index - 1] + list_out[index - 2])
    return list_out


print(list_numbers_fibonatch(10))
