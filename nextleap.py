Year=int(input("Enter the Year:"))
Count=20
Leap_Count=0
print("Leap Years:")
while(Leap_Count!=Count):
    if((Year%4==0 and Year%100!=0) or (Year%400==0)):
        Leap_Count+=1
        print(Year)
    Year=Year+1