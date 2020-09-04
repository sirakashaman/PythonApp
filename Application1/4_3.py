no = int(input("enter the number :"))
if(no%3==0 & no%5==0):
    print("zoom")
elif (no%3==0):
    print("zip")
elif(no%5==0):
    print("zap")
else:
    print("invalid")