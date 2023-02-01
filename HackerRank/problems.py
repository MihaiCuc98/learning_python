# imports:
import itertools
from itertools import combinations

import textwrap
import cmath
import math
import os
import random
import re
import sys
import calendar
from datetime import date
from itertools import combinations
from itertools import combinations_with_replacement


#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     if n >=1 and n<= 100 :
#         if n in range(2,5) and n%2 == 0:
#             print("Not Wird")
#         elif n in range(6,20) and n%2 == 0:
#             print("Weird")
#         elif n > 20 and n%2 == 0 :
#             print("Not Weird")
#         else:
#             print("Weird")


# if __name__ == '__main__':
#     n = int(input())
#     list_n = []
#     if n >= 1 and n <= 20:
#         while n >0 :
#             list_n.append(n-1)
#             n = n-1
#     new_list = list(map(lambda item: item*item, list_n))
#     new_list.reverse()
#     for i in range(len(new_list)):
#         print(str(new_list[i]))


# ---------- write a function

# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if 1900 <= year <= 10 ** 5:
#         if year % 400 == 0:
#             leap = True
#         elif year % 100 == 0:
#             leap = False
#         elif year % 4 == 0:
#             leap = True
#         else:
#             leap = False
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


# ---------- Print function

# if __name__ == '__main__':
#     n = int(input())
#     list_n=[]
#     output = ""
#     while n>0:
#         list_n.append(n)
#         n = n-1
#     list_n.reverse()
#     for i in list_n:
#         output = output+str(i)
#     print(output)


# ---------- What's Your Name?

# def print_full_name(first, last):
#     print("Hello {firstname} {lastname}! You just delved into python".format(firstname=first, lastname=last))
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


# ---------- Find the Runner-Up Score!

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     list_items = list(arr)
#     flag = None
#     if n >= 2 and n <= 10:
#         for item in list_items:
#             if item >= -100 and item <= 100:
#                 flag = True
#             else:
#                 flag = False
#
#     if n == len(list_items):
#         list_items.sort(reverse=True)
#         for index in range(len(list_items)):
#             if list_items[index] > list_items[index+1]:
#                 print(list_items[index+1])
#                 break
#

# ---------- Finding the percentage

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#
#     flag = False
#     if n >= 2 and n <= 10:
#         for i in range (len(scores)):
#             if scores[i] >=0 and scores[i] <= 100:
#                 flag = True
#         print(student_marks)
#         if flag:
#             wanted_marks = student_marks[query_name]
#             print(wanted_marks)
#             sum_list = sum(wanted_marks)
#             length = len(wanted_marks)
#             average = sum_list/length
#             print("%.2f" % average)


# ---------- Lists

# if __name__ == '__main__':
#     N = int(input())
#     my_list = []
#     for i in range(N):
#         cmd = input().split()
#         if cmd[0] == "insert":
#             my_list.insert(int(cmd[1]), int(cmd[2]))
#         if cmd[0] == "print":
#             print(my_list)
#         if cmd[0] == "remove":
#             my_list.remove(int(cmd[1]))
#         if cmd[0] == "append":
#             my_list.append(int(cmd[1]))
#         if cmd[0] == "sort":
#             my_list.sort()
#         if cmd[0] == "pop":
#             my_list.pop()
#         if cmd[0] == "reverse":
#             my_list.reverse()


# ---------- Nested Lists

# if __name__ == '__main__':
#     big_list = []
#     score_list = []
#     name_list = []
#     for _ in range(int(input())):
#         small_list = []
#         name = input()
#         score = float(input())
#         score_list.append(score)
#         small_list.append(name)
#         small_list.append(score)
#         big_list.append(small_list)
#
#     score_list.sort()
#     second_lowest = None
#
#     for i in range(len(score_list)):
#         if score_list[i] < score_list[i+1]:
#             second_lowest = score_list[i+1]
#             break
#     for items in big_list:
#         if items[1] == second_lowest:
#             name_list.append(items[0])
#     name_list.sort()
#     for items in name_list:
#         print(items)
#

# ---------- String Split and Join

