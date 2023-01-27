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
