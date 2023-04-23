import items_control 

time = open("time.txt","w")
user_input_time = input("Enter your time here in AC format. AC is inputted in yy.x where x is the quadrant of the year we are in (the year is split into three-month groups, with ac 00.1 being march of the zeroeth year, and 00.2 being june, etc)\n")
try:
    time.write(items_control.readtime_three_digit(user_input_time))
    items = open("items.py","a")
    items.write(f"#the time is now {items_control.readtime_three_digit(user_input_time)}")
except:
    Exception("Something went wrong.")

time.close()
