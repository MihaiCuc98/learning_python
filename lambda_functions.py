from functools import reduce

# Documentation:
# 1. The map() function applies a passed function to each element in an iterable and returns a map
# object.
# 2. The filter() function applies a filtering function (a function that returns a boolean) to each element
# in an iterable. filter() returns a filter object with only the elements for which the filtering function returned
# True.
# 3. reduce() must be imported from the functools module. It reduces an iterable to a single value by
# cumulatively applying a passed function to the first pair of elements in the iterable and then each sequential
# element with the return value.

list_items = [2, 4, 1, 2.3, 4, 5, 6, .6, 7]
dic_items = {
    "first_item": .3,
    "second_item": 10,
    "third_item": 3
}


def multiply_with_10(number):
    return number * 10


def divide_by_9(number):
    return number / 9


# _________map()_function examples _________
example_1 = list(map(lambda item: item * 2, list_items))
print("Example 1: " + str(example_1))

example_2 = dict(map(lambda item: (item[0], item[1] + 10), dic_items.items()))
print("Example 2: " + str(example_2))

example_3 = dict(map(lambda item: (item[0], multiply_with_10(item[1])), dic_items.items()))
print("Example 3: " + str(example_3))

example_4 = list(map(lambda item: format(divide_by_9(item), '.2f') if item > 5 else item, list_items))
print("Example 4: " + str(example_4))

# _________filter()_function examples________
books = [["Burgess", 1985],
         ["Orwell", "Nineteen Eighty-four"],
         ["Murakami", "1Q85"],
         ["Orwell", 1984],
         ["Burgess", "Nineteen Eighty-five"],
         ["Murakami", 1985]]
# aici trebuie sa te gandesti ca fiecare lista din lista e un item, iar ca sa accesezi ultimul item
# trebuie sa pui [1]
filtered_books = list(filter(lambda item: type(item[1]) == str, books))
print("Filtered books: " + str(filtered_books))

letters = ['r', 'e', 'd', 'u', 'c', 'e']

word = str(reduce(lambda x, y: str(x + y), letters))
print(word)


# __________Decorators_______________
# Decorators are special functions which we can use to add functionality to an existing function

def get_name_and_age_in_10_years(age_function):
    def printing_things(*args):  # this is necessary for using the function with arguments
        print("Mihai will gonna be: ")
        age_function(*args)
        print("old in 10 years")

    return printing_things


@get_name_and_age_in_10_years
def age_in_10_years(age):
    print(age + 10)


age_in_10_years(40)



