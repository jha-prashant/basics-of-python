collection={3,4,3,5,7}
print(collection)
print(type(collection))


#ignore duplicate value
items = { "hello","prashant",44,5,3,6,3,5,5,"haldia",98.87}
print(items)
print(len(items))

# empty set
pair=set()
#methods
pair.add(1)
pair.add(2)
pair.add(2)
pair.add((2,3,4))
pair.add("prashant")
print(pair)
print(pair.clear())

#union & intersaction
set1={1,2,3}
set2={2,4,5}
print(set1.union(set2))

print(set1.intersection(set2))