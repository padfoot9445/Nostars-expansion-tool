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

def relative_time(input):
    global three_digit_number
    try:
        with open("time.txt", "r") as f:
            content = f.read()
            three_digit_number = content[:3]
        
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("Could not parse three digit number from file")
    if "+" in input:
        time2 = int(readtime_three_digit(input[1:])) + int(three_digit_number)
        
        
        return time2
    else:
        print(input)
        time = readtime_three_digit(input)
        
        return time


    
if '__main__' == __name__:
    while 1:

       
        text_items_three = open("text_items.txt","r")
        text_items_contents = text_items_three.read()
        x = open("time.txt","r")
        y = ""
        for char in enumerate(x.readline()):
            if char[0] == 1:
                y += char[1]
            elif char[0] == 2:
                y += char[1]
                y += "."
            else:
                y += char[1]
            
        name = input(f"Please input the name of your construction below without any spaces and without repeating. There must not be numbers at the front of the name,\nthe time now is {y}\n")
        if " " in name:
            raise TypeError("There must not be any spaces in the name")
        if name in text_items_contents:
            raise ValueError("There must not be repeating names.")
        time = input("Please input the end time needed of your construction below in format 00.0 or enter the time needed in format +00.0\n")
        start_time_input = input("please enter the starting time of your construciton in similar format.")
        
        start_time = relative_time(start_time_input)
        total_time = int(readtime_three_digit(time[1:])) + int(start_time)
        
        
        
        items = open("items.py","a")
        output = f"{name} = Construction(\"{name}\", \"{total_time}\", \"{int(total_time)-int(three_digit_number)}\",\"{start_time}\", False)"
        items.write(f"{output}\n")
        items.close()
        text_items = open("text_items.txt","a")
        text_items.write(f"(items.{name},\"{name}\"),")
        text_items.close()
        text_items_two = open("text_items.txt","r")
        items_list = open("items_list.py","w")
        items_list.write(f"import items\n\nitems_list_list = [{text_items_two.read()[:-1]}]")
        items_list.close()
        text_items_two.close()
        print("\n item added to constructions list. Please enter next item or terminate program manually.\n")
    
    




