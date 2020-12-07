#Armstrong number- 153--1*3+53+3*3=153
lower_limit=int(input("enter lower limit" ))
higher_limit=int(input("enter lower limit" ))
perfect=[]
armstrong=[]
for i in range(lower_limit,higher_limit): # generating number
    length=len(str(i)) # type casting to str 
    
    temp=i
    sum1=0
    sum2=0
    for j in range(1,i): # to findout factors 
        if(i%j==0):
            sum1+=j
    if sum1==i:
            perfect.append(i)
    while i>0:
        digit=i%10
        sum2+=digit**length
        i=i//10
        if sum2==temp:
            armstrong.append(temp)
 
print("perfect nos=",perfect)
print("armstrong nos=",armstrong)