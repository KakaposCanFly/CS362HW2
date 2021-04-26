#This program determines whether an inputted year is a leap year or not
#This program does NOT user error handling

year = int(input("Please enter the year (eg 20XX): "))

if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print(year, "is a leap year!")
        else:
            print(year, "is not a leap year!")
    else:
        print(year, "is a leap year!")
else:
    print(year, "is not a leap year!")