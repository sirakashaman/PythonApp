dist = int(input("Enter the distance :"))
total_dist = 2*dist
cost_of_petrol=int(input("enter the cost :"))
mileage = 12
Amount_petrol_required= total_dist/mileage
total_cost = cost_of_petrol*Amount_petrol_required
each_shares = total_cost/4
if (each_shares%5==0):
    print(each_shares)
    print("true")
else:
    print("false")