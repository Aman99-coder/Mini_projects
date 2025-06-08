# if year divisible 4 & 400 it is a leap year
# if year divisible by 100 it is not a leap year.
a=int(input('Enter a Year:'))
if (a%4==0 and a%100!=0) or (a%400==0):
    print(f"{a} is a leap year..!! it contains 366 days..")
else:
    print(f"{a} is not a leap year.. it contains 365 days..")