# def split_and_join(line):
#     result = line
#     result = result.split(" ")
#     result = "-".join(result)
#     return result
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# ---------- sWAP cASE
# def swap_case(s):
#     return s.swapcase()
#
# if __name__ == '__main__':
#     s = input()
#     if len(s)>0 and len(s)<=1000:
#         result = swap_case(s)
#         print(result)


# ---------- Find a string

# def count_substring(string, sub_string):
#     number_of_findings = 0
#     string_to_work = string
#     for i in range(len(string)):
#         index = string_to_work.find(sub_string)
#         print(index)
#         string_to_work = string_to_work[index+1:]
#
#         print(string_to_work)
#         if index > -1:
#             number_of_findings += 1
#             print(index)
#
#     return number_of_findings
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     if len(string) >=1 and len(string) <=200:
#         sub_string = input().strip()
#         count = count_substring(string, sub_string)
#         print(count)


# ---------- Tuples

# if __name__ == '__main__':
#     n = int(input())
#     cmd = list(map(int, input().split()))
#     tup = ()
#     for x in cmd:
#         tup += (x,)
#
#     if len(cmd) == int(n):
#         print(hash(tup))


# ---------- List Comprehensions

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
#     big_list = [[a, b, c] for a in list(range(x+1)) for b in list(range(y+1)) for c in list(range(z+1))]
#     no_duplicate_list = []
#     [no_duplicate_list.append(element) for element in big_list if element not in no_duplicate_list]
#     index_to_be_removed = []
#     for i in range(len(no_duplicate_list)):
#         if sum(no_duplicate_list[i]) == n:
#             index_to_be_removed.append(i)
#     index_to_be_removed.sort(reverse=True)
#     for i in index_to_be_removed:
#         no_duplicate_list.remove(no_duplicate_list[i])
#     print(no_duplicate_list)


# ---------- Mutations
#
# def mutate_string(string, position, character):
#     final_string = string[:position] + character + string[position+1:]
#     return final_string
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# ---------- String Validators

# if __name__ == '__main__':
#     s = input()
#     s_list = list(s)
#     bool_list = [False, False, False, False, False]
#     if len(s) >0 and len(s)<1000:
#         for elemenet in s_list:
#             if elemenet.isalnum():
#                 bool_list[0] = True
#         for elemenet in s_list:
#             if elemenet.isalpha():
#                 bool_list[1] = True
#         for elemenet in s_list:
#             if elemenet.isdigit():
#                 bool_list[2] = True
#         for elemenet in s_list:
#             if elemenet.islower():
#                 bool_list[3] = True
#         for elemenet in s_list:
#             if elemenet.isupper():
#                 bool_list[4] = True
#         for item in bool_list:
#             print(item)


# ---------- Text Alignment

# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# ---------- Text Wrap

# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# ---------- Introduction to Sets
#
# def average(array):
#     if len(array) == n:
#         result = sum(set(array))/len(set(array))
#         return "%.3f" % result

# set =  is an unordered collection of elements without duplicate entries
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)


# ---------- The Minion Game

# def minion_game(string):
#     string_split = []
#     for i in range(len(string)):
#         string_split.append(string[i])
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     stuart_score = 0
#     stuart_consonants = []
#     kevin_score = 0
#     kevin_vowels = []
#     list_permutations = []
#     for i in range(len(string_split)):
#         if string[i] in vowels:
#             if string[i] not in kevin_vowels:
#                 kevin_vowels.append(string_split[i])
#         elif string[i] not in stuart_consonants:
#             stuart_consonants.append(string_split[i])
#     print(kevin_vowels, stuart_consonants)
#     # stuart
#     list_strings = []
#     for i in range(len(string_split)):
#         comb = combinations(string_split, 2 + i)
#         for j in list(comb):
#             list_permutations.append(list(j))
#     sting = ""
#     for item in list_permutations:
#         for y in item:
#             sting += str(y)
#             list_strings.append(sting)
#         sting = ""
#     no_duplicate_list = []
#     [no_duplicate_list.append(element) for element in list_strings if element not in no_duplicate_list]
#     string_to_work = string
#     kevin_combinations = []
#     stuart_combinations = []
#     for item in no_duplicate_list:
#         if item[0] in kevin_vowels:
#             kevin_combinations.append(item)
#         else:
#             stuart_combinations.append(item)
#     for item in kevin_combinations:
#         for i in range(len(string)):
#             kevin_score += string_to_work.count(item)
#             string_to_work = string_to_work[i:]
#     stuart_string = string
#     for item in stuart_combinations:
#         for i in range(len(string)):
#             stuart_score += stuart_string.count(item)
#             stuart_string = stuart_string[i:]

