#Create an empty set
b = set()
print(type(b)) 

#adding values to the set
b.add(4)
b.add(5)
b.add(5)    #adding a value repeatedly does not changes a set
b.add((8,2,3))   #cannot add dictionary and list to a set 
b.add(7)
b.add(11)
print(b)

#length of the set
print(len(b)) #print the length of the set


#removal of a value from set
b.remove(7)
print(b)

#remove a random/arbitary value from set
print(b.pop())
print(b)

#to clear a set
b.clear()
print(b)
