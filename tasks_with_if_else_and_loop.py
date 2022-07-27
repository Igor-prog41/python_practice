def power_of_3(n):
    while n > 1:
        # print(n)
        n = n / 3
    return n == 1


print(power_of_3(27))   # True
print(power_of_3(25))   # False


def descending_order(num):
    out = []
    s = list(str(num))
    for k in range(0, len(s)):
        index = 0
        num_big = int(s[index])
        for i in range(0, len(s)):
            if int(s[i]) > num_big:
                index = i
                num_big = int(s[i])
        out.append(s[index])
        s.pop(index)
    return int("".join(out))


print(descending_order(12333455))

# Best practice
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


# 1. Внесите изменение в решение задачи из примера 4, применив встроенные функции max и min.
# Пример 4. Напишите функцию, которая принимает 2 числа a, b и возвращает сумму чисел от a до b,
# если a < b, и сумму чисел от b до a, если b < a.


def get_sum(a, b):
    s = 0
    for i in range(min(a, b), max(a, b) + 1):
        s += i
    return s


print(get_sum(5, 10))
print(get_sum(5, 2))


# 2.Напишите функцию с именем summation, которая принимает неотрицательное число n
# и возвращает сумму чисел от 1 до n: 1 + 2 + 3 + ... + n.


def summation(n):
    sum_2 = 0
    for i in range(1, n + 1):
        sum_2 += i
    return sum_2


print(summation(5))
print(summation(15))
print(summation(25))


# 3. Напишите функцию describesNumber, которая принимает аргумент number и возвращает описание числа:
# "Even positive number", "Even negative number", "Odd positive number", "Odd negative number", "Zero". Примеры:
#
#
# функция describesNumber(48) должна возвратить "Even positive number";
# функция describesNumber(-12) должна возвратить "Even negative number";
# функция describesNumber(51) должна возвратить "Odd positive number";
# функция describesNumber(-5) должна возвратить "Odd negative number";
# функция describesNumber(0) должна возвратить "Zero".


def describesNumber(n):
    if n == 0:
        return "Zero"
    else:
        if n % 2 == 0:
            out = "Even"
        else:
            out = "Odd"
        if n > 0:
            out += " positive number"
        else:
            out += " negative number"
        return out

print(describesNumber(48))
print(describesNumber(-12))
print(describesNumber(51))
print(describesNumber(-5))
print(describesNumber(0))

# 4. Напишите функцию, которая принимает число и определяет, является ли число степенью числа 5.
# если число не является степенью числа 5, возвратить False. Иначе возвратить, какой степенью является число.
# Например, для числа 100 возвратить False, так как 100 не является степенью числа 5.
# Для числа 125 возвратить 3, так как 5 ** 3 = 125.


def is_power_of_5(n):
    out_4 = 0
    while n > 1:
        n = n / 5
        out_4 += 1
    if n == 1:
        return out_4
    else:
        return False


print(is_power_of_5(100))
print(is_power_of_5(125))
print(is_power_of_5(625))

# 5.Напишите функцию, которая принимает число n и возвращает количество делителей этого числа.
# Например, число 10 имеет 5 делителей : 1, 2, 5, 10. Число 12 имеет 6 делителей: 1, 2, 3, 4, 6, 12.


def number_divisor(n):
    out_5 = []
    for i in range(1, n + 1):
        if n % i == 0:
            out_5.append(i)
    return out_5


print(number_divisor(10))
print(number_divisor(12))
print(number_divisor(20))

# 6. Напишите функцию, которая принимает число n и определяет.является ли число простым.
# Простое число - это число, у которого нет других делителей, кроме 1 и самого числа.
# Числа 0 и 1 не являются простыми. Пример простых чисел: 2, 3, 5, 7, 11, 13, 17, 19...


def is_number_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_number_prime(1))
print(is_number_prime(2))
print(is_number_prime(5))
print(is_number_prime(7))
print(is_number_prime(6))