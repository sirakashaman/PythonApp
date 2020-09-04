x= int(input("enter the 5 rupee coin :"))
y= int(input("enter the 1 rupee coin :"))
z= int(input("enter the amount to be fullfilled in mnimum no if coins :"))
no_of_onecoin_required = z%5
no_of_fivecoin_required = z//5


if(x>=no_of_fivecoin_required):
    if (y>=no_of_onecoin_required):
        print("The no of one rupee coin :")
        print(no_of_onecoin_required )
        print("The no of five rupee coin :")
        print(no_of_fivecoin_required )
    else: 
        print("not possible")
elif(x<no_of_fivecoin_required):
    b=no_of_fivecoin_required-x
    a=(no_of_fivecoin_required-x)*5+no_of_onecoin_required
    if (y>=a):
        print("The no of one rupee coin :")
        print(a )
        print("The no of five rupee coin :")
        print( x )
    else:
        print("not possible")


 