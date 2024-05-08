#create a new file in python in add some following data.
'''with open("priactice.txt","w") as f:
    f.write("hii everyone \n we are learning python i/o\n")
    f.write("usig java \n i like to program in java")'''
    
#waf that repalce all accurance to replace "java" into "python in txtg file"
with open("priactice.txt","r") as f:
    data = f.read()
    
new_data=data.replace("java","python")
print(new_data)

with open("priactice.txt","w") as f:
    f.write(new_data)
    
#search the word "learning" exist in the file or not
word="learning"
with open("priactice.txt","r") as f:
    data=f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

    