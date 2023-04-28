def readtime_three_digit(decimal_time):
    varreturn = ""
    for num in enumerate(decimal_time):
        if num[0] == 0 or num[0] == 1 or num[0] == 3:
            try:
                int(num[1])
            except:
                raise ValueError("There was something other than numbers where numbers should be")
            varreturn += num[1]
        else:
            if num[1] != ".":
                raise ValueError("missing \".\"")
        if num[0] == 3:
            try:
                int_num_3 = int(num[1])
                if int_num_3 != 1 and int_num_3 != 2 and int_num_3 != 3 and int_num_3 != 0:
                    raise ValueError("Decimal place must be either 0, 1, 2, or 3")
            except:
                raise ValueError("There was something other than a number in the decimal place (fourth character).")
    
    return varreturn

time = open("time.txt","w")
user_input_time = input("Enter your time here in AC format. AC is inputted in yy.x where x is the quadrant of the year we are in (the year is split into three-month groups, with ac 00.1 being march of the zeroeth year, and 00.2 being june, etc)\n")
try:
    time.write(readtime_three_digit(user_input_time))
    items = open("items.py","a")
    items.write(f"#the time is now {readtime_three_digit(user_input_time)}")
except:
    Exception("Something went wrong.")

time.close()
