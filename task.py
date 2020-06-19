import copy

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
people = [
    {'name': 'Dobri', 'age': 33, 'hobbies': ['gaming', 'trekking']},
    {'name': 'Jenya', 'age': 28, 'hobbies': ['reading', 'films']}
]

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
people_names_list = [person['name'] for person in people]
print(people_names_list)
# 3) Use a list comprehension to check whether all persons are older than 20.

condition = all([person['age']> 20 for person in people])
print(condition)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
copied_list = copy.deepcopy(people)

# 5) Unpack the persons of the original list into different variables and output these variables.
person_1, person_2 = people
print(person_1)
print(person_2)



# # 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#
#     def describe(self):
#         print(f"This is {self.name}, which is a {self.kind} food")
#
# f = Food('Pizza', 'Italian')
# f.describe()
# # # 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
# class Food:
#     @staticmethod
#     def describe(name, kind):
#         print(f"This is {name}, which is a {kind}")
#
# f = Food()
# f.describe('Pizza', 'Italian')
#
# class Food:
#     name = 'Spagetthi'
#     kind = "Pasta"
#
#     @classmethod
#     def describe(cls):
#         print(f"This is {cls.name}, which is a {cls.kind}")
#
# f = Food()
# f.describe()
# # # 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
#
# class Meat(Food):
#     def __init__(self, name, kind):
#         super().__init__(name, kind)
#
#     def cook(self):
#         print(f'Cooking {self.name}')
#
#
# class Fruit(Food):
#     def __init__(self, name, kind):
#         super().__init__(name, kind)
#
#     def clean(self):
#         print(f'Cleaning {self.name}')
#
#
# m = Meat('Meatball', 'Balkan')
# f = Fruit('Orange', 'Citrus')
# m.cook()
# f.clean()
#
#
# # # 4) Overwrite a “dunder” method to be able to print your “Food” class.
#
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#
#     def __repr__(self):
#         return f"This food is {self.name}, which is {self.kind}. It's delicious"
#
#     def describe(self):
#         print(f"This is {self.name}, which is a {self.kind} food")
#
#
#
# f = Food('Pizza', 'Italian')
# print(f)