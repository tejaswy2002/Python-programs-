year=int(input("enter the year:"))
if(year<=0):
    print("invalid")
elif(year%4==0):
        print("the year is leap year")
else:
            print("the year is not a leap year")
OUTPUT:
  enter the year:1947
the year is not a leap year
