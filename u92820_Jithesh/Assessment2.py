
# Exercise 1: Perform Basic List Operations

# l = [10, 20, 30]

# access elements
# print(l[2])
# print(l[0])

# slicing
# l = [10, 20, 30]
# print(l[1:4])

# insert
# l = [10, 20, 30]
# l.insert(1,8)
# print(l)

#length
# l = [10, 20, 4, 30, 8, 12]
# print(len(l))

#----------------------------------------------------------
# Exercise 2: Perform List Manipulation

# Add element
# l = [10, 20, 30]
# l.append(40)
# print(l)

# Add multiple elements
# l = [10, 20, 30]
# l.extend([6,2])
# print(l)

# Update element
# l = [10, 20, 4, 30, 8, 12]
# l[2] = 11
# print(l)

# sort
# l = [10, 20, 4, 30, 8, 12]
# l.sort()
# print(l)

# Remove
# l = [10, 20, 4, 30, 8, 12]
# l.remove(8)
# print(l)
# ---------------------------------------------------------------

# Exercise 3: Sum and average of all numbers in a list

# arr = [1,2,3,4,5,6,7,8]

# print("Sum: ",sum(arr))

# avg = sum(arr)//len(arr)
# print("Average: ",avg)
# ---------------------------------------------------------------

# Exercise 4: Reverse a list

# arr = [1,2,3,4,5,6,7,8]

# print("Reversed list: ",list(reversed(arr)))
#--------------------------------------------------

# Exercise 5: Turn every item of a list into its square

# arr = [1,2,3,4,5,6,7,8]

# print("Square of list items: ",list(map(lambda x:x*x,arr)))
#--------------------------------------

# Exercise 6: Find Maximum and Minimum

# arr = [1,43,2,30,4,5,11,6,7,8]

# print("Maximum: ",max(arr))
# print("Minimum: ",min(arr))
#------------------------------------------

# Exercise 7: Count Occurrences

# from collections import Counter
# arr = [11,43,2,7,3,4,2,7,11,6,3,7,4]

# c = Counter(arr)
# print("Occurrences: ",dict(c))
#------------------------------------------

# Exercise 8: Sort a list of numbers

# arr = [1,43,2,30,4,5,11,6,3,7,10,8]

# print("Sorted list: ",sorted(arr))
#-------------------------------------------

# Exercise 9: Create a copy of a list

# arr = [1,2,3,4,5,6,7,8]
# arr_copy = arr.copy()

# print(arr_copy)
#------------------------------------------

# Exercise 10: Combine two lists

# arr1 = [1,2,3,4,"five"]
# arr2 = ["six",7,8,9]

# res = arr1 + arr2

# print(res)
#--------------------------------------

# Exercise 11: Remove empty strings from the list of strings

# arr = ["one","","two","three","","four",""]
# res = []
# for i in arr:
#     if i:
#         res.append(i)

# print(res)
#---------------------------------------------

# Exercise 12: Remove Duplicates from list

# arr = [11,43,2,7,3,4,2,7,11,6,3,7,4]

# print(list(set(arr)))
#--------------------------------------------

# Exercise 13: Remove all occurrences of a specific item from a list

# arr = [11,43,2,7,3,4,2,7,11,6,3,7,4]
# n = int(input("[11,43,2,7,3,4,2,7,11,6,3,7,4], enter the number to be removed: "))

# res = [i for i in arr if i != n]
# print(res)
#--------------------------------------------------

# Exercise 14: List Comprehension for Numbers

# Square of numbers
# n = 10
# res = [i*i for i in range(1,n)]
# print(res)

# Even numbers
# n = 22
# res = [i for i in range(1,n) if i%2==0]
# print(res)

# multiply odd number with 2
# arr = [1,11,43,2,7,3,4,5,7,11,6,3,6,9]

# res = [i*2 for i in arr if i%2!=0]
# print(res)

# matrix flattering
# m = [[1, 2], [3, 4], [5, 6]]
# res = [j for i in m for j in i]
# print(res)
#-----------------------------------------------------------

# Exercise 15: Access Nested Lists

# nlst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(nlst[0][2])
# print(nlst[1])
#---------------------------------------------------

# Exercise 16: Flatten Nested List

# nlst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# res = [j for item in nlst for j in item]
# print(res)
# ----------------------------------------------

# Exercise 17: Concatenate two lists index-wise

# arr1 = ['a', 'c', 'e', 'g', 'i']
# arr2 = ['b', 'd', 'f', 'h','j']

# res = zip(arr1,arr2)
# out = [a+b for a,b in res]
# print(out)
#-----------------------------------------------------

# Exercise 18: Concatenate two lists in the following order

