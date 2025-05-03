# Apna Collage practice qustion

# 1. WAP to input side of a square & print its area

"""a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
sum = a + b
print("Sum of a and b is :",sum)"""


# 2. WAP to input 2 floating point numbers & print their average.

# a = int(input("Enter 1st number :"))
# b = int(input("Enter 2nd number :"))
# avg = (a + b)/2
# print("Average of a and b is :",avg)

# 3. WAP to input side of a square & print its area

# a = int(input("Enter 1st number :"))
# area = a * a
# print("Area of square is :",area)


# 4.  WAP to input 2 int numbers, a and b.
# Print True if a is greater than or equal to b. If not print False.

# a = int(input("Enter 1st number :"))
# b = int(input("Enter 2nd number :"))

# print(a >= b)


# 5. WAP to check if a number entered by the user is odd or even.

# number = int(input("Enter 1st number :"))

# if number % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# 6. WAP to find the greatest of 3 numbers entered by the user.

# a = int(input("Enter 1st number :"))
# b = int(input("Enter 2nd number :"))
# c = int(input("Enter 3rd number :"))

# if a > b and a > c:
#     print("a is greater")
# elif b > a and b > c:
#     print("b is greater")
# else:
#     print("c is greater")

# 7. WAP to check if a number is a multiple of 7 or not.

# number = int(input("Enter 1st number :"))

# if number % 7 == 0:
#     print("Number is multiple of 7")
# else:
#     print("Number is not multiple of 7")


# 8. WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# fev_tvSeries =[]

# tvSeries1 = input("Enter 1st TV Series :")
# fev_tvSeries.append(tvSeries1)
# tvSeries2 = input("Enter 2nd TV Series :")
# fev_tvSeries.append(tvSeries2)
# tvSeries3 = input("Enter 3rd TV Series :")
# fev_tvSeries.append(tvSeries3)

# print(fev_tvSeries)


# 9. WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

# word = [1, "abc", "abc", 1]

# word_copy = word.copy()
# word_copy.reverse()
# print(word_copy)

# if word == word_copy:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 10. WAP to count the number of students with the “A” grade in the following tuple

# gread = ("C", "D", "A", "A", "B", "B", "A")
# count = gread.count("A")
# print(count)


# 11. Store the above values in a list & sort them from “A” to “D”.

# gread = ["C", "D", "A", "A", "B", "B", "A"]
# gread.sort()
# print(gread)


# 12. Store following word meanings in a python dictionary :
# table : “a piece of furniture”, “list of facts & figures”
#  cat : “a small animal”

# dict = {
#     "cat" : "a small animal",
#     "table" : ("a piece of furniture", "list of facts & figures")
# }
# print(dict)



# 13. You are given a list of subjects for students. Assume one classroom is required for 1
#  subject. How many classrooms are needed by all students.
#  ”python”, “java”, “C++”, “python”, “javascript”,
#  “java”, “python”, “java”, “C++”, “C”

# subject = {
#     "python", "java", "C++", "python", "javascript",
#     "java", "python", "java", "C++", "C"
# }
# print(len(subject))


# 14. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value

# subject = {}

# s = input("Enter math mark :")
# subject.update({"math" : s})
# s = input("Enter phy mark :")
# subject.update({"phy" : s})
# s = input("Enter cham mark :")
# subject.update({"cham" : s})

# print(subject)


# 15. Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# number = {("int :", 9), ("float :", 9.0)}
# print(number)


# 16. Print numbers from 1 to 100.
# while loop
# i = 1
# while i <= 100:
#   print(i)
#   i += 1


# 17. Print numbers from 100 to 1.
# while loop
# i = 100
# while i >= 1:
#   print(i)
#   i -= 1


# 18. Print the multiplication table of a number n.
# while loop
# n = int(input("Enter number :"))
# i = 1
# while i <= 10:
#   print(i * n)
#   i += 1


# 19. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#   print(nums[i])
#   i += 1

# 20. Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# n = int(input("Enter your number for search :"))
# i = 0
# while i < len(nums):
#   print(nums[i])
#   if nums[i] == n:
#     print(f"'{n}' is found at idx : {i}")
#     break
#   i += 1



