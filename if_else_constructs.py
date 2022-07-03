# char = input("type your chart :")
# if char in "euoaiEUIOA":
#     print(f"{char} is vowel")
# else:
#     print(f"{char} is not vowel")
#
# answer = input("Are you ok? :")
# if answer == "no" or answer == "No":
#     print("Get better!")
# else:
#     print("Cool")
# a = float(input("input number \"a\""))
# b = float(input("input number \"b\""))
# if a % b == 0:
#  print(f"{a} is division by {b}")
# else:
#  print(f"{a} is not division by {b}")
# name = input("input name :")
# time = int(input("input time in hours:"))
# if time >= 0 and time <= 6:
#  print(f"Good night {name}!")
# elif time >= 7 and time <=12:
#  print(f"Good morning {name}!")
# elif time >= 13 and time <= 18:
#  print(f"Good day {name}!")
# elif time >= 19 and time <= 24:
#  print(f"Good evening {name}!")
# else:
#  print(f"Wrong time!")
# a = float(input("input number \"a\" :"))
# b = float(input("input number \"b\" :"))
# operation = input("input simbol of operation (+, -, *, /, %, //):")
# if operation == "+":
#  result = a + b
#  print(f"{a} {operation} {b} = {result}")
# elif operation == "-":
#  result = a - b
#  print(f"{a} {operation} {b} = {result}")
# elif operation == "*":
#  result = a * b
#  print(f"{a} {operation} {b} = {result}")
# elif operation == "/":
#  result = a / b
#  print(f"{a} {operation} {b} = {result}")
# elif operation == "%6":
#  result = a % b
#  print(f"{a} {operation} {b} = {result}")
# elif operation == "//":
#  result = a // b
#  print(f"{a} {operation} {b} = {result}")
# else:
#  print("unknown operator")
# price = float(input("input price of goods :"))
# if price >= 300:
#  print(f"your final prise is :{price-price*0.3} $")
# elif price >= 200:
#  print(f"your final prise is :{price - price * 0.2} $")
# elif price >= 100:
#  print(f"your final prise is :{price-price*0.1} $")
# else:
#  print(f"your final prise is :{price} $")
# age = int(input("print your age :"))
# if age < 16:
#     print("you are children")
# elif age < 50:
#     print("you are men")
# else:
#     print("you are senior")

current_color = input("введите цвет сигнала светофора ('red','yellow','green') :")
if current_color == "red":
    print("next color is green")
elif current_color == "yellow":
    print("next color is red")
else:
    print("next color is yellow")