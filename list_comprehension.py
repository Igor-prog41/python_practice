# List comprehension
# 1. Дан массив чисел. Оставить в списке только положительные числа.
list_numbers = [5, 56, -78, -5, 516, 581, 892, -7, 0]

def list_with_positiv_namber(list_in):
    return [number for number in list_in if number > 0]


print(list_with_positiv_namber(list_numbers))

# 2. Дан массив чисел. Оставить в списке только нечетные числа.


def list_with_odd_number(list_in):
    return [number for number in list_in if number % 2 != 0]


print(list_with_odd_number(list_numbers))

# 3. Дан массив имен. Оставить в списке только имена начинающиеся с гласной буквы.

names = ['Alice', 'Anna', 'Bob', 'Elizabeth']


def list_names_start_with_vowels(list_in):
    return [name for name in list_in if name[0] in "AEUOI"]


print(list_names_start_with_vowels(names))

# 4. Дана строка. Найти количество гласных букв в этой строке
# (получите массив из гласных букв и найдите длину этого массива).

random_string = "Function returns The item with the highest value, Or the item with the Highest value in an iterable."


def count_vowels_in_string(str_in):
    list_of_chart = list(str_in)
    return len([chart for chart in list_of_chart if chart in "EUIOAeuioa"])


print(len(random_string))
print(count_vowels_in_string(random_string))

# 5. Дан массив. Найти сумму положительных элементов массива.


def sum_of_positive_number_of_list(list_in):
    list_positive_number = [number for number in list_in if number > 0]
    return sum(list_positive_number)


print(sum_of_positive_number_of_list(list_numbers))

# 6. Дан массив. Найти количество четных элементов массива.


def count_even_numbers_in_list(list_in):
    return len([num for num in list_in if num % 2 == 0])


print(count_even_numbers_in_list(list_numbers))

# 7. Дан массив. Найти сумму отрицательных элементов массива.


def sum_negative_elements_of_list(list_in):
    return sum([num for num in list_in if num < 0])


print(sum_negative_elements_of_list(list_numbers))

# 8. Дан массив. Получить массив из квадратов элементов исходного массива.


def list_square_number(list_in):
    return [num * num for num in list_in]


print(list_square_number(list_numbers))

# 9. Дано число. Найти сумму его цифр (превратить число в строку, построить массив из цифр,
# преобразовать каждую цифру в число, найти сумму элементов полученного массива).


def sum_digits_of_number(number_in):
    list_of_digits = list(str(number_in))
    return sum([int(digit) for digit in list_of_digits])


print(sum_digits_of_number(565212556))

# 10. Дан массив слов. Оставить только слова, начинающиеся с заглавной буквы.


def list_words_start_capital_letter(list_in):
    return [word for word in list_in if word[0].isupper()]


list_words = random_string.split()
print(list_words_start_capital_letter(list_words))

# 11. Дан массив слов. Получить массив длин этих слов.


def list_length_of_words(list_in):
    return [len(word) for word in list_in]


print(list_length_of_words(list_words))

# 12. Дан массив слов. Получить массив из слов, которые имеют четную длину.


def list_words_with_event_length_of_chart(list_in):
    return[word for word in list_in if len(word) % 2 == 0]


print(list_words_with_event_length_of_chart(list_words))

# 13. Дан смешанный массив, состоящий из чисел, строк, булевых значений. Оставить в массиве только числа.

mixed_list = ["vova", 45, 45, "Anna", True, "lee", False, 569]


def list_of_number(list_in):
    return [el for el in list_in if str(el).isdigit()]


print(list_of_number(mixed_list))

# 14. Дан массив чисел. Четные элементы удвоить, нечетные утроить.


def list_in_special_order(list_in):
    return [number * 2 if i % 2 == 0 else number * 3 for i, number in enumerate(list_in)]


print(list_in_special_order(list_numbers))

# 15. Дан строка из слов, разделенных пробелами. Перевернуть все слова из текста, если их длина >= 5,
# остальные слова не изменять. Получить новую строку.


def change_string_in_special_order(str_in):
    list_of_words = str_in.split()
    list_in_order = [word[::-1] if len(word) >= 5 else word for i, word in enumerate(list_of_words) ]
    return " ".join(list_in_order)


print(change_string_in_special_order(random_string))

# 16. Дан массив чисел. Удвоить четные элементы, утроить нечетные для всех положительных элементов массива.
list_of_number_16 = [1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1]


def change_list_of_number_in_special_order(list_in):
    return [(num*2 if i % 2 == 0 else num * 3) if num > 0 else num * 0 for i, num in enumerate(list_in) ]


print(change_list_of_number_in_special_order(list_of_number_16))