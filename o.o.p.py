# class Person:
#     def __init__(self):
#         self.name = "Jack"
#         self.id = 48532
#         self.age = 55
#         self.residence = "Nakuru"
# person = Person()
# person.name = "Doby"
# person.age = 78
#
# print(f"my name is {person.name} and am a {person.age} year old residing in {person.residence} my ID number is {person.id}")


class People:

    def __init__(self,age, name, email):
        self.age = age
        self.name = name
        self.email = email


age = int(input("Age: "))
name = input("name: ")
email = input("email: ")
# person1 = People(name="Griffindor",age=34,email="yahoo")
# peron2 = People(name="Tristan", age=24,email="gmail")
# person3 = People(name="Richie",age=45,email="gmail")

# print(f"my name is {person1.name}  am {person1.age} years old and my email service is {person1.email}")
print(f"my name is {name} i am {age} years old and my email service is {email} ")