year = 2000

if year % 4 == 0 and year % 100 != 0:
    print("Year is leap")
elif year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")


# if not year % 4 and year % 100:
#     print("Year is leap")
# elif not year % 400:
#     print("Year is leap")
# else:
#     print("Year is not leap")
