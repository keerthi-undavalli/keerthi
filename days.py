Month=int(input("Enter the Month Number:"))
if(Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12):
    print("31 Days")
elif(Month==2):
    print("28 or 29 Days")
elif(Month==4 or Month==6 or Month==9 or Month==11):
    print("30 Days")
else:
    print("In-Valid Month Number ")