# count = 0
# for x in range(101):
#     if x % 7 == 0:
#         count += 1
# print(count)

# 1. Найдите сумму чисел от 1 до 100

# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# 2. Найдите сумму нечетных чисел от 1 до 51.

# sum_1 = 0
# for i in range(1, 52, 2):
#     print(i)
#     sum_1 += i
# print(sum_1)

# 3. Найдите сумму четных чисел от 200 до 300.

# sum_2 = 0
# for i in range(200, 301, 2):
#     sum_2 += i
# print(sum_2)

# 4. Найдите количество чисел, кратных 3, в диапазоне от 0 до 1000.

# count_division_by_3 = 0
# for i in range(3,1001,3):
#     count_division_by_3 += 1
# print(count_division_by_3)
#
# count_division_by_3_1 = 0
# for i in range(1,1001):
#     if i % 3 == 0:
#         count_division_by_3_1 += 1
# print(count_division_by_3_1)

# 5. Найдите сумму четных чисел и количество нечетных чисел в диапазоне от 1 до 100.

# sum_5 = 0
# count_odd_number_5 = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum_5 += i
#     else:
#         count_odd_number_5 +=1
# print(sum_5)
# print(count_odd_number_5)

# 6. Найдите сумму четных чисел от n до k (n, k ввести с помощью input).

# n = int(input("Enter start of range: "))
# k = int(input("Enter end of range: "))
# sum_6 = 0
# for i in range(n, k+1):
#     if i % 2 == 0:
#         sum_6 += i
# print(sum_6)

# 7. Возведите число n в степень k, не используя операцию возведения в степень (n, k ввести с помощью input).
# Для того чтобы возвести число n в степень k, его необходимо k раз умножить на само себя.

# n = int(input("Enter number: "))
# k = int(input("Enter power: "))
# power_of_number = 1
# for i in range(1,k+1):
#     power_of_number = power_of_number * n
# print(power_of_number)

# 8. Найдите факториал числа 7. Факториал числа — это произведение натуральных чисел от 1 до самого числа (включая данное число).
# Обозначается факториал восклицательным знаком «!». Например, 5! = 1*2*3*4*5

# mult_8 = 1
# for i in range(1,8):
#     mult_8 *= i
# print(mult_8)
# print(1*2*3*4*5*6*7)

# 9. У Клавдии было 200 долларов. В первый день она купила конфет на сумму 3 доллара, во второй день - на 6 долларов,
# и каждый день сумма покупки увеличивалась на 3 доллара. Так она поступала 10 дней, пока не посмотрела на себя в зеркало.
# Сколько денег осталось у Клавдии после 10 покупок?

# money = 200
# for i in range(1, 11):
#     money = money - 3*i
#     print(money, i)
# print(money)

# 10. Напечатайте треугольник из звездочек. Количество линий ввеcти с помощью команды input.

# number_of_stars  = int(input("Enter number of stars in last line: "))
# for i in range(1, number_of_stars+1):
#     print("*"*i)

# 11. Получите строку, содержащую лесенку. Число «ступенек» ввести командой input.

# number_of_stairs  = int(input("Enter number of stairs: "))
# for i in range(1, number_of_stairs+1):
#     print(" "*i + "#")

# 12. Нарисуйте пирамиду. Число этажей ввести командой input. Используйте выравнивание строки по центру.

number_of_level  = int(input("Enter number of level: "))

for i in range(1, number_of_level+1,2):
    str_12 = "*"*i
    print(str_12.center(number_of_level+1))
