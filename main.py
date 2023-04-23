import items
import items_list
output = open("output_for_copying.txt","w")
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

    def time_shift():
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
        time2 = open("time.txt","w")
        time2.write(varreturn)
        time2.close()  # added file close statement
        items_open = open("items.py","a")
        items_open.write(f"#The time is now {ac_value}.{decimal_value}   ")
        items_open.close()

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
    def check_finished():
    

        items_open = open("items.py", "a")
        for tuple in items_list.items_list_list:
            if int(tuple[0].total_time) <= int(time_now()):
                items_open.write(f"{tuple[0].name} = Construction(\"{tuple[0].name}\", \"{tuple[0].total_time}\", \"{000}\", \"{tuple[0].start_time}\", True)\n")
            # elif int(tuple[0].start_time)>int(time_now()):
            #     items_open.write(f"{tuple[0].name} = Construction(\"{tuple[0].name}\", \"{tuple[0].total_time}\", \"{000}\", \"{tuple[0].start_time}\", True)\n")
            else:
                # time_passed = int(time_now()) - int(tuple[0].start_time)
                new_time_remaining = int(tuple[0].total_time) - int(time_now())
                items_open.write(f"{tuple[0].name} = Construction(\"{tuple[0].name}\", \"{tuple[0].total_time}\", \"{str(new_time_remaining)}\", \"{tuple[0].start_time}\", {tuple[0].finished})\n")
        items_open.close()
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
    output.write(varreturn)    
    return varreturn

def check_one():
    name = input("What is the item name? (Capitalization and space sensitive) \n")
    for tuple in items_list.items_list_list:
        if name in tuple:
            output.write(f" {tuple[0].name}: Finishing time: {tuple[0].total_time}  Time remaining: {int(tuple[0].total_time) - int(time_now())} Start time: {tuple[0].start_time} Started: {check_started(tuple[0].start_time)} Finished {tuple[0].finished} \n ")
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
    output.write(varreturn)
    return varreturn
            
        
            

        


def main():
    
    main_input1 = input("Choose an option. type in the identifier(for example, for increasing the time, type \"1\"\n1:increase the time\n2: print out the entire list of active, finished, and pending constructions \n 3: print out a specific construction item\n4:check only a single type of item\nenter your choice below:\n")
    try:
        main_input = int(main_input1)
    except:
        ValueError("Wrong input")
    if main_input == 1:
        time_control()
    elif main_input == 2:
        print(check_all())
        output.write(check_all())
        
    elif main_input == 3:
        print(check_one())
    elif main_input == 4:
        print(check_type())
    else: 
        print("Wrong input, try again.")
while 1:
    main()
    print("Restarting...")
# def main():
#     time_control()
# while 1:
#     main()
output.close()
