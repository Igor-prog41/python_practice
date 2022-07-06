# description = "Email name recommendation"
# print("*"*20+"   "+description.upper()+"   "+"*"*20)
# str = (input("your lastname and firstname through space :"))
# index_of_space = str.index(' ')
# last_name = str[0:index_of_space]
# first_name = str[index_of_space+1:len(str)]
# print(f"{last_name}.{first_name}@gmail.com")
# print(description.center(100, '-'))
# print(str.index(' '))

# time = input("enter time (in the format 12:15:20) : ")
# hour = int(time[0:2])
# minutes = int(time[3:5])
# second = int(time[6:8])
# print(hour*60*60+minutes*60+second)

# str = input("enter string: ")
# print(f"has only letters :{str.isalpha()}") if str.isalpha() else 0
# print(f"has only digits :{str.isdigit()}") if str.isdigit() else False
# print(f"has only digits and letters :{str.isalnum()}") if str.isalnum() else False
# print(f"has only lowercase letters :{str.islower()}") if str.islower() else False
# print(f"has only uppercase letters :{str.isupper()}") if str.isupper() else False
# print(f"has digits and lowercase letters :{str.isdigit() and str.islower}") if str.isdigit() and str.islower else False
# print(f"has digits and uppercase letters :{str.isdigit() and str.isupper}") if str.isdigit() and str.isupper else False

# word ="programmer"
# print(word.find("r"))
# print(word.rfind("r"))
# s = input("enter string: ")
# n = int(input("enter index: "))
# print(s[n]*n)

# full_name = input("enter full name Through space: ")
# index_of_space = full_name.find(" ")
# first_name = full_name[0:index_of_space]
# last_name = full_name[index_of_space+1:len(full_name)]
# print(first_name)
# print(last_name)

# string = input("enter two words through space: ")
# index_of_space = string.find(" ")
# first_word = string[0:index_of_space]
# second_word = string[index_of_space+1:len(string)]
# print(second_word + " " + first_word)

# phrase = (input("enter three words through space: "))
# index_of_first_space = phrase.find(" ")
# index_of_second_space = phrase.rfind(" ")
# first_word = phrase[0:index_of_first_space]
# second_word = phrase[index_of_first_space + 1:index_of_second_space]
# third_word = phrase[index_of_second_space + 1:len(phrase)]
# print(f"{third_word} {second_word} {first_word}")

# text = input("nter three words through space: ")
# index_of_first_space = text.find(" ")
# index_of_second_space = text.rfind(" ")
# second_word = text[index_of_first_space + 1:index_of_second_space]
# revers_second_word = second_word[::-1]
# print(revers_second_word)

phrase = "My eyes are green too!"
color_eye = input("What is your favorite color? ")
index_word_green = phrase.find("green")
index_of_last_space = phrase.rfind(" ")
phrase_first_part = phrase[0:index_word_green-1]
phrase_last_part = phrase[index_of_last_space + 1:len(phrase)]
print(f"{phrase_first_part} {color_eye} {phrase_last_part}")