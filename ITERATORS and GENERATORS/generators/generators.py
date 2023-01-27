# generator functions are similar to regular functions but instead of return they use YIELD, and they return an ITERATOR

# def course_generator():
#   yield 'Computer Science'
#   yield 'Art'
#   yield 'Business'

# courses = course_generator()
# for course in courses:
#     print(course)

# will output
# Computer Science
# Art
# Business


# ---------- yield vs return

# def class_standing_generator():
#     yield 'Freshman'
#     yield 'Sophomore'
#     yield 'Junior'
#     yield 'Senior'
#
#
# class_standings = class_standing_generator()
# for standing in class_standings:
#     print(standing)


# ---------- next() and StopIteration

# def student_standing_generator():
#     student_standings = ['Freshman', 'Senior', 'Junior', 'Freshman']
#     for standing in student_standings:
#         if standing == "Freshman":
#             yield 500
#
#
# standing_values = student_standing_generator()
# print(next(standing_values))
# print(next(standing_values))


# ---------- Generator Expressions
#
# def cs_generator():
#     for i in range(1, 5):
#         yield "Computer Science " + str(i)
#
#
# cs_courses = cs_generator()
# for course in cs_courses:
#     print(course)
#
# cs_generator_exp = ("Computer Science " + str(i) for i in range(1, 5))  # a bit the same as
# for gen in cs_generator_exp:
#     print(gen)


# ---------- Generator Methods: send()
#
# def generator():
#     count = 0
#     while True:
#         n = yield count
#         if n is not None:
#             count = n
#         count += 1
#
#
# my_generator = generator()
# print(next(my_generator))  # Output: 0
# print(next(my_generator))  # Output: 1
# print(my_generator.send(3))  # Output: 4
# print(next(my_generator))  # Output: 5

# MAX_STUDENTS = 50
#
#
# def get_student_ids():
#     student_id = 1
#     while student_id <= MAX_STUDENTS:
#         # Write your code below
#         n = yield student_id
#         if n is not None:
#             student_id = n
#             continue
#         student_id += 1
#
#
# student_id_generator = get_student_ids()
# for i in student_id_generator:
#     # Write your code below
#     if i == 1 :
#         i = student_id_generator.send(25)
#     print(i)


# ---------- Generator Methods: throw()

# eg:
# def generator():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
#
# my_generator = generator()
# for item in my_generator:
#     if item == 3:
#         my_generator.throw(ValueError, "Bad value given")


# ---------- Connecting Generators

def science_students(x):
    for i in range(1, x + 1):
        yield i


def non_science_students(x, y):
    for i in range(x, y + 1):
        yield i


def combined_students():
    yield from science_students(5)
    yield from non_science_students(10, 15)
    yield from non_science_students(25, 30)


student_generator = combined_students()
for student in student_generator:
    print(student)
