myDict = {
     "Naman" : "cute and sweet",
    "Cecilia" : "Stubborn",
    "Marks"  : [1,2,4],
    #nested dictionary
    "anotherdic" : {'Naman':'hot','Rajat' : 'Loser'},
    1 :2
 }

 #dictionary Methods
print(myDict.keys())  #print the keys of the dictionary
print(type(myDict.keys()))  #print the typecast
print(list(myDict.keys()))    #print the keys of the dictionary in list
print(list(myDict.values()))  #print the values of the dictionary
print(myDict.items())    #print the (key,values) for all contents of the dictionary


updatedict = {
    "Hitansh" : "brother",
    "Cecilia"  : "more stubborn"
}
myDict.update(updatedict)  #update the dictionary by adding key-values from updatedict 
                           # can update the values from previous dictionary
print(myDict)
print(myDict.get("Naman"))



              #differenec between .get method and [] syntax in Dictionaries:
print(myDict.get("Naman2"))   #it will return none as naman2 is not present in the dictionary
print(myDict["Naman2"])  #it will throw an error as naman2 is not present in dictionary

                         #thats why we use get method to prevent from showing a error