# useing for loop
# 21. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# rendom_num = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# for i in rendom_num:
#   print(i)


# 22. Search for a number x in this tuple using loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# rendom_num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# n = int(input("Enter number :"))
# idx = 0
# for vlu in rendom_num:
#   print(vlu)
#   if vlu == n:
#     print(f"{vlu} found at idx : {idx}")
#     break
#   idx += 1


# using for & range( )
# 23. Print numbers from 1 to 100.

# for i in range(1, 100):
#   print(i)

# 24. Print numbers from 100 to 1.

# for i in range(100, 0, -1):
#   print(i)

# 25. Print the multiplication table of a number n.

# for i in range(1, 11):
#   print(i * n)


# 26. WAP to find the sum of first n numbers. (using while)

# n = int(input("Enter your number :"))
# i = 0
# sum = 0
# while i <= n:
#   sum += i
#   i += 1
# print(sum)

# 27. WAP to find the factorial of first n numbers. (using for)

# n = int(input("Enter your number :"))
# fact = 1
# for i in range(1, n+1):
#   fact *= i
# print(fact)

# 28. WAF to print the length of a list. ( list is the parameter)

# rendom_num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# def print_lent(list):
#   print(len(list))
# print_lent(rendom_num)


# 29. WAF to print the elements of a list in a single line. ( list is the parameter)

# rendom_num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# def print_elem(list):
#   for i in list:
#     print(i, end=" ")
# print_elem(rendom_num)


# 30. WAF to find the factorial of n. (n is the parameter)

# def fact(n):
#   fact = 1
#   for i in range(1, n+1):
#     fact *= i
#   print(fact)
# fact(5)

# 31. WAF to convert USD to BDT.

# def usd_to_bdt(usd):
#   fact = usd * 121.91
#   print(f"{usd} USD : {fact} BDT")
# usd_to_bdt(2000)

# 32. Write a recursive function to calculate the sum of first n natural numbers.

# def calculat_sum(n):
#   if n == 1:
#     return 1
#   return calculat_sum(n - 1) + n

# print(calculat_sum(5))

# 33. Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

# def show_list(list, idx=0):
#   if idx == len(list):
#     return
#   print(list[idx])
#   show_list(list, idx + 1)

# rendom_num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# show_list(rendom_num)


# 34. Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

"""with open("practice.txt", "w") as f:
   data = f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")"""

# 35. WAF that replace all occurrences of “java” with “python” in above file.

"""with open("practice.txt", "r") as f:
   data = f.read()

replace = data.replace("Java", "Python")
print(replace)"""

# 36. Search if the word “learning” exists in the file or not.
"""def find_word():
    word = input("Enter your word :")
    with open("practice.txt", "r") as f:
        data = f.read()
    if word in data:
        print(f"'{word}' found")
    else:
        print("Word not found")

find_word()"""
  

# 37. WAF to find in which line of the file does the word “learning”occur first.
#Print -1 if word not found.

"""def find_wordline():
    word = input("Enter your word :")
    data = True 
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"'{word}' found line : {line_no}")
                return
            line_no += 1
        return -1
print(find_wordline())"""

# 38. more efficient way to find world and World line

"""def find_word():
    word = input("Enter your word :")
    found = False
    count = 0
    with open("practice.txt", "r") as f:
        for line_no, line in enumerate(f, start=1):
            if word.lower() in line.lower():
                print(f"'{word}' found at line : {line_no}")
                found = True
                count += 1
    if found:
        print(f"'{word}' total occerrences : {count}")
    else:
         print(f"'{word}' is not found in this file")
         
find_word()"""
     
     
# 39. From a file containing numbers separated by comma, print the count of even numbers.

"""with open("number.txt", "w") as f:
    data = f.write("12, 13, 45, 97, 54, 6, 4, 74, 84, 866")
    
with open("number.txt", "r") as f:
    data = f.read()
    count = 0
    num = data.split(",")
    for vlu in num:
        if(int(vlu) % 2 == 0):
            print(int(vlu))
            count += 1
print(f"Total even num : {count}")"""


