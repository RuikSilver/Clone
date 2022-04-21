# CONVERSION CALCULATOR

def in_to_mm(inches):
    return inches * 25.4

def mm_to_in(mm):
    return mm / 25.4

def print_answer(num, conv_num, order_units):
    print(num, '=', conv_num)
    # assign num to in and conv_num to mm if order_units ==1
    # assign num to mm and conv_num to in if order_units ==2
    if order_units =='1':
        #in then mm
        num_units = 'in'
        conv_num_units = 'mm'
    if order_units =='2':
        #mm then in
        num_units = 'mm'
        conv_num_units = 'in'

while(True):
    # ask the user which conversion they want
    user_menu_selection = input('What type of conversion? (1-in to mm, 2-mm to in, Q -quit)')
    # if user selected 1 - in to mm
    converted_number = 0

    user_number = float(input ('What is your number?'))

    if user_menu_selection == '1':
        converted_number = in_to_mm(user_number)

    if user_menu_selection == '2':
        converted_number = mm_to_in(user_number)

    print_answer(user_number, converted_number, user_menu_selection)
     
    # if user selected Q - quit
    if user_menu_selection == 'Q' or user_menu_selection == 'q':
        break
    # exit the program