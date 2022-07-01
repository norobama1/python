
sub1 = float(input("Enter the marks of subject 1: "))
sub2 = float(input("Enter the marks of subject 2: "))
sub3 = float(input("Enter the marks of subject 3: "))

overall = (sub1+sub2+sub3)/3

if(sub1<33 or sub2<33 or sub3<33):
    print(" you failed your exam because you have less than 33% in one of the subject")
elif(overall<40):
    print(" you failed your exam because you have less than 40% overall")
else:
    print("you passed")


