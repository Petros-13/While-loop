number=int(input("Enter a number :"))
sum=0
x=number 
while x>0:
     y=x%10
     sum+=y**3
     x//=10
if number==sum:
    print(number,"is a armstrong number")
else:
    print(number,"Is not a armstrong number")