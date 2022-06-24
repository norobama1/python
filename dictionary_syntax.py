myDict = {
    "Naman" : "cute and sweet",
    "Cecilia" : "Stubborn",
    "Marks"  : [1,2,4],
    #nested dictionary
    "anotherdic" : {'Naman':'hot','Rajat' : 'Loser'}
 }

print(myDict['Naman'])
print(myDict['Cecilia'])
print(myDict['Marks'])
myDict['Marks'] = [45,77]   #cannot contain multiple keys
print(myDict['Marks'])
print(myDict['anotherdic'])
