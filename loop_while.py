# x = 0.2
# while x <= 3.5:
#     print(round(x,1))
#     x += 0.2

# Найдите сумму нечетных чисел от 5 до 41.
# x = 5
# s = 0
# while x <= 41:
#     print(x)
#     s = s + x
#     x += 2
# print(s)

# Найдите произведение чисел от -1 до -11.
# m = 1
# x = -1
# while x >= -11:
#     print("x= " +str(x))
#     print(m)
#     m *= x
#     x -= 1
# print(m)

# Постройте строку из 30 букв "z". Напечатайте полученную строку и ее длину.
# i = 1
# string = ""
# while i <= 30:
#     string = string + "z"
#     i += 1
# print(string + " " + str(len(string)))

# Постройте строку "1 sheep... 2 sheep... 3 sheep... ... 20 sheep... "
# i = 1
# string_1 = ""
# while i <= 20:
#     string_1 = string_1 + str(i) + " sheep... "
#     i += 1
# print(string_1)

# Постройте строку “1 monkey 2 monkeys ... 10 monkeys”.
# i = 1
# string_2 = ""
# while i <= 10:
#     if i == 1:
#         string_2 = string_2 + str(i) + " monkey "
#     else:
#         string_2 = string_2 + str(i) + " monkeys "
#     i += 1
# print(string_2)

# Составьте строку, которая "отсчитывает" секунды до старта ракеты: "10 seconds...9 seconds...8 seconds...7 seconds...6 seconds...5 seconds...4 seconds...3 seconds...2 seconds...1 second"
# i = 10
# string_3 = ""
# while i >= 1:
#     if i != 1:
#         string_3 = string_3 + str(i) + " seconds..."
#     else:
#         string_3 = string_3 + str(i) + " second..."
#     i -= 1
# print(string_3)

#В первый день тренировок спортсмен пробежал 5 км.
#В каждый последующий день он пробегал на 5% больше, чем в предыдущий день.
#Через сколько дней спортсмен будет пробегать более n км в день?

# first_day_distance = 5
# n = int(input("how mach distance you want to reach: "))
# day = 1
# while n > first_day_distance:
#     first_day_distance = first_day_distance + first_day_distance * 0.05
#     day += 1
#     print(day)
#     print(first_day_distance)
# print(day)

# Ученик к моменту начала обучения не знает ни одного английского слова.
# В первый день занятий он выучил 5 английских слов.
# В каждый последующий день он выучивал на 2 слова больше, чем в предыдущий.
# Через сколько дней ученик будет знать не менее n английских слов?
know_words = 0
count_days = 1
study_words_per_day = 5
n = int(input("how much do you want to know English words?"))
while n > know_words:
    count_days += 1
    know_words = know_words + study_words_per_day
    study_words_per_day += 2
print(" student need: " + str(count_days))
