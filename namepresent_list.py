names = ['Naman','Hitansh','Norobama','Rajat','Tallen','Ceci']

name = input("Enter the name to check: \n")

if(name in names):
    print(name + " is present in the list")
else:
    print(name +" is not present in the list")