age = int(input("Enter your age "))
if(age>= 18):
    print("can drive")
elif(age< 18):
    print("cannot drive")

age = 18
if(True):
    print("can vote")

light= input("Enter colour of light: ")
if(light== "red"):
    print("stop")
elif(light== "green"):
    print("go")
elif(light== "yellow"):
    print("wait")
else:
    print("light is broken ")
print("end of code")


marks= int(input("Enter the marks of student= "))
if(marks>= 90):
    grade= "A"
elif(marks>= 80 and marks<90):
    grade= "B"
elif(marks>= 70 and marks<80):
    grade= "C"
else:
    grade= "D"
print("garde of the student -> ",grade)


Nesting


age = 95
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")