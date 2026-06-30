# Exercise 1: List Comprehension Mastery
# words = ["apple", "bat", "cherry", "dog", "elderberry"]

# res = [word.upper() for word in words if len(word) > 4]

# print(res)
#-----------------------------------------------------------

# Exercise 2: Dictionary Merging with Logic

# def merge_d(d1, d2):
#     for k,v in dict_a.items():
#         if k in dict_b:
#             dict_b[k] = v + dict_b[k]
#         else:
#             dict_b[k] = v
#     return dict_b

# dict_a = {'a': 10, 'b': 20}
# dict_b = {'b': 5, 'c': 15}

# print(merge_d(dict_a, dict_b))
#-----------------------------------------------------

# Exercise 3: Frequency Map with Counter

# def count_str(text):
#     n_text = text.replace(" ","")
#     count = {}
#     for letter in n_text.lower():
#         count[letter] = count.get(letter,0)+1
#     return count

# text = "Python Programming"
# print(count_str(text))
#------------------------------------------------------

# Exercise 4: Anagram Checker

# def anagram(w1, w2):
#     s_w1 = "".join(sorted(w1))
#     s_w2 = "".join(sorted(w2))
#     if s_w1 == s_w2:
#         return True
#     else:
#         return False


# word1 = "listen"
# word2 = "silent"

# print(f"Is \"listen\" an anagram of \"silent\"? {anagram(word1, word2)}")
#----------------------------------------------------------------------------

# Exercise 5: Flatten a Nested List

# out_list = []
# def flatten(nested):
#     global out_list
#     for item in nested:
#         if type(item) == list:
#             flatten(item)
#         else:
#             out_list.append(item)
#     return out_list

# nested = [1, [2, 3], [4, [5, 6]], 7]
# print(flatten(nested))
#------------------------------------------------

# Exercise 6: Reverse Each Word of a String

# input_str = "Python is awesome"

# split_str = input_str.split()
# for i in range(len(split_str)):
#     split_str[i] = "".join(reversed(split_str[i]))

# print(" ".join(split_str))

#--------------OR------------------

# out = ""
# for word in input_str.split():
#     res = "".join(reversed(word))
#     print(res, end=" ")
#     out += res
# print(out)
#---------------------------------------------------

# Exercise 7: Palindrome Sentence

# import re
# def palindrome(given_str):
#     sntnc = "".join(re.findall(r'[a-zA-Z]+', given_str))
#     reverse_sntnc = "".join(reversed(sntnc.lower()))
#     if sntnc.lower() ==  reverse_sntnc:
#         return True
#     else:
#         return False

# given_str = "A man, a plan, a canal: Panama"
# print(palindrome(given_str))
#----------------------------------------------------

# Exercise 8: List Comprehension Filtering (Advanced)

# arr = ["apple", "education", "ice", "ocean", "python", "umbrella"]

# res = [item for item in arr if len(item) > 5 and item[0] in "aeiouAEIOU"]

# print(res)
#-----------------------------------------------------------------------------------

# Exercise 9: Remove Duplicates (Preserving Order)

# def duplicate(arr):
#     new_list = []

#     for item in arr:
#         if item not in new_list:
#             new_list.append(item)

#     return new_list

# arr =  [1, 2, 2, 3, 1, 4, 2]
# print(duplicate(arr))
#---------------------------------------

# Exercise 10: Circular Shift (Rotation)

# def rotation(lst, n, direction):
#     if direction == "right":
#         return lst[-n:] + lst[:-n]
    
#     elif direction == "left":
#         return lst[n:] + lst[:n]


# arr = [1, 2, 3, 4, 5]
# Shift = 2
# Direction = 'right'

# print(rotation(arr, Shift, Direction))
#---------------------------------------------

# Exercise 11: Dictionary Merging (Value Grouping)

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# new_d = {}

# for k,v in d1.items():
#     if k in d2:
#         new_d[k] = [v,d2[k]]
#     else:
#         new_d[k] = [v]

# for key,val in d2.items():
#     if key not in new_d:
#         new_d[key] = [val]

# print(new_d)
#---------------------------------------

# Exercise 12: Inverted Index

# def invert(input_d):
#     d = {}
#     for k,v in input_d.items():
#         if type(v) == list:
#             for item in v:
#                 d[item] = k
#         else:
#             d[v] = k
#     return d


# input_d = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

# print(invert(input_d))
#-------------------------------------------------------

# Exercise 13: Dictionary Sorting (Lambda)

# employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]

# res = sorted(employees, key=lambda x : x["salary"])
# print(res)
#-----------------------------------------------------------

# Exercise 14: Subset and Superset Validation

# def set_validation(Set_A, Set_B):
#     if Set_A.issubset(Set_B):
#         print("Set A is subset of Set B")
#     else:
#         print("Not a Subset")

#     if Set_A.issuperset(Set_B):
#         print("Set A is a superset of Set B")
#     elif Set_B.issuperset(Set_A):
#         print("Set B is a superset of Set A")
#     else:
#         print("Invalid")
    
