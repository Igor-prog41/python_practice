# c = ""
# while c != "=":
#     text = input("Enter your text: ")
#     c = input("Enter your cart: ")
#     print(text.count(c))

# chart = ""
# while chart != "=":
#     string = input("enter your string: ")
#     chart = input("enter your chart: ")
#     length_string = len(string)
#     print(round(string.count(chart)/length_string * 100,2))

# text = "If you want to be somebody, somebody really special, be yourself."
# count_o = text.count("o")
# count_e = text.count("e")
# if count_e > count_o:
#     print("e " * count_e)
# else:
#     print("o " * count_o)

# first_name = input("enter your firstname: ")
# last_name = input("enter your lastname: ")
# midlle_name = input("enter your midllename: ")
# max_string = int(max(len(first_name),len(last_name),len(midlle_name)))
# print(first_name.rjust(max_string))
# print(last_name.rjust(max_string))
# print(midlle_name.rjust(max_string))

# word = input("enter your word: ")
# width = int(input("Enter your width: "))
# if width + 2 < len(word):
#     print("Error")
# else:
#     print("*" * width)
#     print("*" + word.center(width-2) + "*")
#     print("*" * width)

# animal = input("Enter aanimal name: ")
# tail = input("Enter tail: ")
# print(animal.endswith(tail))

# greet = input("Enter your greet: ")
# print( greet.startswith("Hello"))

# name = input("Enter your name: ")
# if name[0] in "EUOIA":
#     print(f"{name}, your name starts with vowel")
# else:
#     print(f"{name}, your name starts with consonant")
#
# string = input("Enter your string: ")
# word = input("Enter your word: ")
# print(string[len(string)-1] in "0123456789")
# print("Yes" if "y" in string else "No" + "  \"y\" in this string")
# print(str(word in string) + " your word in your string")

# str = "     anna vova kolia      "

# count_left_space = 0
# end_of_look_for = True
# i = len(str)-1
# while end_of_look_for:
#     if str[i] == " ":
#         count_left_space += 1
#         i -= 1
#     else:
#         end_of_look_for = False
# print(str.strip().title() + "!" * count_left_space)
# print(count_left_space)

# string_10 = "Summer is my favorite time of year"
# print(string_10.replace("Summer", "Winter"))

# s = "we like python"
# print(s.replace("e", "").replace("u", "").replace("i", "").replace("o", "").replace("a", ""))

string_11 = input("Enter your string: ")
old_word = input("Enter word what you want to change: ")
new_word = input("Enter new word what you want to change: ")
print(string_11.replace(old_word, new_word))
