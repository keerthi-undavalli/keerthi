Num=int(input("enter the number:"))
EvenSum=0
OddSum=0
for i in range(1,Num+1):
    if(i%2==0):
        EvenSum+=i
    else:
        OddSum+=i
print("Even Sum",EvenSum)
print("Odd Sum",OddSum)