#     if Set_A.isdisjoint(Set_B):
#         print("Set A is not a disjoint of Set B")
#     elif Set_B.isdisjoint(Set_A):
#         print("Set B is not a disjoint of Set A")
#     else:
#         print("Invalid")


# Set_A = {1, 2, 3}
# Set_B = {1, 2, 3, 4, 5}

# set_validation(Set_A, Set_B)
#-----------------------------------------------

# Exercise 15: Set Symmetric Difference

# list1 = [101, 102, 103]
# list2 = [103,104, 105]

# res = set(list1).symmetric_difference(set(list2))

# print(res)
#----------------------------------------------------

# Exercise 16: Power Set Generation

# arr = [1, 2, 3]
# n = len(arr)

# pow_set = []

# for i in range(1<<n):
#     subset = ()
#     for j in range(n):
#         if i & (1 << j) != 0:
#             subset += (arr[j],)
#     pow_set.append(subset)

# print(pow_set)
#==========================================

# Exercise 17: Age Calculator (Exact)

# def age_calc(Birthdate, Today):

#     bd = Birthdate.split("-")
#     td = Today.split("-")

#     years = int(td[0]) - int(bd[0])
#     months  = int(td[1]) - int(bd[1])
#     days = int(td[2]) - int(bd[2])

#     if days < 0:
#         months -= 1
#         days = 31 + days
    
#     if months < 0:
#         years -= 1
#         months = 12 + months

#     print(f"{years} years, {months} months, {days} days")

# Birthdate =  "1995-05-15"
# Today = "2026-01-02"
# age_calc(Birthdate, Today)
#-------------------------------------------------------------------

# Exercise 18: Countdown Timer (Time Delta)

# from datetime import datetime
# import re

# def days_to_go(Current_Date, curr_time, New_year):
#     cd = Current_Date.split("-")
#     ny = New_year.split("-")
#     ct = curr_time.split(":")
#     date1 = datetime(int(cd[0]), int(cd[1]), int(cd[2]), int(ct[0]), int(ct[1]))
#     date2 = datetime(int(ny[0]), int(ny[1]), int(ny[2]))

#     difference = date2 - date1

#     days = difference.days
#     seconds = difference.seconds
#     hours = seconds//3600
#     minutes = (seconds % 3600) // 60
    
#     return f"{days} days, {hours} hours, {minutes} minutes until New Year!"


# date =  "2026-01-02 7:10"
# curr_date = re.findall(r'\d{4}-\d{2}-\d{2}', date)
# curr_time = re.findall(r'\d{1}:\d{2}', date)

# New_year = "2027-01-01"

# res = days_to_go(curr_date[0], curr_time[0],  New_year)
# print(res)

#--------------------------OR------------------------------------

# from datetime import datetime

# def days_to_go(Current_Date, New_year):

#     date1 = datetime.strptime(Current_Date, "%Y-%m-%d %I:%M")
#     date2 = datetime.strptime(New_year, "%Y-%m-%d")

#     difference = date2 - date1

#     days = difference.days
#     seconds = difference.seconds
#     hours = seconds//3600
#     minutes = (seconds % 3600) // 60
    
#     return f"{days} days, {hours} hours, {minutes} minutes until New Year!"

# curr_date =  "2026-01-02 7:10"
# New_year = "2027-01-01"

# print(days_to_go(curr_date, New_year))

#--------------------------------------------------------------------------------

# Exercise 19: Business Days Calculator

# from datetime import datetime, timedelta

# def business_days(start_date, n):

#     delta = timedelta(days = n)

#     start = datetime.strptime(start_date, "%Y-%m-%d")
#     future_date = ""
#     w = start.isoweekday()
#     if w <= 5:
#         future_date = start + delta

#     print(future_date)

# day = "Friday"
# date = "2026-01-02"
# N = 5
# business_days(date, N)
#--------------------------------------------------------------

# Exercise 20: Custom Iterator Class

# class PowerOfTwo:
#     def __init__(self,exponent):
#         self.exponent = exponent

#     def powers(self):
#         n = self.exponent
#         count = 1
#         res = []
#         while count <= n:
#             for i in range(1,10):
#                 if 2%i == 0:
#                     res.append(i)
#                 count += 1
#         return res
    
# powers = PowerOfTwo(3)
# print(powers.powers())
#######################################################Not Done
#---------------------------------------------

# Exercise 21: Find Duplicates in O(n) Time

# def duplicat(numbers):
#     res = set()
#     for num in numbers:
#         if numbers.count(num) > 1:
#             res.add(num)

#     return res

# numbers = [1, 2, 3, 2, 4, 5, 1, 6]
# print(duplicat(numbers))
#---------------------------------------------------

# Exercise 22: Singly Linked List Implementation

#####################################################Not Done

# Exercise 23: Stack Implementation (LIFO)

# class Actions:
#     def __init__(self):
#         self.stack = []

#     def pop(self):
#         print(f"Current Top: {self.stack}")
#         if len(self.stack) > 0:
#             pop_item = self.stack.pop()
#             print(f"Popped: {pop_item}")
#         else:
#             print("No items found")
#         print(f"New Top: {self.stack}")

