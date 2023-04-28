import items
import items_list

def time_now():
    time_file = open("time.txt", "r")
    time_str = time_file.readline().strip()  # read first line and remove any trailing whitespace
    time_file.close()
    return time_str
def time_control():
    
    def read_time():
        time = open("time.txt","r")
        global list_of_times  # corrected variable name
        list_of_time1 = []
        for char in time.read():
            list_of_time1.append(int(char))
        decimal_base_four = list_of_time1.pop()  # corrected variable name
        
        
        list_of_times = [int(str(list_of_time1[0])+str(list_of_time1[1])),decimal_base_four]
        time.close()
    def check_finished():
    

        items_open = open("items.py", "a")
        for tuple in items_list.items_list_list:
            if int(tuple[0].total_time) <= int(time_now()) or int(tuple[0].time_remaining) < 0 or int(tuple[0].time_remaining) == 0:
                items_open.write(f"\n{tuple[0].name} = Construction(\"{tuple[0].name}\", \"{tuple[0].total_time}\", \"{000}\", \"{tuple[0].start_time}\", True)\n")
            # elif int(tuple[0].start_time)>int(time_now()):
            #     items_open.write(f"{tuple[0].name} = Construction(\"{tuple[0].name}\", \"{tuple[0].total_time}\", \"{000}\", \"{tuple[0].start_time}\", True)\n")
            else:
                # time_passed = int(time_now()) - int(tuple[0].start_time)
                new_time_remaining = int(tuple[0].total_time) - int(time_now())
                items_open.write(f"\n{tuple[0].name} = Construction(\"{tuple[0].name}\", \"{tuple[0].total_time}\", \"{str(new_time_remaining)}\", \"{tuple[0].start_time}\", {tuple[0].finished})\n")
        items_open.close()
    def time_shift():
        repeat()
        
        varreturn = ""
        read_time()
        ac_value = int(list_of_times[0])
        decimal_value = list_of_times[1]
        if decimal_value == 3:
            ac_value +=1
            decimal_value = 0
        elif decimal_value != 3:
            decimal_value +=1  # corrected increment value
        if ac_value <10:

            varreturn = "0"+str(ac_value)+str(decimal_value)
        else:
            varreturn = str(ac_value)+str(decimal_value)
        with open("time.txt","w") as file:
            file.write(varreturn)
        items_open = open("items.py","a")
        items_open.write(f"\n#The time is now {ac_value}.{decimal_value}\n   ")
        items_open.close()
        check_finished()

    def user_input_time_shift():
        read_time()
        add = input("Please input the amount of AC you wish to add onto the current time below in format 00.0 \n only AC input is allowed; dd/mm/yy is not.\n input below:\n")
        list1 = []
        for char in add:
            list1.append(char)
        list2 = []
        decimal_value = list1.pop()
        decimal_character = list1.pop()
        # corrected variable used for appending decimal
        list1.append(decimal_value)
    
        for char in list1:

            list2.append(int(char))
        decimal_amount = (((list2[0]*10+list2[1]))*4+ int(decimal_value))
        for i in range(int(decimal_amount)):  # corrected data type for range function
            time_shift()
        print("Time shifted successfully")  # added success message
    
    user_input_time_shift()     
    
    check_finished()
def check_started(start_time):
       
        time_int = int(time_now())
        if int(start_time) >= time_int:
            return False
        else:
            return True
def check_all():
    
    not_started = "IN QUEUE/NOT STARTED:\n\n"
    in_construction = "IN CONSTRUCTION:\n\n"
    finished = "FINISHED:\n\n"
    varreturn = ""
    for tuple in items_list.items_list_list:
        if not check_started(int(tuple[0].start_time)) and not tuple[0].finished:
            not_started +=f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {int(tuple[0].total_time) - int(time_now())} Start time: {tuple[0].start_time} Started: {check_started(int(tuple[0].start_time))} Finished {tuple[0].finished} \n "
        elif check_started(tuple[0].start_time) and not tuple[0].finished:
            in_construction +=f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {int(tuple[0].total_time) - int(time_now())} Start time: {tuple[0].start_time} Started: {check_started(int(tuple[0].start_time))} Finished {tuple[0].finished} \n "
        elif check_started(tuple[0].start_time) and tuple[0].finished:
            finished +=f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {000} Start time: {tuple[0].start_time} Started: {check_started(tuple[0].start_time)} Finished {tuple[0].finished} \n "
        elif not check_started(tuple[0].start_time) and not tuple[0].finished:
            print("DFSGFDHF")

        else:
            print("xyz")
            raise Exception("Line 103(or earlier), main.py, unknown error")
    varreturn += f"{not_started}\n{in_construction}\n{finished}"
     
    return varreturn

