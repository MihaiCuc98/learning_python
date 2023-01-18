def createStudent(name, age, grades = []):
    return {
        "name": name,
        "age": age,
        "grades": grades

    }


chrisley = createStudent("Chrisley", 15)
dallas = createStudent('Dallas', 16)


def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])


addGrade(chrisley, 90)
addGrade(dallas, 100)
print(id(chrisley['grades']))
print(id(dallas['grades']))
print("---------------------------------")

age = 27
def func():
    age = 70
    def inner_func():
        global age
        print(age)

    inner_func()
func()

print ("----------")

def first_function(height):
    def second_function(var1, var2):
        return var1 * height * var2
    return second_function
result = first_function(20)
print(result(1,2))

print ("----------")
prices = [1,2,3,4,3,2,1,3,3]
def add_tax(price):
    return price + price*.2


def add_bill(price):
    return price*2


def return_result(funcione, list_arg: list):
    new_list=[]
    for i in list_arg:
        total = funcione(i)
        new_list.append("Ia aci:{nr}".format(nr=total))
    return new_list


print(return_result(add_bill, prices))

print("-----------Map built-in  higher-order function-------------")
int_list = [2, 3, 1, 3, 10]
doubled = map(lambda inp: inp * 2, int_list)
print(list(doubled))

list_items_to_double = [2,2,2,2,2]
def double_function(thing):
    return thing*2
result_double = map(double_function, list_items_to_double)
print(result_double)





print("-----------Coding question-------------")
# Say we stored our course grades in a list,
# but some of the grades were on a four-point scale and
# others were on a 100-point scale. To get all
# the grades on the same scale, try using a lambda
# function with the map() function to multiply just
# the grades on the four-point scale by 25 to get all
# of the grades on the same 100-point-scale.


grade_dict = {
    "one":3.5,
    "two":3.7,
    "three": 2.6,
    "four":95,
    "five":87}

# Your code below:
# assign the result of your map function to the variable grades_100scale
grades_100scale = dict(map(lambda raspuns: (raspuns[0] + "dadada", add_tax(raspuns[1])) if type(raspuns[1]) is float else raspuns,
                           grade_dict.items()))
# convert grades_100scale to a list and save it as updated_grade_list
updated_grade_dict = grades_100scale
# print updated_grade_list
print(grades_100scale)



