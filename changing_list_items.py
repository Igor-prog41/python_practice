# Changing, adding, inserting list items
# 1. Дан список чисел. Замените все элементы списка на противоположные по знаку элементы.

arr_1 = [5, 9, 89, -45, 0, 894, -56]


def reversal_of_sign_numbers_in_list(arr_in):
    out_arr = []
    for i in range(0, len(arr_in)):
        out_arr.append(-arr_in[i])
    return out_arr


print(reversal_of_sign_numbers_in_list(arr_1))

# 2.Дан список чисел. Все четные элементы замените нулем, а нечетные увеличьте на 1.
arr_2 = [5, 9, 89, -45, 0, 894, -56]


def changing_list_according_rules(arr_in):
    for i in range(0, len(arr_in)):
        if i % 2 == 0:
            arr_in[i] = 0
        else:
            arr_in[i] = arr_in[i] + 1
    return arr_in


print(changing_list_according_rules(arr_2))
print(arr_2)


# 3. Дан числовой список . Элементы с четными индексами возвести в квадрат, а элементы с нечетными индексами - в куб.
arr_3 = [5, 9, 89, -45, 0, 894, -56]


def changing_list_according_rules(arr_in):
    for i in range(0, len(arr_in)):
        if i % 2 == 0:
            arr_in[i] = arr_in[i] ** 2
        else:
            arr_in[i] = arr_in[i] ** 3
    return arr_in


print(changing_list_according_rules(arr_3))
print(arr_3)

# 4. Дан смешанный список . Получить массив чисел.
arr_4 = [False, 45, 'srting', 89.34, 'hahaha', True]


def number_list_from_list(arr_in):
    arr_out = []
    for el in arr_in:
        if type(el) == int or type(el) == float:
            arr_out.append(el)
    return arr_out


print(number_list_from_list(arr_4))

# 5. Дан список слов. Отфильтровать список , получив список слов, которые начинаются с гласной буквы.
str_5 = "We use cookies to remember your preferences and to analyze our traffic"
arr_5 = str_5.split(" ")


def list_word_that_start_with_vowels(arr_in):
    list_out = []
    for word in arr_in:
        if word[0] in "eioau":
            list_out.append(word)
    return list_out


print(list_word_that_start_with_vowels(arr_5))

# 6. Дан список целых чисел. Получить список четных чисел.
list_6 = [5, 9, 89, -45, 0, 894, -56]


def numbers_list_to_even_numbers_list(list_in):
    list_out = []
    for number in list_in:
        if number % 2 == 0:
            list_out.append(number)
    return list_out


print(numbers_list_to_even_numbers_list(list_6))

# 7. Дан список целых чисел. Получить список чисел, которые имеют четное число цифр.
list_7 = [5, 9, 89, 45, 0, 894, 56, 45668, 588996]


def numbers_list_to_even_number_of_digits_list(list_in):
    list_out = []
    for number in list_in:
        if len(str(number)) % 2 == 0:
            list_out.append(number)
    return list_out


print(numbers_list_to_even_number_of_digits_list(list_7))


# 8. Дан числовой список . Получить список чисел, которые являются квадратами целых чисел.
# Например, arr = [4, 1, 2, 9, 16, 13, 36]. Получить список [4, 1, 9, 16, 36].
list_8 = [4, 1, 2, 9, 16, 13, 36]


def list_number_power_2(list_in):
    list_out = []
    for number in list_in:
        if number ** 0.5 == round(number ** 0.5):
            list_out.append(number)
    return list_out


print(list_number_power_2(list_8))   # [4, 1, 9, 16, 36]

# 9.Дано два списка одинаковой размерности: arr1 = [1, 2, 3, 4, 5, 6], arr2 = ["a", "b", "с", "d", "e", "f"].
# Получить список : arr3 = [1, "a", 2, "b", 3, "с", 4, "d", 5, "e", 6, "f"]
list_9_1 = [1, 2, 3, 4, 5, 6]
list_9_2 = ["a", "b", "с", "d", "e", "f"]


def concatenation_of_two_lists(list_1, list_2):
    list_out = []
    if len(list_1) == len(list_2):
        for i in range(0, len(list_1)):
            list_out.extend([list_1[i], list_2[i]])
    else:
        list_out.append("list is not equal")
    return list_out


print(concatenation_of_two_lists(list_9_1, list_9_2))  #[1, "a", 2, "b", 3, "с", 4, "d", 5, "e", 6, "f"]

# 10. Дан список слов. Найти максимальную и минимальную длину слов.
str_10 = "We use cookies to remember your preferences and to analyze our traffic a"
list_10 = str_10.split(" ")


def min_and_max_in_list(list_in):
    max_in_list = len(list_in[0])
    min_in_list = len(list_in[0])
    for word in list_in:
        if len(word) > max_in_list:
            max_in_list = len(word)
        if len(word) < min_in_list:
            min_in_list = len(word)
    return [max_in_list, min_in_list]


print(min_and_max_in_list(list_10))


# 11. Дан список слов. Вывести слово максимальной длины.
str_11 = "We use cookies to remember your preferences and to analyze our traffic a"
list_11 = str_11.split(" ")


def word_max_long_in_list(list_in):
    max_in_list = list_in[0]
    for word in list_in:
        if len(word) > len(max_in_list):
            max_in_list = word
    return max_in_list


print(word_max_long_in_list(list_11))


# 12. Дан список слов. Получить среднюю длину слова (среднее арифметическое длин слов).
str_12 = "We use cookies to remember your preferences and to analyze our traffic a"
list_12 = str_12.split(" ")


def average_words_in_list(list_in):
    average_word = 0
    for word in list_in:
        average_word += len(word)
    return round(average_word/len(list_in), 2)


print(average_words_in_list(list_12))
