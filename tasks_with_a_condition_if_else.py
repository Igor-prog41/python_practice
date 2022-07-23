# 1.Напишите функцию, которая принимает число number и возвращает "Even",
# если число четное, или "Odd", если число нечетное.


def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"


print(even_or_odd(45))
print(even_or_odd(40))
print(even_or_odd(-45))
print(even_or_odd(0))

# 2.Число считается счастливым, если оно делится на 9. Напишите функцию lucky_number,
# которая принимает число и возвращает True, если число является счастливым, или False - в противном случае.


def lucky_number(num):
    return True if num % 9 == 0 else False


print(lucky_number(9))
print(lucky_number(7))
print(lucky_number(19))


# 3. Напишите функцию с именем negative, которая принимает число и возвращает его отрицательным.
# Если число является отрицательным, то возвращается само число.


def negative(num):
    if num <= 0:
        return num
    else:
        return -num


print(negative(5))
print(negative(-5))
print(negative(0))


# 4. Функция принимает числа a, b и операцию operation (+,-,*,/,%,//) и
# возвращает результат выполнения этой операции над числами a, b.


def f_4(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "%": return a % b
    elif operation == "//": return a // b


print(f_4(45, 8, "//"))

# 5. Функция принимает длину length и ширину width 4-угольника. 4-угольник может быть квадратом или прямоугольником.
# Если это квадрат, возвратить его площадь. Если это прямоугольник, возвратить его периметр.


def area_or_perimeter(length, width):
    if length == width:
        return length * width
    else:
        return length * 2 + width * 2


print(area_or_perimeter(10, 10))
# print(area_or_perimeter(10, 11))

# 6. Функция принимает числа x и y. Возвратить True, если число x делится на число y.


def full_separation(x, y):
    return True if x % y == 0 else False


print(full_separation(4, 2))
print(full_separation(5, 2))

# 7. Функция принимает числа n, a, b. Возвратить True, если число n делится на оба числа a и b.

def full_separation_2_num(n, a, b):
    return True if n % a == 0 and n % b == 0 else False


print(full_separation_2_num(15, 2, 1))
print(full_separation_2_num(52, 2, 1))

# 8. Функция принимает три числа a, b, c. Возвратить True, если существует треугольник со сторонами a, b, c,
# и False, в противном случае.

#
def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and c + b > a else False


print(is_triangle(3, 4, 5))
print(is_triangle(333, 4, 5))

# 9. Напишите функцию с именем final_grade, которая вычисляет финальную отметку студента.
# Отметка зависит от двух параметров: отметки за экзамен exam_grade и числа выполненных проектов projects.
# Функция принимает два параметра exam_grade (число от 0 to 100) и projects - число проектов (число >=0).
# Функция возвращает число final grade, которая вычисляется по следующим правилам:
# 100, если отметка за экзамен больше 90 или если число выполненных проектов больше 10.
# 90, если отметка за экзамен больше 75 и если число выполненных проектов минимум 5.
# 75, если отметка за экзамен больше 50 и если число выполненных проектов минимум 2.
# 0, в других случаях.


def final_grade(exam_grade, projects):
    if exam_grade > 90 or projects >10:
        return 100
    elif exam_grade > 75 and projects >= 5:
        return 90
    elif exam_grade > 50 and  projects >= 2:
        return 75
    else:
        return 0


print(final_grade(95, 7))
print(final_grade(85, 11))
print(final_grade(80, 6))
print(final_grade(51, 4))
print(final_grade(40, 7))

# 10. Напишите функцию, которая вычисляет финальную зарплату.
# Функция принимает два параметра: : salary (целое число), bonus(булевая величина).
# Если bonus имеет значение True, зарплата умножается на 5. Если bonus имеет значение False, вы получаете только salary.

def final_salary(salary, bonus):
    return salary * 5 if bonus else salary


print(final_salary(500, False))
print(final_salary(500, True))

# 11. Напишите функцию sale_cakes, которая принимает n - число пирожных, которые собирается купить покупатель.
# В зависимости от числа покупаемых пирожных магазин делает скидки. Полная цена одного пирожного равна 100 центов.
# Если число пирожных n < 5, скидки нет и вы платите полную стоимость покупки.
# Если n>=5 and n<10, то за одно пирожное вы платите 95 центов. Если вы покупаете пирожных n>=10,
# то за одно пирожное вы платите 90 центов. Функция должна возвратить общую стоимость вашей покупки.


def sale_cakes(n):
    if n < 5:
        return n * 100
    elif n < 10:
        return n * 95
    else:
        return n * 90


print(sale_cakes(1))
print(sale_cakes(5))
print(sale_cakes(10))
print(sale_cakes(15))

# 12.Напишите функцию planet_name, которая принимает n - номер планеты от Солнца и возвращает name - название планеты:
# n = 1: name = "Mercury"
# n = 2: name = "Venus"
# n = 3: name = "Earth"
# n = 4: name = "Mars"
# n = 5: name = "Jupiter"
# n = 6: name = "Saturn"
# n = 7: name = "Uranus"
# n = 8: name = "Neptune"


def planet_name(n):
    return planet_name_list[n]


planet_name_list = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"
}
n = int(input("Enter number of planet: "))
print(planet_name(n))