# for i in range(len(string)):
#     index = string.find(sub_string)
#     print(index)
#     string_to_work = string_to_work[index + 1:]

# print(list(list_permutations))
# print(list_strings)
# print(no_duplicate_list)
# print(kevin_combinations, stuart_combinations)
# print(kevin_score, stuart_score)

#

# solution from the site:   soo smart
# def minion_game(string):
#     length = len(string)
#     kevin_score, stuart_score = 0, 0
#
#     for i in range(length):
#         print(string[i])
#         if string[i] in 'AEIOU':
#
#             kevin_score += length - i
#         else:
#             stuart_score += length - i
#
#     if kevin_score > stuart_score:
#         print('Kevin', kevin_score)
#     elif kevin_score < stuart_score:
#         print('Stuart', stuart_score)
#     else:
#         print('Draw')


# # stuart
# for i in range(len(stuart_consonants)):
#     for y in range(len(string_split)):
#         stuart_consonants[i] = str(stuart_consonants[i])+string_split[y]
#         stuart_score = stuart_score + string.count(stuart_consonants[i])
# print(stuart_score)
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# def minion_game(string):
#     length = len(string)
#     kevin_score, stuart_score = 0, 0
#
#     for i in range(length):
#         print(string[i])
#         if string[i] in 'AEIOU':
#
#             kevin_score += length - i
#         else:
#             stuart_score += length - i
#
#     if kevin_score > stuart_score:
#         print('Kevin', kevin_score)
#     elif kevin_score < stuart_score:
#         print('Stuart', stuart_score)
#     else:
#         print('Draw')
#     print('Kevin', kevin_score)
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)


# ---------- String Formatting

# def print_formatted(number): if 1 <= number <= 100: for i in range(number + 1): if i == 0: continue print(str(
# i).rjust(len(format(number, 'b'))) + str( format(i, 'o')).rjust(len(format(number, 'b'))+1) + str(format(i,
# 'x')).rjust(len(format(number, 'b'))+1) + str(format(i, 'b')).rjust(len(format(number, 'b'))+1))
#
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# ---------- Capitalize

#
# def solve(s):
#     if 0 < len(s) < 100:
#         index = s.find(" ")
#         first_capitalize = s[0].upper()
#         second_capitalize = s[index + 1].upper()
#         print(first_capitalize + s[1:index] + " " + second_capitalize + s[index + 2:])
#     return
#
#
# if __name__ == '__main__':
#     s = input()
#     result = solve(s)


# ---------- Calendar Module

# if __name__ == '__main__':
#     s = input().split(" ")
#     day_dict = {
#         0: "MONDAY",
#         1: "TUESDAY",
#         2: "WEDNESDAY",
#         3: "THURSDAY",
#         4: "FRIDAY",
#         5: "SATURDAY",
#         6: "SUNDAY"
#     }
#
#     day_number = calendar.weekday(int(s[2]), int(s[0]), int(s[1]))
#     print(day_dict[day_number])


# ---------- itertools.permutations()

# if __name__ == '__main__':
#     s = input().split(" ")
#     comb = itertools.permutations(str(s[0]), int(s[1]) )
#     list_comb = list(comb)
#     list_comb.sort()
#     for i in range(len(list_comb)):
#         print(''.join(list_comb[i]))


# ---------- itertools.combinations()

