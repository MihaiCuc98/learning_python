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


# Infinite Iterator: Count
# max_capacity = 1000
# num_bags = 0
#
# for nr in itertools.count(start=13.5, step = 13.5):
#   if nr >= max_capacity:
#     break
#   num_bags +=1
#   print(num_bags)


#Input-Dependent Iterator: Chain
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





