#Pratice serise

#1
# WAP to check if a number entered by the user is odd or even.
num= int(input("Enter a number "))
if(num%2==0):
    print("even")
else:
    print("odd")

#2
# WAP to find the greatest of 3 numbers entered by the user.
a=int(input("Enter frist value: "))
b=int(input("Enter second value: "))
c=int(input("Enter thrid value: "))
if(a>b and a>c):
    print("The Largest number is: ",a)
elif(b>a and b>c):
    print("The Largest number is: ",b)
elif(c>b and c>a):
    print("The Largest number is: ",c)

#3
# WAP to check if a number is a multiple of 7 or not.
num = int(input("enter a number"))
f= num%7
if(f==0):
    print("number is muitple of 7")
else:
    print("number is not a mutiple of 7")

#4
# True or False
a= int(input("Enter the frist number : "))
b= int(input("Enter the second number : "))
print(a>=b)

#5
# sum a&b
a= int(input("Enter the frist number : "))
b= int(input("Enter the second number : "))
print("sum of two number : ",a+b)

#6
# 2 number average 
a= int(input("Enter the frist number : "))
b= int(input("Enter the second number : "))
print("sum of two number : ",a+b)

#7
# area of a square
a= int(input("Enter the frist number : "))
b= int(input("Enter the second number : "))
print("sum of two number : ",a+b)

#8
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
a = input("Enter the name of frist movies: ")                              movies=[]
b = input("Enter the name of second movies: ")                             movies.append(input("Enter the name of frist movies: "))
c = input("Enter the name of thrid movies: ")                              movies.append(input("Enter the name of second movies: "))
                                                       #or
list =[a,b,c]                                                            movies.append(input("Enter the name of thrid movies:"))
print(list)                                                                print(movies)
print(type(list))

#9
# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method)
#palindrome= word that spells out the same from either side. e.g
# racecar, maam, 1221 
list1 = [9,2,9]
copy_list= list1.copy()
copy_list.reverse()
if(copy_list==list1):
    print("Palindrome")
else:
    print("Not Palindrome")

#10
# WAP to count the number of students with the “A” grade in the following tuple.  [”C”,“D”,“A”,“A”,“B”,“B”,“A”]
list=["C","D","A","A","B","B","A"]
print(list.count("A"))

#11
# Store the above values in a list & sort them from “A” to “D”
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)

#12
#Store the word meanings in a python dictionary :table:“a piece of furniture”,“list of facts&figures”,cat:“a small animal”
dict={
    "table":("a piece of furniture","list of facts & figures"),
    "cat" : "a small animal",
}
print(dict)

#13
#You are given a list of subjects for students. Assume one classroom is required for 1subject. 
#How many classrooms are needed by all students.”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
dict= {
    "C1":"PYTHON",
    "C2":"C++",
    "C3":"JAVA",
    "C4":"JAVASCRIPT",
    "C5":"C",
}
print(len(dict))
                                                #or in set
subject={
    "python","java","C++","python","javascript","java","python","java","C++","C"
}
print(len(subject))

#14
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}
x= int(input("ENTER THE MARK"))
marks.update({"chem":x})
y= int(input("ENTER THE MARK"))
marks.update({"phy":y})
z= int(input("ENTER THE MARK"))
marks.update({"maths":z})
print(marks)

#15
# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)
value={9,"9.0"}
print(value)
                                                      # or
value={
    ("float",9.0),
    ("int",9)
}
print(value)
print(type(value))

