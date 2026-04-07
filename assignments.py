#theoretical assignment:
#(1)  Explain python's Role in data scince.
#ans... introduction:- pytjon is one of the mosst popuar programig langiages used in data science. ye bahut use hota he kyoki pythan simple, powerfull or isme bahut usefull libreris he
# data callaction:- python alag alag soursenjesenwebsite or database se data collact karne me madad karta he
# data cleaning:- raw data me aksar error, mising value or duplicat data hota he python data ko clean or preper karne me madad karta he
#python data ko analy karne me or usme se usefull infomation nikalne me use hota he
#python data ko graphs or charts ke form me dikhane me madad karta he, machine learning modal banane me use hota he
#



#(2)  presentation:object- Orianted programing (oop) Concepts in python
# what is oops:- object orianted programing ek programing he jo objects or classes pr based hoti he, class ek blue print hota he iska use object banane ke liye hota he



#prectice tasks:
#task1: python Fundamentals
#1) Write a python program to sum of the first n positive integers.
#ans....
n = int(input("enter a number :"))
sum = 0
for i in range(1, n + 1):
    sum = sum + i 
print("positive integers is:", sum)


#2) Write a pyhon program to count occurences of a substring in a string.
#ans.......

string = input("enter a string: ")
substring = input("enter substring to count: ")

count = string.count(substring)
print("occurences:", count)


#3) write a python program to count the ocurrences of each word in a givin sentence..

sentence = input("enter a sentence :")
words = sentence.split()
for word in words:
    print(word, ":", words.count(word))


#4) write a python program to get a single sttring from  two givin strings, seprated by a space and swap the first two charectors of each string

string1 = "ABC"
string2 = "XYZ"
new_string1 = string1[:2] + string2[2:]
new_string2 = string2[:2] + string1[2:]
result = new_string1 + " " + new_string2
print(result)

#5) write a python program to add "ing" at the end of a givin string(lenght should be at least 3) if the given string already endswith "ing" then add "ly" instead if the string lenght of the given string is less then 3, leave it unchanged.

string = input("enter a string: ")
if len(string) >=3:
    if string.endswith("ing"):
        string = string + "ly"
    else:
        string = string + "ing"
print(string)





#6)wriite a python program to find the first apperence of the substring 'not' dolows the "poor" replace the whole "not"....."poor" string
string = input("Enter a sentence: ")

if "not" in string and "poor" in string:
    
    not_pos = string.find("not")
    poor_pos = string.find("poor")
    
    if poor_pos > not_pos:
        string = string[:not_pos] + "good" + string[poor_pos + 4:]

print("Final string:", string)


#7) program to find gretest common divirsor of two numbers. For example , the GCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.


import math

num1 = int(input("enter a first number: "))
num2 = int(input("enter a second number: "))

print("GCD is:", math.gcd(num1, num2))



#8) write a python program to check whether a list contains a sublist.

main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

if str(sub_list)[1:-1] in str(main_list):
    print("sublist exists")
else:
    print("sublist does not exists")


#9) write a python program to find the second smallest number in list.

num = [5, 6, 8, 2, 3, 4, 7, 9, 5, 3, 2]
num = list(set(num))
num.sort()
print("second smallest number is :", num[1])


#10)write a python program to get unique values from a list.

number = [1, 1, 2, 2, 3, 5, 4]
unique_number = list(set(number))
print("unique value:", unique_number)

#11) write a python program to unzip a list of tuples into indibidual list.

data = [(1, 5), (2, 4), (3, 3)]

list1 = []
list2 = []

for item in data:
    list1.append(item[0])
    list2.append(item[1])
print(list1)
print(list2)    


#12) write a python program to convert a list of tupels into a dictionary.


data = [(7, "pen"), (5, "pencil"), (15, "eresor")]
result = dict(data)
print(result)


#13) write a python program to sort a dictionary (ascending/ descending) by value.




#14)write a python program to find the highest 3 value in a dictionary.

data = {'a' : 10, 'b': 30, 'c' : 20, 'd' : 40}
values = list(data.values())
values.sort()
print("highest 3 values:", values[-3:])

#15)given a number n, wriite a python program to make and print the list of fibonacci series up to n. input : n=7 Hint: first 7 numbers in the series Expected outpu:      First few fibonacci number are 0, 1, 1, 2, 3, 5, 8, 13.



n = int(input("enter number of terms: "))
a = 0
b = 1
print("first few fibonacci numbers are:")
for i in range(n):
    print(a, end=", ")
    c = a + b
    a = b
    b = c


#16) Counting the frequencies in a list using a dictionary in python. input: [1, 1, 1, 5, 5,3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

nums =  [1, 1, 1, 5, 5,3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
freq = {}
nums.sort()
for num in nums:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1
print(freq)


#17) Write a python program using function to find the sum of odd series and even seies
#odd series: 12/2! + 32/3! + 52/5! +.....n
#even series: 22/2! + 42/4! + 62/6!+......n



#18)   python program to find factorial of number using recursion

def fectorial(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n* fectorial(n-1)
n = int(input("enter a number: "))
result = fectorial(n)
print("fectorial is: ", result)



#19) write a python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list(set(lst))
numbers = [1, 2, 2, 4, 4, 5]
print(unique_list(numbers))


#20)