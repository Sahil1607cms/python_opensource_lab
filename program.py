# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("----Lists----")
li=["Sahil","Priyansh","Hardik","Krishna","Sethi","Anish","Rahul","Rautela","Shaurya","Vansh"]
print(li[0])
print(li[-1])
print(li[3:6])
print(li[::-1])
print(li[8:3:-1])
print("\n")

print("----Tuples----")
tup=("Sahil","Priyansh","Hardik","Krishna","Sethi","Anish","Rahul","Rautela","Shaurya","Vansh")
print(tup)
# tuples are immutable    
# adding Harshit
tup=tup+('Harshit',)
print(tup)
# removing Harshit
litup=list(tup)
litup.pop()
tup=tuple(litup)
print(tup)
print(tup[1:4])
# cant modify a index in tuple without converting it to a list and then back to tuple

print("dictionary")
students = {
    "Sahil": 19,
    "Priyansh": 21,
    "Hardik": 20,
    "Krishna": 22,
    "Sethi": 18
}
for name,age in students.items():
    if age>20:
        print(f"{name} is {age} years old")

students["Amit" ] = 30
del students["Sethi"]
average_age = sum(students.values())/len(students)
print(f" Average age of students in the dictionary is {average_age}")

li=[1,2,3,4,5,6,7,8,9,10]
for i in li:
    if i%2==0:
        print(i)

li=[1,1,2,3,3,4,4,5,6,7,7]
seen =set()
duplicate = set()
for item in li:
    if item in seen:
        duplicate.add(item)
    else:
        seen.add(item)
print(f"Duplicate elements {duplicate}")

name= "Elephant"
print(f"Reversed string is {name[::-1]}")



