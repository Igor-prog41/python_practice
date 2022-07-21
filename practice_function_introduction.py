# import math

# 1. Напишите функцию с именем greet, которая возвращает фразу "Hello world!"


def greet():
    return "Hello world!!"

print(greet())
print(greet())

# 2. Напишите функцию с именем hello_user, которая принимает имя name в качестве параметра
# и возвращает фразу "Hello name" (вместо name должно быть имя, переданное в функцию в качестве параметра).

def greet_2(name_2):
    return "Hello " + name_2 + "!!!"
name = input("Enter name: ")
print(greet_2(name))

# 3. Напишите функцию с именем say_hello, которая принимает два строковых параметра (name и time).
# Time может быть "morning", "afternoon", "evening" или "night".
# Функция должна возвращать приветствие пользователя по имени
# в зависимости от времени суток: "Good" + time + name (например, "Good evening Samanta!"

name_3_1 = input("Enter name: ")
time_3_1 = input("Enter \"morning\", \"afternoon\", \"evening\" or \"night\": ")
def greet_3(name_3, time_3):
    return "Good " + time_3 + " " + name_3 + "!"

print(greet_3(name_3_1, time_3_1))

# 4. Напишите функцию с именем product, которая принимает три параметра (числа) и возвращает их произведение.

def product(num1, num2, num3):
    return num1 * num2 * num3

print(product(45,85,56))

# 5. Напишите функцию с именем opposite, которая принимает число и возвращает противоположное по значению число.

num_5 = int(input("Enter number: "))
def opposite(num1):
    return -num1

print(opposite(num_5))

# 6. Напишите функцию distance_from_origin, которая принимает два числа x,y (координаты точки на плоскости)
# и возвращает расстояние от этой точки до начала координат.


def distance_from_origin(x, y):
    # return math.sqrt(x * x + y * y)
    return (x * x + y * y) ** 0.5


print(round(distance_from_origin(45, 78), 2))
print(distance_from_origin(45, 78))


# 7. Напишите функцию distance, которая принимает четыре аргумента: x1, y1 (координаты первой точки на плоскости) и
# x2, y2 (координаты второй точки на плоскости) и возвращает расстояние между точками.
# Расстояние между точками (x1, y1) и (x2, y2) равно ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5.


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(round(distance(11,25,86,89), 2))

# 8.Напишите функцию percentage, которая принимает два аргумента: number и percent и возвращает процент от числа.

def percentage(number, percent):
    return number / 100 * percent


print(percentage(233000, 5)/12)

# 9. Индекс массы тела рассчитывается путем деления массы тела (в килограммах) на квадрат роста (в метрах квадратных).
# Напишите функцию body_mass_index, которая принимает два аргумента: weight и height и возвращает индекс массы тела.


def body_mass_index(weight, height):
    return weight / height ** 2


print(round(body_mass_index(86, 1.77), 2))

# 10. Напишите функцию average, которая принимает два числа: a и b и возвращает среднее арифметическое этих чисел.


def average(a, b):
    return (a + b) / 2

print (average(45, 85))

# 11. Напишите функцию geometric_mean, которая принимает два числа: num1 и num2 и
# возвращает среднее геометрическое этих чисел. Чтобы найти среднее геометрическое двух чисел,
# нужно перемножить эти числа и извлечь из них корень.


def geometric_mean(num1, num2):
    return (num1 * num2) ** 0.5


print(round(geometric_mean(10, 10), 2))
print(round(geometric_mean(100, 10), 2))
print(round(geometric_mean(2, 10), 2))

# 12. Сумма углов n-угольника равна 180 * (n − 2). Напишите функцию angles_of_polygon,
# которая принимает аргумент n (число углов) и возвращает сумму углов n-угольника.


def angles_of_polygon(n):
    return (n - 2) * 180


print(angles_of_polygon(4))

# 13. Напишите функцию с именем miles_to_feet, которая принимает число miles (количество миль)
# в качестве аргумента и возвращает это расстояние в футах. 1 миля = 5280 футов.


def miles_to_feet(miles):
    return miles * 5280


print(miles_to_feet(10))

# 14. Напишите функцию с именем centigrade, которая принимает значение температуры в градусах Фаренгейта tempF
# в качестве аргумента и возвращает значение температуры в градусах Цельсия.


def centigrade(tempf):
    return (tempf - 32) * 5 / 9


print(round(centigrade(400), 2))

# 15. Напишите функцию с именем fahrenheit, которая принимает значение температуры в градусах Цельсия tempС
# в качестве аргумента и возвращает значение температуры в градусах Фаренгейта.


def fahrenheit(tempc):
    return tempc * 9 / 5 + 32


print(round(fahrenheit(204.44), 2))
