Num=int(input("enter the integer:"))
EvenDigitCount=0
Rem=0
while(Num!=0):
    Rem=Num%10
    if(Rem%2==0):
        EvenDigitCount+=1
    Num=Num//10
print("number of Even Digits are",EvenDigitCount)