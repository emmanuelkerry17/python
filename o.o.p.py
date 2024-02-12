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


class people:

    def __init__(self,Age,name,email):
        self.Age =Age
        self.name =name
        self.email =email
Age=int(input("age: "))
name = input("name: ")
email = input("email: ")
# person1 = people(name="Griffindor",Age=34,email="yahoo")
# peron2 = people(name="Tristan", Age=24,email="gmail")
# person3 = people(name="Richie",Age=45,email="gmail")

# print(f"my name is {person1.name}  am {person1.Age} years old and my email service is {person1.email}")
print(f"my name is {name} i am {Age} years old and my email service is {email} ")