# arr1 = ["Hello","Python"]
# arr2 = ["w","World"]

# res1 = [i+j for i in arr1 for j in arr2]
# res2 = [m+n for m in arr2 for n in arr1]
# print(res1+res2)
#-----------------------------------------------------

# Exercise 19: Iterate both lists simultaneously

# arr1 = [1, 2, 3, 4, 5]
# arr2 = ['one', 'two', 'three', 'four','five']

# for i in range(len(arr1)):
#     print(arr1[i],arr2[i])
#---------------------------------------------------

# Exercise 21: Add new item to list after a specified item

# arr = ['one', 'two', 'three', 'four','five']

# for i in arr:
#     if i == "two":
#         arr[arr.index(i)+1] = "six"

# print(arr) 
# --------------------------------------------------------------

# Exercise 22: Extend nested list by adding the sublist

# nl = [[1,2],[3,4],[5,6],[7,8]]
# sub_lst = [9,10]
# nl.append(sub_lst)
# print(nl)
# -----------------------------------------------------------

# Exercise 23: Replace list’s item with new value if found

# l = [1,2,3,4,5,6,7,8]

# n = 5
# new_val = 10

# for i in range(len(l)):
#     if l[i] == n:
#         l[i] = new_val

# print(l)
#--------------------------------------------------

# Exercise 1: Perform basic dictionary operations 

# Access values
# d = {"name": "Ram", "Age": 30, "Place": "Bnglr", "Subject": "IT"}
# print(d["name"])
# print(d["Age"])
#----------------------------------------------------------------
# Exercise 2: Perform dictionary operations 

# Add item
# d = {"name": "Ram"}
# d["Age"] = 30
# d["Place"] = "Bangalore"
# print(d)

# Remove item
# d = {"name": "Ram", "Age": 30, "Place": "Bnglr", "Subject": "IT"}

# d.pop("Place")
# print(d)
#-----------------------------------------------

# Exercise 3: Dictionary from Lists 

# lst = [1, 2, 3, 4, 5]
# lst2 = ['one', 'two', 'three', 'four','five']

# d = {}

# for i in range(len(lst)):
#     d[lst[i]] = lst2[i]

# print(d)
#---------------------------------------------------

# Exercise 4: Clear Dictionary 

# d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# d.clear()

# print(d)
#-------------------------------------------------

# Exercise 5: Merge two Python dictionaries into one 

# d1 = {1: 'one', 2: 'two', 3: 'three'}
# d2 = {4: 'four', 5: 'five',6: 'six'}

# d3 = ({**d1, **d2})
# print(d3)
#---------------------------------------------------

# Exercise 6: Count Character Frequencies 

# from collections import Counter

# string = "dictionaries"
# c = Counter(string)
# print(dict(c))
# ---------------------------------------------------

# Exercise 7: Access Nested Dictionary 
# d = {1: 'one', 2: 'two', 3: 'three', "Person": {"name":"John", "Age":35}}
# print(d["Person"]["Age"])
#---------------------------------------------------

# Exercise 8: Print the value of key ‘history’ from nested dict

# d = {1: 'one', 2: 'two', "marks": {"maths":25, "history":45}}

# print(d["marks"]["history"])
#------------------------------------------------------------------

# Exercise 9: Modify Nested Dictionary

# d = {1: 'one', 2: 'two', "marks": {"maths":25, "history":45}}

# d["marks"]["maths"] = 30
# print(d)
#------------------------------------------------------------------

# Exercise 10: Initialize dictionary with default values 

# l = [1,2,3,4,5,6]
# d = {}

# for i in l:
#     d[i] = d.get(i,0)
# print(d)
#------------------------------------------

# Exercise 11: Create a dictionary by extracting the keys from a given dictionary 

# d1 = {"name": "Ram", "Age": 30, "Place": "Bnglr", "Subject": "IT"}
# new_dict = {}

# keys = d1.keys()
# for i in keys:
#     new_dict[i] = d1[i]
# print(new_dict)
#-----------------------------------------------------------

# Exercise 12: Delete a list of keys from a dictionary 

# d = {"name": "Ram", "Age": 30, "Place": "Bnglr", "Subject": "IT"}

# keys = ["name","Subject"]

# for i in keys:
#     if i in d.keys():
#         del d[i]

# print(d)
#------------------------------------------------------------

# Exercise 13: Check if a value exists in a dictionary 

# d = {"name": "Ram", "Age": 30, "Place": "Bnglr", "Subject": "IT"}
# val = "IT"

# print(val in d.values())
#------------------------------------------

# Exercise 14: Rename key of a dictionary 

# d = {"name": "Ram", "Age": 30, "Place": "Bnglr", "Subject": "IT"}