def check_one():
    name = input("What is the item name? (Capitalization and space sensitive) \n")
    for tuple in items_list.items_list_list:
        if name in tuple:
            
            return f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {int(tuple[0].total_time) - int(time_now())} Start time: {tuple[0].start_time} Started: {check_started(tuple[0].start_time)} Finished {tuple[0].finished} \n "
def check_type():
    varreturn = ""
    type = input("Which type? \n1:not started \n2:in construction \n3:finished\n")
    if int(type) == 1:
        varreturn += "NOT STARTED\n"
        for tuple in items_list.items_list_list:
            if not check_started(int(tuple[0].start_time)) and not tuple[0].finished:
                varreturn +=f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {int(tuple[0].total_time) - int(time_now())} Start time: {tuple[0].start_time} Started: {check_started(int(tuple[0].start_time))} Finished {tuple[0].finished} \n "
    elif int(type) == 2:
       for tuple in items_list.items_list_list:
        if check_started(tuple[0].start_time) and not tuple[0].finished:
                varreturn +=f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {int(tuple[0].total_time) - int(time_now())} Start time: {tuple[0].start_time} Started: {check_started(int(tuple[0].start_time))} Finished {tuple[0].finished} \n "  
    elif int(type) == 3:
        for tuple in items_list.items_list_list:
            if check_started(tuple[0].start_time) and tuple[0].finished:
                varreturn +=f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {000} Start time: {tuple[0].start_time} Started: {check_started(tuple[0].start_time)} Finished {tuple[0].finished} \n "
    
    return varreturn
            



def readtime_file():
    time_file = open("time.txt","r")
    time_str = time_file.readline()
    time_int = int(time_str.strip())
    time_file.close()
    return time_int
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
def read_time_file():
        with open("time.txt","r") as file:
            time_int = int(file.readline().strip())
            return time_int 
