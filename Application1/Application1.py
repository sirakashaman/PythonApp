lower_limit = int(input("enter a num :-"))
upper_limit = int(input("enter a num :-"))
# num= int(input("enter a num :-"))
j=2
for i in range(lower_limit,upper_limit+1):
   
   while(j<i):
      if(i%j==0):
         #print( i ,end=" is not a prime no  ")
         break
      else:
         if(j== i-1):
            print(i, end=" is prime  ")
         j+=1
   i+=1
   j=2