# 13. Функция принимает три отметки s1, s2, s3 (каждая отметка - число от 0 до 100).
# Функция находит средний балл ученика score и возвращает буквенное значение финального балла:
# если 90 <= score <= 100, возвратить 'A';
# если 80 <= score < 90, возвратить 'B';
# если 70 <= score < 80, возвратить 'C';
# если 60 <= score < 70, возвратить 'D';
# если 0 <= score < 60, возвратить 'F'.


def average_score(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score >= 0 and score < 60:
        return "F"
    else:
        return "ERROR something wrong!!!"


print(average_score(95, 86, 71))
print(average_score(55, 46, 71))
print(average_score(95, 99, 91))
print(average_score(195, 186, 171))

# 14.Напишите функцию, которая принимает два параметра weightи height.
# Функция вычисляет индекс массы тела bmi по формуле: bmi = weight / height ** 2 и возвращает описание результата:
# если bmi <= 18.5, возвратить "Underweight";
# если bmi <= 25.0, возвратить "Normal";
# если bmi <= 30.0, возвратить "Overweight";
# если bmi > 30 , возвратить"Obese".


def bmi_score(weight, height):
    bmi = round(weight / height ** 2, 2)
    if bmi <= 18.5:
        return "Underweight - tonkiy " + str(bmi)
    elif bmi <= 25.0:
        return "Normal " + str(bmi)
    elif bmi <= 30.0:
        return "Overweight " + str(bmi)
    elif bmi > 3:
        return "Obese " + str(bmi)


print(bmi_score(85, 1.77))
print(bmi_score(55, 1.67))
print(bmi_score(59, 1.78))

# 15. Напишите функцию, которая принимает возраст человека age и возвращает описание возраста:
# если age <= 12, возвратить "You're a kid"
# если age между 13 и 17 (включительно), возвратить"You're a teenager"
# если age между 18 и 64 (включительно), возвратить"You're an adult"
# если age >= 65, возвратить "You're an elderly".


def person_age(age):
    if age <= 12:
        return "You're a kid"
    elif 12 < age <= 17:
        return "You're a teenager"
    elif 18 < age <= 64:
        return "You're an adult"
    elif age > 64:
        return "You're an elderly"
    else:
        return "ERROR something wrong!!!"


your_age = int(input("Enter your age: "))
print(person_age(your_age))


# 16. Напишите функцию, которая принимает цифру от 0 до 9 и возвращает это значение словами:
# 0 - zero, 1 - one, 2 - two, 3 - three, 4 - four, 5 - five, 6 - six, 7 - seven, 8 - eight, 9 - nine.

def write_a_number(num):
    if num == 0:
        return "zero"
    elif num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    else:
        return "ERROR something wrong!!!"


num_16 = int(input("Enter your number: "))
print(write_a_number(num_16))

# 17. Напишите функцию square_of_triangle, которая принимает три аргумента a, b, c (стороны треугольника) и
# возвращает площадь треугольника, если треугольник существует, или сообщение "The triangle does not exist",
# в противном случае. Площадь треугольника находится по формуле
# Герона: area = (p * (p - a) * (p - b) * (p - c)) ** 0.5, где p = (a + b + c) / 2.


def square_of_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
    else:
        return "The triangle does not exist"


print(square_of_triangle(3, 4, 5))
print(square_of_triangle(103, 4, 5))