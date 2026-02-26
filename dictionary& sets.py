dict={
    "name":"Harshit",
    "age": 19,
    "cgpa": 98.3,
    "marks": 98, 
}
dict["subject"]= 7
print(dict)

nested dictionary 
dict={
    "name":"Harshit",
    "subject": {
        "phy": 97,
        "chem":98,
        "math":95
    }
}
print(dict["subject"]["chem"])

METHODS IN DICTIONARY
student={
   "name":"Harshit",
   "subject": {
        "phy": 97,
        "chem":98,
        "math":95
    }
}
print(student.keys()) 

student={
   "name":"rahul kumar",
   "subject": {
        "phy": 97,
        "chem":98,
        "math":95
    }
}
print(list(student.values())) 

student={
   "name":"rahul kumar",
   "subject": {
        "phy": 97,
        "chem":98,
        "math":95
    }
}
print(student.items())
or
student={
   "name":"rahul kumar",
   "subject": {
        "phy": 97,
        "chem":98,
        "math":95
    }
}
paris= list(student.items())
print(paris[0])                              #or we can use 1 too.

student={
   "name":"rahul kumar",
   "subject": {
        "phy": 97,
        "chem":98,
        "math":95
    }                                                                #if we use "name2" which didn't exist then  
}                                                                    #print(student[name2])will give us a error
print(student.get("name"))                                           #where as .get retruns none. 

student={
    "name":"rahul kumar",
    "subject": {
         "phy": 97,
         "chem":98,
         "math":95
    }
}
new_dict = {"name" : "neha kumar","age":19 }
student.update(new_dict)
print(student)


set
collection = {5,8,6,5,3,8,"hi","hello","hi"}
print(collection)
print(len(collection))                                           #its the total number of items

METHOD OF SETS
collection= set()
collection.add(5)
collection.add((3,4,3))
collection.add((3,4,3))
print(collection)

collection={5,8,6,5,3,8,"hi","hello","hi"}
collection.remove("hi")
collection.remove(5)
print(collection)

collection={5,8,6,5,3,8,"hi","hello","hi"}
collection.clear()
print(collection)

collection={5,8,6,5,8,"hi","hello","hi"}
print(collection.pop())
print(collection.pop())

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))

set1={1,2,3}
set2={2,3,4}
print(set1.intersection(set2))
"THE END."