def repeating_items(): 
    import repeating_items_list
    
    global new_repeating_item
    def update_list():
        with open("text_repeating_items.txt","r") as file1:
            text = file1.readline()
            with open("repeating_items_list.py","w") as file:
                file.write(f"import repeating_items\n\nrepeating_items_list_list = [{text[:-1]}] ")
    def new_repeating_item():        
        name = input("Enter the name of the item you want to repeat here:\n")
        
        if name in repeating_items_list.repeating_items_list_list:
            raise ValueError("item already repeating")
        #name, times, amount, interval, multiplier, cap
        interval = readtime_three_digit(input("Enter the interval below in 00.0 format."))
        multiplier = input("Enter the multiplier (amount of items per construction) here:\n")
        cap = input("Enter the amount of times this should repeat. If there is no upper limit, enter False.\n")
        with open("repeating_items.py","a") as items:
            items.write(f"\n{name} = construction_repeat(\"{name}\", 0, 0, \"{interval}\", {multiplier}, {cap}, items.{name}, )")
        with open("text_repeating_items.txt","a") as file:
            file.write(f"(repeating_items.{name},\"{name}\"),")
        repeat()
        update_list()
    update_list()
    
    global repeat
    def repeat():
        
        for tuple in enumerate(repeating_items_list.repeating_items_list_list):
            #check if the thing in normal items is finished
            if tuple[1][0].reference.finished:
                #check if there is a cap
                if not tuple[1][0].cap:
                    #check if the amount of times repeated is not equal to or above the cap
                    if not tuple[1][0].times == tuple[1][0].cap or not tuple[1][0].times > tuple[1][0].cap:
                        #new name
                        name = f"{tuple[1][0].name[:-1]}{int(tuple[1][0].name[-1:]) + 1+tuple[0]}"
                        #update repeating items

                        #update repeating_items.py
                        with open("repeating_items.py","a") as repeating:
                            
                            repeating.write(f"\n{tuple[1][0].name} = construction_repeat(\"{tuple[1][0].name}\", {tuple[1][0].times + 1}, {tuple[1][0].times * tuple[1][0].multiplier}, \"{tuple[1][0].interval}\", {tuple[1][0].multiplier}, {tuple[1][0].cap}, items.{name}, )\n")
                        #update items

                        #update items.py
                        with open("items.py","a") as items:
                            items.write(f"\n{name} = Construction(\"{name}\", \"{tuple[1][0].reference.total_time}\", \"{int(tuple[1][0].reference.total_time) - read_time_file()}\",\"{int(tuple[1][0].reference.total_time) + int(tuple[1][0].interval)}\", False)\n")
                        #update text_items.txt
                        with open("text_items.txt","a") as file:
                            file.write(f"(items.{name},\"{name}\"),")
                        update_list()
    global check_repeating
    #name, times, amount, interval, multiplier, cap
    def check_repeating():
        varreturn = ""
        
       
        for tuple in repeating_items_list.repeating_items_list_list:
            if not tuple[0].cap:
                cap = "None"
            else: 
                cap = str(tuple[0].cap)
            varreturn += f"NAME: {tuple[0].name}  TIMES: {tuple[0].times} AMOUNT: {tuple[0].amount} INTERVAL: {tuple[0].interval} AMOUNT PER BATCH: {tuple[0].multiplier} MAX ITERATIONS: {cap}\n"
        return varreturn
    global single_check_repeating
    def single_check_repeating():
        search_name = input("input the item you wish to search for here:\n")
        
        for tuple in repeating_items_list.repeating_items_list_list:
            if not tuple[0].cap:
                cap = "None"
            else: 
                cap = str(tuple[0].cap)

            if search_name in tuple:
                return f"NAME: {tuple[0].name}  TIMES: {tuple[0].times} AMOUNT: {tuple[0].amount} INTERVAL: {tuple[0].interval} AMOUNT PER BATCH: {tuple[0].multiplier} MAX ITERATIONS: {cap}\n"
        return "Item not found."
            
            





        

                
                

                


    





    #name, times, amount, interval, multiplier, cap, reference
    # name, total_time, time_remaining, start_time, finished    
def items_control():
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
    items.write(f"\n{output}\n")
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
    
    




   


        

def main():
    repeating_items()
    with open("output_for_copying.txt","w") as file:
        
        main_input1 = input(f"The time now is {read_time_file()} Choose an option, and type in the relevant number.\n1:Increase the time\n2:non-repeating things \n3:repeating things\nenter your choice below:\n")
        
        try:
            main_input = int(main_input1)
        except:
            Exception("Wrong input")
        
        if main_input == 1:
            time_control()
        elif main_input == 2:
            singular_input_one = input("Choose an option, and type in the relevant number.\n1:check all constructions\n2.check a singular type of construction\n3.check a singular item\n4:new singular item\nenter your choice below:\n")
            try:
                singular_input = int(singular_input_one)
            except:
                ValueError("Wrong input")
            if singular_input == 1:
                a = str(check_all())
                print(a)
                file.write(a)
            elif singular_input == 2:
                a = str(check_type())
                print(a)
                file.write(a)
            elif singular_input == 3:
                a = str(check_one())
                print(a)
                file.write(a)
            elif singular_input == 4:
                items_control()
                
            else:
                print("Wrong input, try again.")
        elif main_input == 3:
            
            repeating_input_one = input("Choose an option, and type in the relevant number.\n1:make an one-off item repeating(you cannot create from scratch)\n2.check all repeating constructions\n3.check a singular repeating item\nenter your choice below:\n")
            try:
                repeating_input = int(repeating_input_one)
            except:
                ValueError("Wrong input")
            if repeating_input == 1:
                new_repeating_item()
            elif repeating_input == 2:
                a = check_repeating()
                print(a)
                file.write(a)
            elif repeating_input == 3:
                a = single_check_repeating()
                print(a)
                file.write(a)
            else:
                print("Wrong input, try again.")
            
        else: 
            print("Wrong input, try again.")
while 1:
    main()
    print("Restarting...")
# def main():
#     time_control()
# while 1:
#     main()

