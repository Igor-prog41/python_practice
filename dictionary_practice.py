# dictionary
# 1. Создайте словарь с именем address, у которого есть ключи:
# "city" со значением "Miami", "state" со значением "FL", "country" со значением "USA".

address = {
    "city": "Miami",
    "state": "FL",
    "country": "USA"
}

# print(address)

# 2. Создайте словарь с именем user, у которого есть ключи: "name" со значением "Alice", "age" со значением 25,
# "is_adult" со значением True.

user = {
    "name": "Alice",
    "age": 25,
    "is_adult": True
}

# print(user)

# 3. Создайте словарь, содержащий перечень десяти ваших любимых фильмов (книг.)
# Ключи – названия фильмов или книг, значения – жанр фильма (книги).

list_of_book = {
    1: {
        "name": "Code: The Hidden Language of Computer Hardware and Software",
        "author": "Charles Petzold"
    },
    2: {
        "name": "Cracking the Coding Interview: 189 Programming Questions & Solutions",
        "author": "Gayle Laakmann McDowell"
    },
    3: {
        "name": "Code Complete",
        "author": "Steve McConnell"
    },
    4: {
        "name": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio and Aaron Courville"
    },
    5: {
        "name": "Clean Code: A Handbook of Agile Software Craftsmanship",
        "author": "Robert C. Martin"
    },
    6: {
        "name": "Grokking Algorithms",
        "author": "Aditya Y Bhargava"
    },
    7: {
        "name": "Dancing with Python: Learning to Code With Python and Quantum Computing",
        "author": "Robert S. Sutor"
    },
    8: {
        "name": "Coding: 3 Books in One",
        "author": "Michael Clark and Michael Learn"
    },
    9: {
        "name": "Haskell In-Depth",
        "author": "Vitaly Bragilevsky"
    },
    10: {
        "name": "Basic Concepts in Algorithms",
        "author": "Shmuel Tomi Klein"
    }
}

# print(list_of_book)


# 4. Создайте словари-карточки для фильмов (книг), в которых будет содержаться информация о конкретном фильме (книге)
# из вашего списка (название фильма (книги), год выпуска, название студии (издательства),
# зрительский (читательский) рейтинг и т. д.).


# 5. Создайте объект person, у которого есть ключи "name" со значением "Alice", "is_student" со значением True.
# Присвойте переменной first_name значение ключа "name" объекта person.

person = {
    "name": "Alice",
    "is_student": True
}
first_name = person["name"]
# print(first_name)

# 6.Добавьте в созданный вами перечень новых фильмов (книг) 2-3 новых элемента.

list_of_book[11] = {"name": "Make Your Own Neural Network", "author": "Tariq Rashid"}


print(list_of_book[11]["name"])

# 7.Создайте словарь animal, у которого есть свойство 'name' со значением 'bear'.
# Затем запишите команду, которая добавляет в словарь свойство 'class' со значением 'mammal'.

animal = {
    "name": "bear"
}
print(animal)

animal["class"] = "mammal"

print(animal)

# 8. Создайте словарь person, у которого есть свойство 'name' со значением 'Bob'.
# Затем запишите команду, которая добавляет в словарь свойство 'address' со значением 'Sacramento'.

new_person = {
    "name": "Bob"
}
print(new_person)
new_person["adrresr"] = "Sacramento"
print(new_person)

# 9. Создайте словарь student, содержащий элементы: "name" со значением "Peter",
# "school" со значением "PASV", "isAdult" со значением False.
# Затем запишите команду, которая удаляет элемент "isAdult".

student = {
    "name": "Peter",
    "school": "PASV",
    "isAdult": False
}
print(student)
del student["isAdult"]
print(student)


# 10.Создайте словарь car, имеющий свойства: "make" со значением "Ford", "model" со значением "Mustang",
# "year" со значением 2015. Затем запишите команду, которая удаляет элемент "year".

car = {
    "make": "Ford",
    "model": "Mustang",
    "year": 2015
}
print(car)
del car["year"]
print(car)

# 11. Словарь хранит информацию о запасах фруктов на складе. Определите, есть ли на складе апельсины ("orange")

fruits = {
  'apple': 40,
  'orange': 25,
  'mango': 50
}

print("orange" in fruits)
print("banana" in fruits)

# 12. Словарь хранит информацию о кинофильме. Определите, хранит ли словарь информацию о годе создания фильма ('year').

movie = {
  'name': 'Groundhog day',
  'type': 'comedy',
  'year': 1993,
}

print("year" in movie)
print("producer" in movie)

# 13. Словарь хранит информацию об отметках студента. Определите,
# хранит ли словарь информацию об успеваемости по математике ('math').

report = {
  'math': 5,
  'history': 4,
  'science': 5,
}

print("math" in report)

# 14. Словарь хранит информацию о запасах фруктов на складе.
# Получите список ключей, список значений и список всех элементов словаря.

fruits_list = {
    'apple': 40,
    'orange': 25,
    'mango': 50,
    'banana': 85
}

print(fruits_list.keys())
fruits_keys = list(fruits_list.keys())
print(fruits_keys)

print(fruits_list.values())
fruits_values = list(fruits_list.values())
print(fruits_values)

print("**********************")
print(fruits_list)
print(fruits_list.items())
fruits_items = list(fruits_list.items())
print(fruits_items)
print(type(fruits_items[1]))


# 15.Создайте словарь, содержащий перечень десяти ваших любимых фильмов (книг.).
# Напечатайте перечень всех элементов словаря, пройдя по нему циклом for.

for element in list_of_book:
    print(list_of_book[element]["author"])

# 16. ания
# Заполните словарь, содержащий имена студентов и их рейтинг (количество баллов за решенные задачи).
# Информацию ввести в цикле с помощью команды input.

student_dictionary = {}
number_of_student = int(input("Enter number of student: "))
for i in range(1, number_of_student + 1):
    name = input(f"Enter name of {i} student: ")
    score = input(f"Enter score of {i} student: ")
    student_dictionary[name] = score
print(student_dictionary)