#     def push(self, items):
#         if isinstance(items, list):
#             self.stack.extend(items)
#         else:
#             self.stack.append(items)
#         return self.stack
    
#     def peek(self):
#         if len(self.stack) > 0:
#             return f"Top: {self.stack[-1]}"
#         else:
#             raise IndexError("empty list")


# items = ["google.com", "pynative.com"]
# Action: "Pop"

# obj = Actions()
# print(obj.push(items))

# print(obj.peek())

# obj.pop()
#--------------------------------------------------------------

# Exercise 24: Queue Implementation (FIFO)

# from collections import deque

# class data_que:
#     def __init__(self):
#         self.dq = deque()
    
#     def enqueue(self, data_arr):
#         for item in data_arr:
#             self.dq.append(item)
#         print(self.dq)

#     def dequeue(self):
#         if len(self.dq) > 0:
#             serving = self.dq.popleft()
#             print(f"Serving: {serving}")
#         print(f"Next in line: {self.dq}")
        

# arr = ["Customer A", "Customer B"]
# Action = "Dequeue"

# obj = data_que()
# obj.enqueue(arr)
# obj.dequeue()
#----------------------------------------------------------

# Exercise 25: Recursive Binary Search

# def binary_search(sorted_list, target, left, right):
#     if left > right:
#         return -1
    
#     mid = (left + right) // 2
#     if sorted_list[mid] == target:
#         return mid
    
#     elif sorted_list[mid] > target:
#         return binary_search(sorted_list, target, left, mid - 1)
    
#     else:
#         return binary_search(sorted_list, target, mid + 1, right)


# Sorted_list = [10, 20, 30, 40, 50, 60]
# Target = 30

# res = binary_search(Sorted_list, Target, 0, len(Sorted_list)-1)

# if res != -1:
#     print(res)
# else:
#     print("Target not found")
#------------------------------------------------------------------------

# Exercise 26: Lambda Sorting with Tuples

# employees = [("Alice", 30, 50000), ("Bob", 25, 75000), ("Charlie", 35, 60000)]

# res = list(sorted(employees, reverse=True, key=lambda x : x[2]))
# print(res)
#------------------------------------------------------------------------------------

# Exercise 27: Map and Filter Combination

# nums = [1, 2, 3, 4, 5, 6]

# res = list(map(lambda y : y**2, filter(lambda x : x%2==0, nums)))
# print(res)
#----------------------------------------------------------------------------

# Exercise 28: Custom @timer Decorator

# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Function {func.__name__} took {end-start:.4f} seconds to run")
#     return wrapper


# @timer
# def waste_time():
#     return time.sleep(1.5)

# waste_time()
#-----------------------------------------------------

# Exercise 29: Fibonacci Generator (Memory Efficiency)

# def fibonacci(n):
#     n1 = 0
#     n2 = 1
#     for i in range(n):
#         yield n1
#         n1, n2 = n2, n1+n2

# n = 8
# f = fibonacci(n)

# for j in range(n):
#     print(next(f), end=" ")
#-------------------------------------------

# Exercise 30: Custom Context Manager ( with statement)

##############################################################Not Done
# Exercise 31: The Versatile *args and **kwargs

# def log_event(event, *args, **kwargs):
#     print(f"Event: {event}")
#     # for i in args:
#     print(f"Details: {args}")
#     print(f"Metadata: {kwargs}")


# log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
#----------------------------------------------------------

# Exercise 32: Zip and Enumerate Mapping

# names = ["Alice", "Bob", "Charlie"] 
# scores = [85, 92, 78]

# res = dict(zip(names, scores))

# order_res = dict(sorted(res.items(), reverse = True, key=lambda x : x[1]))

# count = 1
# for k,v in order_res.items():
#     print(f"Rank{count}: {k} scored {v}")
#     count += 1
#-----------------------------------------------------

# Exercise 33: Memoization with lru_cache

##############################################Not Done

# Exercise 34: Set Operations for Data Analysis

# trial = [1, 2, 3, 4, 5]
# paid = [4, 5, 6, 7, 8]

# Upgraded = set(trial) & set(paid)
# print(Upgraded)

# Leads = set(trial).difference(set(paid))

# print(Leads)

# Unique = set(trial).symmetric_difference(set(paid))
# print(Unique)
#-------------------------------------------------------

# Exercise 35: Inheritance and Method Overriding

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def fuel_type(self):
#         print("Vehicle fuel type")

# class ElectricCar(Vehicle):
#     def brand_type(self):
#         print(f"Brand: {self.brand}")

#     def fuel_type(self):
#         return "Electricity"

# car = ElectricCar("Tesla")
# car.brand_type()
# print(f"Fule Type: {car.fuel_type()}")
#---------------------------------------------

# Exercise 36: Encapsulation (Private Attributes)

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print(f"Insufficient funds! Final Balance: {self.__balance}")
#         else:
#             self.__balance -= amount
            
# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(200)
#--------------------------------------------------

# Exercise 37: Property Decorators ( @property )

class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value < 0 or value >100:
            raise ValueError("Score must be between 0 and 100.")
        else:
            self._score = value
            return self.score

s = Student("kevin", 10)
s.score = 110
print(s.score)