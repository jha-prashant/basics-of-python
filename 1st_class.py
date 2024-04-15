str = "prashant jha"
print(str[5:6])

str1="haldia"
print(str1[-4:-1])

str2="my name is prashant jha"
str2=str2.replace("jha","kumar")
print(str2)

name=input("type your name here")
print(name)
print(len(name))

name=name.count("a")
print(name)

light="green"
if (light =="green"):
    print("go")
elif (light == "red"):
    print("stop")
elif (light =="yellow"):
    print("slow down")
else:
    print("light's are damaged")
    