# k = "Place"
# if k in d:
#     d["City"] = d.pop("Place")

# print(d)
#------------------------------------------------------

# Exercise 15: Get the key of a minimum value 

# d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6}

# res = min(d,key=d.get)
# print(res)
#------------------------------------------------------

# Exercise 16: Change value of a key in a nested dictionary

# d = {1: 'one', 2: 'two', "marks": {"maths":25, "history":45}}

# d["marks"]["maths"] = 30
# print(d)
#-----------------------------------------------------

# Exercise 17: Invert Dictionary

# d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
# new_dict = {}

# for k,v in d.items():
#     new_dict[v] = k

# print(new_dict)
#-------------------------------------------------------

# Exercise 18: Sort Dictionary by Keys

# d = {3: 'three', 1: 'one', 2: 'two', 5: 'five', 4: 'four'}

# res = dict(sorted(d.items()))
# print(res)
#-----------------------------------------------------

# Exercise 19: Sort Dictionary by Values

# d = {'two': 2, 'four': 4, 'one': 1, 'three': 3, 'five': 5}

# res = dict(sorted(d.items(), key=lambda item : item[1]))
# print(res)
#------------------------------------------------------

# Exercise 20: Check if All Values are Unique
# d = {1: 'two', 4: 'four', 3: 'three', 1: 'one', 5:'five', 6:'one'}

# val = list(d.values())
# for i in val:
#     if val.count(i) > 1:
#         print("Not unique")
#         break
# else:
#     print("Unique")
#-----------------------------------------------------------

# Exercise 1: Perform Basic Tuple Operations

# accessing elements
# tup = (10, 20, 30, 2, 3, 4, 50)

# print(tup[0])
# print(tup[2])

# slicing
# tup = (10, 20, 30, 2, 3, 4, 50)
# print(tup[:5])
# print(tup[3:6])

# concatenate tuple
# t1 = (1,2,3)
# t2 = (4,5,6)
# print(t1+t2)

# tuple to list
# tup = (10, 20, 30, 2, 3, 4, 50)
# print(list(tup))

# index
# tup = (10, 20, 30, 2, 3, 4, 50)
# print(tup.index(3))

# length
# tup = (10, 20, 30, 2, 3, 4, 50)
# print(len(tup))
#-----------------------------------------------------

# Exercise 2: Tuple Repetition
# t = (1,2,3)
# print(t*3)
#----------------------------------

# Exercise 3: Slicing Tuples
# tup = (10, 20, 30, 2, 3, 4, 50)
# print(tup[:5])
# print(tup[3:6])
#-----------------------------------------------

# Exercise 4: Reverse the tuple

# tup = (10, 20, 30, 2, 3, 4, 50)

# print(tuple(reversed(tup)))
#-------------------------------------------

# Exercise 5: Access Nested Tuples

# tup = (10, 20, 30, (2, 3, 4, 50))
# print(tup[3][1])
#-------------------------------------------

# Exercise 6: Create a tuple with single item 50
# t = (50,)
# print(type(t))
#--------------------------------------

# Exercise 7: Unpack the tuple into 4 variables
# t = (1,2,3,4)
# a,b,c,d = t
# print(a,b,c,d)
#------------------------------------------------

# Exercise 8: Swap two tuples in Python

# t1 = (1,2,3)
# t2 = (4,5,6)

# t1,t2 = t2,t1

# print(f"t1: {t1}\nt2: {t2}")
#--------------------------------------------------

# Exercise 9: Copy Specific Elements From Tuple

# tup = (10, 20, 30,2, 3, 4, 50)

# indexes = [2,0,4]
# copy_tup = tuple((tup[i] for i in indexes))

# print(copy_tup)
#---------------------------------------------------

# Exercise 10: List to Tuple
# l = [10, 20, 30,2, 3, 4, 50]

# print(tuple(l))
#-----------------------------------------

# Exercise 11: Function Returning Tuple

# def get_tupl(l):
#     res = tuple(l)
#     return res

# l = [10, 20, 30,2, 3, 4, 50]
# print(get_tupl(l))
#-------------------------------------------

# Exercise 12: Comparing Tuples

# equal
# t1 = (1, 2, 3)
# t2 = (1, 2, 3)

# print(t1 == t2)

# greater than
# t1 = (2, 4, 6)
# t2 = (1, 2, 3)

# print(t1 > t2)
# print(t1 < t2)
#---------------------------------------

# Exercise 13: Removing Duplicates from Tuple

# t = (10, 20, 30,2, 30, 4, 10, 50)
# print(tuple(set(t)))
#--------------------------------------------