# 40. Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

"""class Student:
    def __init__(self, name, math, phy, cham):
        self.name = name
        self.math = math
        self.phy = phy
        self.cham = cham
        
    def marks(self):
        print(f"Student Name : {self.name}\nMath : {self.math}\nPhysic : {self.phy}\nChamstry : {self.cham}")
        
    def total_avg(self):
        sum = self.math + self.phy + self.cham
        avg = sum / 3
        print(f"'{self.name}' your total marks : {sum}")
        print(f"'{self.name}' your marks average : {avg}")
        
s1 = Student("Jisan", 80, 70, 89)
s1.marks()
s1.total_avg()

def stu_result(name, math, phy, cham):
    s = Student(name, math, phy, cham)
    s.marks()
    s.total_avg()

stu_result("Robart pationson", 100, 70, 90)"""

# 41. Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

"""class Account:
    def __init__(self, name, acu, pwd, blnc):
        self.name = name
        self.acu = acu
        self.__pwd = pwd
        self.blnc = blnc
        
    def account_detils(self, pwd):
         if self.__pwd == pwd:
             print(f"Name : {self.name}\nAcount number : {self.acu}\nPessword : {self.__pwd}\nBalance : {self.blnc}")
         else:
            print("Pessword is incorrect")
    
    def debit(self, add, pwd):
        if self.__pwd == pwd:
            print(f"{self.name} your balance is added : {add}")
            self.blnc += add
            print(f"'{self.name}' your total balance : {self.blnc}")
        else:
            print("Pessword is incorrect")
        
    def credit(self, widraw, pwd):
        if self.__pwd == pwd:
            if widraw > self.blnc:
                print("error")
            else:
                self.blnc -= widraw
            print(f"'{self.name}' your total balance : {self.blnc}")
        else:
            print("Pessword is incorrect")            
        
    def chak_balance(self, pwd):
        if self.__pwd == pwd:
            print(f"'{self.name}' your total balance : {self.blnc}")
        else:
            print("Pessword is incorrect")

a1 = Account("Jisan", "abc098", "Jisan098", 5000)
a1.debit(590, "Jisan098")
a1.credit(4989, "Jisan098")
a1.chak_balance("Jisan098")
#print(a1.pwd)
a1.account_detils("Jisan098")"""


# 42. Qs . Define a Circle class to create a circle with radius r using the constructor Define an Area ( ) method of the class which calculates the area of the circle . Define a Perimeter ( ) method of the class which allows you to calculate the perimeter of the circle.

"""class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2
        
    def perimeter(self):
        return 2 * (22/7) * self.radius
        
c1 = Circle(7)
print(c1.area())
print(c1.perimeter())"""


# 43. Qs . Define a Employee class with attributes role , department & salary . This class also a showDetails ( ) method . Create an Engineer class that inherits properties from Employee & has additional attributes : name & age .

"""class Coder:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill
        
    def coder_bio(self):
        print(f"Name : {self.name}\nAge : {self.age}\nSkill : {self.skill}")

class Employee(Coder):
    def __init__(self, name, age, skill, com, role, dep, salary):
        super().__init__(name, age, skill)
        self.com = com
        self.role = role
        self.dep = dep
        self.salary = salary
        
    def employee_details(self):
        super().coder_bio()
        print(f"Company : {self.com}\nRole : {self.role}\nDepartment : {self.dep}\nSalary : {self.salary}")
        
ep1 = Employee("Jisan", 21, "Python", "Google", "Data scintest", "AI", 200000)
ep1.employee_details()"""
    

# 44. Qs . Create a class called Order which stores item & its price . Use Dunder function __gt __ ( ) to convey that : order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, name, item, price):
        self.name = name
        self.item = item
        self.price = price
        
    def show_order(self):
        print(f"'{self.name}' your order\nItem : {self.item}\nPrice : {self.price}")
        
    def __gt__(self, odr2):
            return self.price > odr2.price
            
        
odr1 = Order("Jisan", "Pizza", 399)
odr1.show_order()

odr2 =  Order("Jason", "Mojo", 80)
odr2.show_order()

print(odr1 > odr2)
        