import itertools

# this is the way in which you can crete a custom iterable class

# class CustomerCounter:
#     def __iter__(self):
#         self.count = 0
#         return self
#     def __next__(self):
#         self.count +=1
#         if self.count >100:
#           raise StopIteration
#         return self.count
# customer_counter = CustomerCounter()
# for counter in customer_counter:
#   print(counter)

#another example:
# class FishInventory:
#     def __init__(self, fishList):
#         self.available_fish = fishList
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index < len(self.available_fish):
#             fish_status = self.available_fish[self.index] + " is available!"
#             self.index += 1
#             return fish_status
#         else:
#             raise StopIteration

# Infinite Iterator: Count
# max_capacity = 1000
# num_bags = 0
#
# for nr in itertools.count(start=13.5, step = 13.5):
#   if nr >= max_capacity:
#     break
#   num_bags +=1
#   print(num_bags)


# Input-Dependent Iterator: Chain
# great_dane_foods = [2439176, 3174521, 3560031]
# min_pin_pup_foods = [6821904, 3302083]
# pawsome_pup_foods = [9664865]
#
# # Write your code below:
# all_skus_iterator = itertools.chain(great_dane_foods,min_pin_pup_foods,pawsome_pup_foods)
#
# for iterator in all_skus_iterator:
#   print(iterator)


# Combinatoric Iterator: Combinations

# collars = ["Red-S", "Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

# collar_combo_iterator = itertools.combinations(collars, 3)
# lala = list(collar_combo_iterator)
# print(lala)
# print(len(lala))

# for collar in lala:
#     print(collar)

# OR
# interesting thing with the memory
# once you printed the iterator, it will be clean from the memory

# for collar in collar_combo_iterator:
#     print(collar)
#

# Review
# 1. Using the iter() funtion to create an iterator.
# 2. Using the next() function to manually iterate over an iterator.
# 3. How for loops use iterables and iterators.
# 4. How to write custom iterators by implementing the __iter__() and __next__() methods.
# 5. How to use built-in itertools including count(), chain() and combinations().

# max_money = 15
# options = []
# cat_toys = [("laser", 1.99), ("fountain", 5.99), ("scratcher", 10.99), ("catnip", 15.99)]
# cat_toy_iterator = iter(cat_toys)
# for i in range(len(cat_toys)):
#     print(next(cat_toy_iterator))
# toy_combos = itertools.combinations(cat_toys, 2)
# for combo in toy_combos:
#    toy1 = combo[0]
#    cost_of_toy1 = toy1[1]
#    toy2 = combo[1]
#    cost_of_toy2 = toy2[1]
#    if cost_of_toy1 + cost_of_toy2 <= max_money:
#       options.append(combo)
# print(options)
