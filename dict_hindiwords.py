#create a dictionary of hindi words which shows its meaning in english
myDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Khana" : "Food"
}

print("options are: ",myDict.keys())
a = input("Enter the hindi word:\n")
print("The meaning of your word is: ",myDict.get(a))