# if __name__ == '__main__':
#     s = input().split(" ")
#     split_string = []
#     [split_string.append(s[0][i]) for i in range(len(s[0]))]
#     split_string.sort()
#     string_after_sort = "".join(split_string)
#     big_list_comb = []
#     for i in range(int(s[1])):
#         big_list_comb.append(sorted(list(combinations(string_after_sort, int(i+1)))))
#     for i in big_list_comb:
#         for y in i:
#             print(''.join(y))


# ---------- itertools.product()

# if __name__ == '__main__':
#     A = list(map(int,input().strip().split()))
#     B = list(map(int,input().strip().split()))
#     if 0 < len(A) < 30 and 0 < len(B) < 30:
#         A.sort()
#         B.sort()
#         str_to_output = ""
#         prod = itertools.product(A, B)
#         for i in list(prod):
#             str_to_output = str_to_output + str(i) + " "
#         print(str_to_output)


# ---------- itertools.combinations_with_replacement()

# if __name__ == '__main__':
#     S = input().split(" ")
#     split_string = []
#     [split_string.append(S[0][i]) for i in range(len(S[0]))]
#     split_string.sort()
#     new_string = "".join(split_string)
#     if 0 < int(S[1]) <= len(S[0]) and new_string.isupper():
#         comb = combinations_with_replacement(new_string, int(S[1]))
#         for i in list(comb):
#             print("".join(i))


# ---------- Power - Mod Power

# if __name__ == '__main__':
#      A = int(input())
#      B = int(input())
#      m = int(input())
#      print(int(pow(A, B)))
#      if B >=0:
#          print(int(pow(A,B,m)))


# ---------- Mod Divmod

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a // b)
#     print(a % b)
#     print(divmod(a, b))


# ---------- Integers Come In All Sizes

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     if 1 <= a <= 1000 and\
#        1 <= b <= 1000 and\
#        1 <= c<= 1000 and \
#        1 <= d <= 1000:
#         print(a**b + c**d)


# ---------- Polar Coordinates

# if __name__ == '__main__':
#     compl = input()
#     index_to_split = 0
#     if compl.find("-") == 0:
#         index_to_split = compl[1:].find("-") + 1
#     else:
#         index_to_split = compl.find("-")
#     if compl.find("+")>0:
#         index_to_split = compl.find("+")
#     x = int(compl[:index_to_split])
#     y = int(compl[index_to_split:compl.index("j")])
#     print(math.sqrt(x ** 2 + y ** 2))
#     print(cmath.phase(complex(x, y)))


# ---------- Set .add()

# Documentation:
# 1. Sets are used to store multiple items in a single variable.
# 2. Set items are unordered, unchangeable, and do not allow duplicate values
#
#
# if __name__ == '__main__':
#     N = int(input())
#     items = []
#     for i in range(N):
#         items.append(input())
#     set_items = {items[0]}
#     for i in range(N - 1):
#         try:
#             set_items.add(items[i])
#         except Exception:
#             continue
#     print(len(set_items))


# ---------- Set .discard(), .remove() & .pop()

# n = int(input())
# s = set(map(int, input().split()))
# N = int(input())
# sum_elem = 0
# if n == len(s):
#     for i in range(N):
#         cmd = input().split(" ")
#         if cmd[0] == "pop":
#             s.pop()
#         if cmd[0] == "remove":
#             s.remove(int(cmd[1]))
#         if cmd[0] == "discard":
#             s.discard(int(cmd[1]))
#     for i in s:
#         sum_elem += i
#     print(sum_elem)


# ---------- Two Sum ---- LeetCode.com

# def twoSum(nums: list, target: int):
#     comb = combinations(nums, 2)
#     mini_list = []
#
#     for i in list(comb):
#         if sum(i) == target:
#             mini_list.append(i[0])
#             mini_list.append(i[1])
#             break
#     print(mini_list)
#     if mini_list[0] == mini_list[1]:
#         result = [int(nums.index(mini_list[0])), int(nums.index(mini_list[1], int(nums.index(mini_list[0]))+1))]
#     else:
#         result = [int(nums.index(mini_list[0])), int(nums.index(mini_list[1]))]
#     return result
# big_list = []
# result = twoSum(big_list, 19999)
# print(result)