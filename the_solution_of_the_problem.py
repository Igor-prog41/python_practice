# Напишите алгоритм выравнивания текста. Задана последовательность слов и целое число k длина строки,
# верните список строк, которые представляют каждую строку, полностью выровненную.
# В частности, в каждой строке должно быть как можно больше слов. Между каждым словом должен быть хотя бы один пробел.
# При необходимости добавьте лишние пробелы, чтобы каждая строка имела длину равную k.
# Пространства следует распределять как можно более равномерно, а дополнительные места, если таковые имеются,
# распределять, начиная с левой стороны.
# Если вы можете уместить только одно слово в строке, вы должны заполнить правую часть пробелами.
# Гарантируется, что каждое слово не длиннее k. Например, учитывая список слов
# [“the”, “quick”, “brown”, “fox”, “jumps”, “over”, “the”, “lazy”, “dog”] и k = 16, вы должны вернуть следующее:
# [“the quick brown”, “fox jumps over”, “the  lazy  dog”]



example_list = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
max_length_of_string = 16


def to_list_aligned_string(list_in, length_of_string):
    list_out = []
    funded_string = []
    for word in list_in:
        funded_string.append(word)
        if len(" ".join(funded_string))> length_of_string:
            extra_word = funded_string.pop()
            list_out.append(add_escapes(funded_string, length_of_string))
            funded_string = [extra_word]
    list_out.append(add_escapes(funded_string, length_of_string))
    return list_out


def add_escapes(list_words_in, max_length_of_string_in):
    count_escapes = max_length_of_string_in - len(" ".join(list_words_in))
    print(count_escapes)
    i = 0
    while count_escapes > 0:
        list_words_in[i] += " "
        count_escapes -= 1
        i += 1
        if len(list_words_in) == 1 or i == len(list_words_in) - 1:
            i = 0
    return " ".join(list_words_in)


# print(add_escapes(["the", "quick", "brown"], 16))
print(to_list_aligned_string(example_list, max_length_of_string))