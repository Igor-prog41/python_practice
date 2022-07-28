# 1. Напишите функцию, которая принимает строку из строчных и прописных букв и возвращает строку,
# в которой строчные буквы стали прописными, а прописными - строчными ("Sky IS BluE" ---> "sKY is bLUe").


def str_revers_case(str_1):
    return str_1.swapcase()


print(str_revers_case("Sky IS BluE"))

# 2. Напишите функцию, которая принимает строку текста, записанного в стиле "kebab-case" и возвращает строку,
# записанную в стиле "snake_case" ("number-of-people-of-the-city" ---> "number_of_people_of_the_city")


def srt_to_snake_case(str_2):
    return str_2.replace("-", "_")


print(srt_to_snake_case("number-of-people-of-the-city"))


# 3. Напишите функцию, которая принимает строку, состоящую из букв и цифр,
# и возвращает количество цифр в этой строке ("Today is 31 of December of 2020" ---> 6)


def count_number(str_3):
    count = 0
    for chart in str_3:
        if chart in "0123456789":
            count += 1
    return count


print(count_number("Today is 31 of December of 2020"))

# 4. Напишите функцию, которая принимает строку, состоящую из 10 цифр,
# и возвращает строку в формате телефонного номера ("1234567890" ---> "+(123) 456-78-90")


def str_to_phone(str_4):
    return f"+({str_4[0]}{str_4[1]}{str_4[2]}) {str_4[3]}{str_4[4]}{str_4[5]}-{str_4[6]}{str_4[7]}-{str_4[8]}{str_4[9]}"


print(str_to_phone("1234567890"))

# 5. Напишите функцию, которая принимает строку, и возвращает строку,
# в которой удалены все гласные буквы ("summer" ---> "smmr")
# (путем построения новой строки, в которую войдут все буквы, кроме гласных).


def str_without_vowels(str_5):
    out_5 = ""
    for chart in str_5:
        if chart in "euioa":
            pass
        else:
            out_5 += chart
    return out_5


print(str_without_vowels("summer"))
