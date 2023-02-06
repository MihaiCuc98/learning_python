# __________ Inheritance_________
# class Employee:
#     new_id = 1
#
#     def __init__(self):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#
#     def say_id(self):
#         print("My id is {id}".format(id=self.id))
#
#
# class Admin(Employee):
#     def say_id(self):
#         super().say_id()
#         print("this works!")
#
#
# class Manager(Admin):
#     def say_id(self):
#         super().say_id()
#         print("I am in charge!")
#
#
# e1 = Employee()
# e2 = Employee()
# e3 = Admin()
# e4 = Manager()
# e3.say_id()
# e4.say_id()
# print("----------")
# objects = [Employee(), Admin(), Manager()]
# for item in objects:
#     item.say_id()
# ______________Polymorphism_________
# posibilitatea de a utiliza aceeasi metoda pe mai multe tipuri de date

# ________________Dunder Methods__________
# class Employee():
#     new_id = 1
#
#     def __init__(self):
#         self.id = Employee.new_id
#         Employee.new_id += 1
#
#
# class Meeting:
#     dff = [1, 2, 3]
#
#     def __init__(self):
#         self.attendees = []
#
#     def __add__(self, employee):
#         print("ID {} added.".format(employee.id))
#         self.attendees.append(employee)
#
#     def __len__(self):
#         return len(self.attendees)
#
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
# m1 = Meeting()
# m2 = Meeting()
# m3 = Meeting()
# m1 + e1
# m1 + e2
# m1 + e3
# print(len(m1))

# _______________ Abstraction
# from abc import ABC, abstractmethod
#
#
# class AbstractEmployee(ABC):
#     new_id = 1
#
#     def __init__(self):
#         self.id = AbstractEmployee.new_id
#         AbstractEmployee.new_id += 1
#
#     @abstractmethod
#     def say_id(self):
#         pass
#
#
# # Write your code below
# class Employee(AbstractEmployee):
#     def say_id(self):
#         print("Hoau bau: " + str(self.id))
#
#     pass
#
#
# e1 = Employee()
# e1.say_id()

# ______________ Getters, Setters and Deleters _________________
# class Employee():
#   new_id = 1
#   def __init__(self, name=None):
#     self.id = Employee.new_id
#     Employee.new_id += 1
#     self._name = name
#
#   # Write your code below
#   def get_name(self):
#     return self._name
#   def set_name(self, new_name):
#     if isinstance(new_name, str):
#       self._name = new_name
#     else:
#       raise TypeError
# def delete_name(self):
#     del self._name
#
#
# e1 = Employee("Mihai")
# e2 = Employee()
# print(e1.get_name())
# e1.set_name("Valentin")
# print(e1.get_name())
# print(e1.get_name())

# e2.set_name("Iuli")
# print(e2.get_name())

# e2.del_name()
# print(e2.get_name())


# __________________ CodeCademy example
# from abc import ABC, abstractmethod
#
#
# class AbstractEmployee(ABC):
#     new_id = 1
#
#     def __init__(self):
#         self.id = AbstractEmployee.new_id
#         AbstractEmployee.new_id += 1
#
#     @abstractmethod
#     def say_id(self):
#         pass
#
#
# class User:
#     def __init__(self):
#         self._username = None
#
#     @property
#     def username(self):
#         return self._username
#
#     @username.setter
#     def username(self, new_name):
#         self._username = new_name
#
#
# class Meeting:
#     def __init__(self):
#         self.attendees = []
#
#     def __add__(self, employee):
#         print("{} added.".format(employee.username))
#         self.attendees.append(employee.username)
#
#     def __len__(self):
#         return len(self.attendees)
#
#
# class Employee(AbstractEmployee, User):
#     def __init__(self, username):
#         super().__init__()
#         User.__init__(self)
#         self.username = username
#
#     def say_id(self):
#         print("My id is {}".format(self.id))
#
#     def say_username(self):
#         print("My username is {}".format(self.username))

# ___________Review exercise ___________
# class School:
#     def __init__(self, name, level, numberOfStudents):
#         self.name = name
#         self.level = level
#         self.numberOfStudents = numberOfStudents
#
#     def get_name(self):
#         return self.name
#
#     def get_level(self):
#         return self.level
#
#     def get_numberOfStudents(self):
#         return self.numberOfStudents
#
#     def set_numberOfStudents(self, number):
#         if isinstance(number, int):
#             self.numberOfStudents = number
#         else:
#             raise TypeError
#
#     def __repr__(self):
#         return "A {level} school named {name} with {numberOfStudents} students".format(level=self.level, name=self.name,
#                                                                                        numberOfStudents=self.numberOfStudents)
#
#
# class PrimarySchool(School):
#     def __init__(self, name, level, pickupPolicy: str):
#         super().__init__(name, level, 19)
#         self.pickupPolicy = pickupPolicy
#         self.interesting_thing = None
#
#     def get_pickupPolicy(self):
#         return self.pickupPolicy
#
#     def set_interesting(self, interesting):
#         self.interesting_thing = interesting
#
#     def __repr__(self):
#         inherited_repr = super().__repr__()
#         return inherited_repr + "-------{pickupPolicy}------{interesting}".format(pickupPolicy=self.pickupPolicy, interesting = self.interesting_thing)
#     def set_pickupPolicy(self):
#         return self.pickupPolicy
#
# first_school = School("Mihai Viteazul", "middle", 30)
# first_school.set_numberOfStudents(100)
# print(first_school.get_level())
# print(first_school)
# primary_school = PrimarySchool("cristi", "primary", "No")
# primary_school.set_interesting("du-te ma")
# print(primary_school)


# ____________ property() Python function _________
class Box:
    def __init__(self, weight):
        self.__weight = weight

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        if weight >= 0:
            self.__weight = weight

    def delWeight(self):
        del self.__weight

    weight = property(getWeight, setWeight, delWeight, "Docstring for the 'weight' property")


box = Box(100)
print(box.weight)
box.weight = 200
print(box.weight)
del box.weight

# _________ Benefits:_______
# 1. We can now use the weight attribute as if it was public. We no longer have to call
# the setters, getters, and deleter methods directly and thus giving our program a simpler syntax.
# 2. Even though we
# no longer call the methods directly, we still can maintain constraints such as the weight limit in setWeight().
# It’s the best of both worlds!
# 3. If we had a huge codebase that used our methods multiple times in multiple places,
# a single change to the method name would seriously mess up our program since we would have to change it everywhere!
# We no longer have this issue using the property() method since we never call it directly.


# ___________ another way to use the property function -> decorators! _______

    # @property
    # def weight(self):
    #     """Docstring for the 'weight' property"""
    #     return self.__weight
    #
    # @weight.setter
    # def weight(self, weight):
    #     if weight >= 0:
    #         self.__weight = weight
    #
    # @weight.deleter
    # def weight(self):
    #     del self.__weight
