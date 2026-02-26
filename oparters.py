#arithmetic operator
a = 5
b = 2
(a+b)
prinprintt(a-b)
print(a*b)
print(a/b)
print(a%b) #modulo : used to find remainder
print(a**b) # power : a to the power b

#relational operator
a = 50
b = 20
print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a <= b) #False
print(a < b)  #False
print(a > b)  #True

#Assignment operator
num = 10
num += 10
print("num :", num)
num = 10
num -= 10
print("num :", num)
num = 10
num *= 5
print("num :", num)
num = 10
num /= 5
print("num :", num)
num = 10
num %= 5 
print("num :", num)
num = 10
num **= 5
print("num :", num) 

#logial operator
print(not False )
print(not True)
a=50
b=30
print(not (a>b))
print(not(a<b))

val1= True
val2= True
print("and operator:",val1 and val2)
val1= True
val2= False
print("and operator:",val1 and val2)
val1= False
val2= False
print("and operator:",val1 and val2)

a=50
b=30
val1= False 
val2= False
print("OR Operator:", (a==b) or (val2))     #give true if one is true 
print("OR Operator:", (a>b) or (val2))