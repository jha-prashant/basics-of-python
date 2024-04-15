#Q1> store wordmining in python dictonary:
dict1={
    "table":["a pice of furniture","list of fact & figure"],
    "cat":["a small animal"],
}
print(dict1)

# Q2>you are given a list of a sub. for student ,assume one classroom is requird  for 1 sub./n
# . how many class room are needed by all stuedent
sub={"python","java","c","python","java","python","html","java" }
print(len(sub))
print(sub)
#that mins we need 4 classroom to read sub.

'''Q3> WAP to to enter marks of 3 sub from the user and store tham in the dictionary
start  with an empety dict.. and add one by one use sub name as key  and marks as a value'''

marks = {}
x = int(input("enter phy marks"))
marks.update({"phy":x})

y = int(input("enter chem marks"))
marks.update({"chem":y})

z = int(input("enter math marks"))
marks.update({"math":z})

print(marks)

'''figure out a way to store 9 and 9.0 saparate values in the set'''
value = {
    ("float",9.0),
    ("int",9),
}
print(value)