# Exercise 14: Filter Tuples
# even numbers
# t = (10, 5, 30,1, 3, 4, 10, 50)
# res = tuple(filter(lambda x : x%2 == 0,t))
# print(res)
#----------------------------------------------

# Exercise 15: Map Tuples
# t = (10, 5, 30,1, 3, 4, 10, 50)

# res = tuple(map(lambda x : x*2, t))
# print(res)
#----------------------------------------------

# Exercise 16: Modify Tuple
# t = (10, 5, 30,1, 3, 4, 10, 50)

# l = list(t)
# l[2] = 11
# t1 = tuple(l)
# print(t1)
#---------------------------------------------

# Exercise 17: Sort a tuple of tuples by 2nd item

# t = ((1,2),(3,5),(23,11),(9,4),(10,30))
# res = sorted(t,key=lambda x : x[1])
# print(res)
#-----------------------------------------------

# Exercise 18: Count Elements

# t = (10, 5, 30,1, 3, 4, 10, 50)
# print(len(t))
#--------------------------------------------

# Exercise 19: Check if all items in the tuple are the same
# t = (1, 1, 1,1, 1, 1, 1, 1)

# if len(set(t)) > 1:
#     print("All are different")
# else:
#     print("All are same")
#-------------------------------------------------

# Exercise 1: Perform Basic Set Operations

# Add
# s1 = {1,2,3,4}
# s1.add(6)
# print(s1)

# Remove
# s1 = {1,2,3,4}
# s1.remove(2)
# print(s1)

# Discard
# s = {1,2,3,4}
# s.discard(6)
# print(s)

# length
# s = {1,2,3,4}
# print(len(s))

# Membership
# s = {1,2,3,4}
# print(3 in s)
#--------------------------------------------------

# Exercise 2: Union of Sets

# s1 = {1,2,3,4}
# s2 = {5,3,6,1}
# print(s1 | s2)
#---------------------------------------------

# Exercise 3: Intersection of Sets

# s1 = {1,2,3,4}
# s2 = {5,3,6,1}
# print(s1 | s2)
#--------------------------------------------

# Exercise 4: Difference of Sets
# s1 = {1,2,3,4}
# s2 = {5,3,6,1}

# print(s1 - s2)
# print(s2 - s1)
#-----------------------------------------

# Exercise 5: Symmetric Difference

# s1 = {1,2,3,4}
# s2 = {5,3,6,1}

# print(s1 ^ s2)
#---------------------------------------

# Exercise 6: Add a list of Elements to a Set
 
# st = {2,44,12,10,4,62,7,8,24}
# l = [5,6,20,33,62,78]

# st.update(l)

# print(st)
#-------------------------------------------------

# Exercise 7: Set Difference Update

# s1 = {1,2,3,4}
# s2 = {5,3,6,1}

# s1.difference_update(s2)
# print(s1)
#----------------------------------------------

# Exercise 8: Remove Items From Set Simultaneously

# s1 = {1,2,3,4}
# s2 = {3,4}

# s3 = s1 - s2
# print(s3)
#---------------------------------------------------

# Exercise 9: Check Subset
# s1 = {1,2,3,4}
# s2 = {3,4}

# print(s2.issubset(s1))
#-----------------------------------------------

# Exercise 10: Check Superset
# s1 = {1,2,3,4}
# s2 = {3,4}

# print(s1.issuperset(s2))
#-----------------------------------------------

# Exercise 11: Set Intersection Check
# s1 = {1,2,3,4}
# s2 = {3,4}
# print(s1 | s2)
#---------------------------------------------------

# Exercise 12: Set Symmetric Difference Update

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# s1.symmetric_difference_update(s2)
# print(s1)
#--------------------------------------------------

# Exercise 13: Set Intersection Update
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

# s1.intersection_update(s2)
# print(s1)
#---------------------------------------------

# Exercise 14: Find Common Elements in Two Lists

# l1 = {1,2,3,4}
# l2 = {3,4,5,6}

# print(list(set(l1) & set(l2)))
#-------------------------------------------------------

# Exercise 15: Frozen Set

# frzn = frozenset([1,2,3,4])
# print(frzn)
#---------------------------------------

# Exercise 16: Count Unique Words

# from collections import Counter
# s = "Hello world welcome to the world of python"

# c = Counter(s.split())
# print(dict(c))
#----------------------------------------------

# arr = """P   A   H   N
# A P L S I I G
# Y   I   R"""

# new_list = []
# # print(arr.split())
# for i in arr:
#     if i != " ":
#         new_list.append(i.strip())

# print(new_list)
# print("".join(new_list))

string = "PAYPALISHIRING"
num_row = 3

rows = [""]*num_row
curr_rw = 0

for char in string:
    rows[curr_rw] += char

print(rows)