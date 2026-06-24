# 1. print Hello Python

print("Hello Python")

# ------------------------------
# 2. Sum of Two Numbers

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))

print(a+b)

# ---------------------------------------------
# 3. Even or Odd

n = int(input("Enter the number: "))

if n%2 == 0:
    print("Even")
else:
    print("Odd")

# ----------------------------------------------------
# 4. Positive, Negative, or Zero

n = int(input("Enter the number: "))

if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")

# ----------------------------------------------------------
# 5. Largest of Two Numbers

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))

print(max(a,b))

# ------------------------------------------------------
# 6. Multiplication Table

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"5 X {i} = {5*i}")

# -----------------------------------------------------
# 7. Sum of Numbers from 1 to N

N = int(input("Enter the number: "))

print(sum(i for i in range(N+1)))

# -------------------------------------------------------
# 8. Count Even Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(len([i for i in numbers if i%2==0]))

# -------------------------------------------------------
# 9. Reverse a String

s = input("Enter the string: ")

print("".join(reversed(s)))

# ---------------------------------------------
# 10. Find Largest Number in a List

numbers = [12, 45, 3, 67, 22]
print(max(numbers))

# -------------------------------------------------
# 11. Create a Function for Addition

def add(a,b):
    return a+b

a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

print(add(a,b))

# ---------------------------------------------
# 12. Function to Check Even Number

def evn_odd(number):
    if number%2 == 0:
        return True
    else:
        return False

num = int(input("Enter the number: "))
print(evn_odd(num))

# ------------------------------------------------
# 13. Count Elements in a List

fruits = ["apple", "banana", "orange", "apple", "grapes"]
print(len(fruits))

# -------------------------------------------------------------
# 14. Dictionary Lookup

student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student["course"])

# ---------------------------------------
# 15. Student Class

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

obj = Student("Rahul",22)
obj.display()

# -----------------------------------------------
# 16. Find Factorial of a Number

def fact(num):
    res = 1
    if num <= 0:
        res*=1
    else:
        res *= num*fact(num-1)
    return res

num = int(input("Enter the number: "))
print(fact(num))

# ------------------------------------------------
# 17. Count Vowels in a String

s = input("Enter the string: ")

print(sum(1 for i in s if i in "aeiouAEIOU"))

# --------------------------------------------------------
# 18. Remove Duplicates from a List

arr = [1, 2, 2, 3, 4, 4, 5]

print(list(set(arr)))

# ---------------------------------------------------
# 19. Read and Write a File

with open("demo.txt","w") as f:
    f.write("Python Training")

with open("demo.txt",'r') as f:
    for line in f:
        print(line)

#-----------------------------------------------------
# 20. Handle Division by Zero

def devision(a,b):
    try:
        return (a//b)
    except:
        return "Cannot devide with zero"

a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

print(devision(a,b))
