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

# Print function
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
# What's Your Name?
# def print_full_name(first, last):
#     print("Hello {firstname} {lastname}! You just delved into python".format(firstname=first, lastname=last))
#
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# Find the Runner-Up Score!
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
#
#

