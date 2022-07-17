# 1. Ввести строку. Пройти в цикле по строке и вывести индексы символов строки.

# str_1 = input("Enter string: ")
# for i in range(len(str_1)):
#     print(i)

# 2. Ввести строку. Вывести символы строки и через тире - их индексы. Например, если введена строка "sky", вывести:

# str_2 = input("Enter string: ")
# for index,char in enumerate(str_2):
#     print(f"{char} - {index}")

# 3. Посчитайте количество заглавных букв в строке.

# count_upper_3 = 0
# str_3 = input("Enter string: ")
# for chart in str_3:
#     if chart.isupper():
#         count_upper_3 += 1
# print(count_upper_3)

# 4. Посчитайте общее количество гласных в строке (в верхнем и нижнем регистре).

# count_vowel_4 = 0
# str_4 = input("Enter string: ")
# for chart in str_4:
#     if chart in "euioaEUIOA":
#         count_vowel_4 += 1
# print(count_vowel_4)

# 5. Удвойте все символы строки (путем создания новой строки).

# str_5 = input("Enter string: ")
# new_str_5 = ""
# for chart in str_5:
#     new_str_5 = new_str_5 + chart * 2
# print(new_str_5)

# 6. Задайте строку с произвольным значением (например, "Python").
# Получите строку, в которой все буквы будут разделены пробелами ("P y t h o n").

# str_6 = input("Enter string: ")
# new_str_6 = ""
# for chart in str_6:
#     new_str_6 = new_str_6 + chart + " "
# print(new_str_6)

# 7. Вставьте пробелы после всех неалфавитных символов строки (путем создания новой строки).
# Например, s = "Bananas,2apples,sweets and 8plums". Получить "Bananas, 2 apples, sweets and 8 plums".

# str_7 = input("Enter string: ")
# new_str_7 = ""
# for chart in str_7:
#     if chart.isalpha():
#         new_str_7 = new_str_7 + chart
#     else:
#         new_str_7 = new_str_7 + chart + " "
# print(new_str_7)

# 8. Задайте строку с произвольным значением (например, "summer").
# Получите строку, в которой гласные буквы станут заглавными ("sUmmEr").

# str_8 = input("Enter string: ")
# new_str_8 = ""
# for chart in str_8:
#     if chart in "euioa":
#         new_str_8 = new_str_8 + chart.upper()
#     else:
#         new_str_8 = new_str_8 + chart
# print(new_str_8)

# 9. Дана строка.Замените все гласные буквы на символ "*".
# При решени задачи используйте цикл и метод replace.

# str_9 = input("Enter string: ")
# new_str_9 = ""
# for chart in "eioau":
#     new_str_9 = str_9.replace(chart, "*")   #.replace("i","*").replace("o","*").replace("a","*").replace("u","*")
#     str_9 = new_str_9
# print(new_str_9)

# 10. Дана строка. Удалите все гласные буквы в строке. При решени задачи используйте цикл и метод replace.

# str_10 = input("Enter string: ")
# new_str_10 = ""
# for chart in "eioau":
#     new_str_10 = str_10.replace(chart, "")   #.replace("i","*").replace("o","*").replace("a","*").replace("u","*")
#     str_10 = new_str_10
# print(new_str_10)

# 11. Дана строка. Получить две новые строки: одну - из символов с четными индексами, другую - из символов с нечетными индексами.
# Напримре, s = "separate". Новые строки: "sprt", "eaae".

# str_11 = input("Enter string: ")
# new_str_11_odd = ""
# new_str_11_even = ""
# for index, chart in enumerate(str_11):
#     if index % 2 == 0:
#         new_str_11_even = new_str_11_even + chart
#     else:
#         new_str_11_odd = new_str_11_odd + chart
# print(new_str_11_even)
# print(new_str_11_odd)

# 12. Ввести строку, включающую строчные и прописные буквы.
# Вывести ту же строку в одном регистре, который зависит от того, каких букв больше.
# При равном количестве преобразовать в нижний регистр.
# Например, вводится строка "HeLLo World", она должна быть преобразована в "hello world",
# потому что в исходной строке малых букв больше.

str_12 = input("Enter your string: ")
count_12_lowercase = 0
count_12_uppercase = 0
for chart in str_12:
    if chart.islower():
        count_12_lowercase += 1
    else:
        count_12_uppercase += 1
if count_12_lowercase >= count_12_uppercase:
    print(str_12.lower())
else:
    print(str_12.upper())