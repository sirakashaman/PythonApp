n = int(input("enter the no of subjects :"))
subMarks = []
credit = []
for i in range(n):
    subMarks[i] = int(input("enter the marks"))
    credit[i] = int(input("enter the credit "))

for i in range(n):
    print(subMarks[i])