list_num = [-1, 5, -1, 856, -1, 600523, -10, 8]


# 1. Дан список, содержащий числа. Найти сумму элементов списка.


def sum_of_list_elements(arr_in):
    sum_of_element = 0
    for el in arr_in:
        sum_of_element += el
    return sum_of_element


print(sum_of_list_elements(list_num))

# 2. Найти сумму четных элементов списка.


def sum_of_even_elements_list(arr_in):
    sum_of_element = 0
    for i in range(0, len(arr_in)):
        if i % 2 == 0:
            sum_of_element += arr_in[i]
    return sum_of_element


print(sum_of_even_elements_list(list_num))

# 3.Найти произведение нечетных элементов списка.


def sum_of_odd_elements_list(arr_in):
    sum_of_element = 0
    for i in range(0, len(arr_in)):
        if i % 2 != 0:
            sum_of_element += arr_in[i]
    return sum_of_element


print(sum_of_odd_elements_list(list_num))

# 4.Найти среднее арифметическое элементов списка.


def average_elements_list(arr_in):
    sum_of_element = 0
    for i in range(0, len(arr_in)):
        sum_of_element += arr_in[i]
    return sum_of_element/len(arr_in)


print(average_elements_list(list_num))

# 5. Найти количество отрицательных элементов списка.


def count_negative_number_in_list(arr_in):
    count_elements = 0
    for index, element in enumerate(arr_in):
        if element < 0:
            count_elements += 1
    return count_elements


print(count_negative_number_in_list(list_num))

# 6. Найти количество элементов списка, кратных 5.


def count_numbers_multiples_of_5_in_list(arr_in):
    count_elements = 0
    for element in arr_in:
        if element % 5 == 0:
            count_elements += 1
    return count_elements


print(count_numbers_multiples_of_5_in_list(list_num))


# 7. Найдите количество четных положительных элементов списка.


def count_numbers_even_and_positive_in_list(arr_in):
    count_elements = 0
    for element in arr_in:
        if element % 2 == 0 and element > 0:
            count_elements += 1
    return count_elements

print(count_numbers_even_and_positive_in_list(list_num))

# 8. Дан список, содержащий слова.
arr_8 = ["apple", "apricot", "pineapple", "banana", "grape", "plum", "aaaaa"]
# Найдите количество слов длиной 5.


def count_words_with_length_5_in_list(arr_in):
    count_element = 0
    for element in arr_in:
        if len(element) == 5:
            count_element += 1
    return count_element


print(count_words_with_length_5_in_list(arr_8))

# 9.Дан список, содержащий слова.
arr_9 = ["apple", "appricot", "pineapple", "banana", "grape", "orange", "uuuu",]
# Найдите количество слов, которые начинаются с гласной буквы


def count_words_words_that_start_with_vowel_in_list(arr_in):
    count_element = 0
    for element in arr_in:
        if element[0] in "euoai":
            count_element += 1
    return count_element


print(count_words_words_that_start_with_vowel_in_list(arr_9))

# 10. Дан список, содержащий слова.
arr_10 = ["apple", "appricot", "pineapple", "banana", "grape", "plum", "kiwi"]
# Найдите количество слов, которые содержат букву "a".

def count_words_words_that_has__a__in_list(arr_in):
    count_element = 0
    for element in arr_in:
        if "a" in element:
            count_element += 1
    return count_element


print(count_words_words_that_has__a__in_list(arr_10))