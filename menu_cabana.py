print("                              ")
print("------------------------------")
print("THIS IS MY PYTHON FUNDAMENTALS")
print("------------------------------")

print(" Submitted by : Lovely Claire M. Cabana ")
print(" PROJECT IN ITCS102 ")

print("_______________________________________________________________")
print("                                                               ")
print(" THIS ARE THE EXAMPLES OF CODES THAT YOU MIGHT ENCOUNTER ")
print("_______________________________________________________________")
print("                                                               ")


def Arithmetic_operator():
    amount = int(input('enter your amount:' ))

    php1k = amount // 1000
    php5h = (amount % 1000)// 500
    php2h = (amount % 500)// 200
    php1h = (amount % 200)// 100
    php50 = (amount % 100 )// 50
    php20 = (amount % 20)// 50
    coin10 = (amount % 20)// 10
    coin5 = (amount % 10)// 5
    coin1 = (amount % 5)// 1

    

    print(f'1000:{php1k} \n 500:{php5h} \n 200:{php2h} \n 100:{php1h} \n 50:{php50} \n 20:{php20} \n 10:{coin10} \n 5:{coin5} \n 1:{coin1} \n')

def Comparison_operator():
    item = int(input('price of your item? '))
    quantity = int(input('how many is your item? '))

    price_item = item * quantity
    print("The total price of the item that you've bought" , price_item)

    discount = 0.10
    if price_item>= 100:
        disc = price_item * discount
        discounted_price = price_item - disc
        print("your total price with 10 percent discount is, " , discounted_price ) 
    else:
        print("no discount is applied", price_item )

def operator_1():
    print("______LOAN APPLICATION______")

    choice = input('Would you like to take a loan? \n1 - yes\n0 - No\n ---> ')

    if choice.isnumeric():

            if choice == '0':
                print('thank you, hope to see you again')

            elif choice == '1':
                name = input('Input your name --> ')
                loan_value = input('How much would you like to loan --> ')

                if loan_value.isnumeric():
                    months = input('How many months do you plan in paying the loan value? : ')
                    print('Please input a valid number of months ')
                else:
                    print('loan has a fix value of 5% interest per month ')
                
                    interest = int(loan_value) * 0.05
                    monthly = int(loan_value) / int(months)
                    monthly_amortization = monthly + interest 
                    print('Hi ', name,' your monthly amortization is ', monthly_amortization, 'php for the loan amount of' , monthly, 'php' )
            else:
                print('please input a valid monetary value')
    else:
        print('Only numeric value is accepted, please check your input')    

def conditional_1():
    age = input('what is your age ---> ')

    if age.isdigit():
        if int(age) >= 0 and int(age) <= 12:
            print('you are a child')

    if age.isdigit():
        if int(age) >= 13 and int(age) <= 19: 
            print('you are a teen')

    if age.isdigit():
        if int(age) >= 20 and int(age) <= 64:
            print('you are an adult')

    if age.isdigit():
        if int (age) >= 65:
            print('you are a senior')

    else:
        print('invalid input')

def conditional_2():
    year = input('what is your college year ? --> ')
    if year == 'freshmen':
        print('hi ! First year !! ')
    elif year == 'f':
        print('hi ! First year !! ')
    elif year == 'F':
        print('hi ! First year !! ')
    elif year == 'sophomore':
        print('hi ! Second Year !! ')
    elif year == 's':
        print('hi ! Second Year !! ')
    elif year == 'S':
        print('hi ! Second Year !! ')
    elif year == 'junior':
        print('hi ! Junior !!')
    elif year == 'j':
        print('hi ! Junior !!')
    elif year == 'J':
        print('hi ! Junior !!')
    elif year == 'senior':
        print('hi ! Senior !!')
    elif year == 'sr':
        print('hi ! Senior !!')
    elif year == 'Sr':
        print('hi ! Senior !!')

def While_loop():
    rapha = True
    larvin = 0
    neo = 0

    while rapha == True:
        num = input("enter a number -- >" )
        neo = neo + 1

        if num.isnumeric():
            larvin += int(num)
            ave = larvin / neo
            continue
        else:
            break
    print(ave)

def For_Loop1():
    for hello in range (1, 7):
        for deadznaako in range (1, hello):
            print("*", end= " ")
        print("*")
    for hi in range (7, 0, -1):
        for hello in range (1, hi):
            print("*", end= " ")
        print("*")

def For_Loop2():
    for cafe in range (1, 7):
        for coffeee in range (1, cafe):
            print(coffeee, end= " ")
        print()

def List_Example():
    def biodata (first_name, middle_initial, last_name, age, sex, height, weight, civil_status, birth_of_date, religion, nationality, gmail, contact_number, occupation, mothers_name, fathers_name):
        greet = " "
        if sex == "m" :
            greet = "Mr."
        else:
            greet = "Ms."
        print(f"Hi, Good Morning {greet}.{first_name}, {middle_initial}, {last_name}, {age}, {sex}, {height}, {weight}, {civil_status}, {birth_of_date}, {religion}, {nationality}, {gmail}, {contact_number}, {occupation}, {mothers_name}, {fathers_name}")

    first_name = input("what is yor name? ")
    middle_initial = input("what is your middle initial? ")
    last_name = input("what is your last name? ")
    age = int(input("how old are you? "))
    sex = input("sex? m/f" )
    height = int(input("what is your height? "))
    weight = int(input("what is your weight? "))
    civil_status = input("your civil status: ")
    birth_of_date = int(input("what is your birth date? "))
    religion = input("religion: ")
    nationality = input("what is your nationality? ")
    gmail = input("gmail" )
    contact_number = input("phone number: ")
    occupation = input("what is your occupation? ")
    mothers_name = input(" what is your mother's name? ")
    fathers_name = input(" what is your father's name?" )

    biodata (first_name, middle_initial, last_name, age, sex, height, weight, civil_status, birth_of_date, religion, nationality, gmail, contact_number, occupation, mothers_name, fathers_name)

def Another_Example():
    thislist = ["apple", "coffee", "milo", "milk"]
    print(thislist)

def Function():
    import random
    def sum (*numbers):
        sum = 0
        for each_num in numbers:
            sum += each_num
        return sum


    def right_triangle():
        for ayaw in range(1,6):
            for ko in range(1, ayaw):
                print("*", end = " ")
            print()

    def ayawkonamagcode():
        while True:
            secret = int(input("what is the number: "))
            tired = random.randint(1,10)

            if secret == tired:
                print("you are right")
                break
            else:
                print("engkkk, nice try")
                continue
    print(sum(5, 6, 76))
    right_triangle()
    ayawkonamagcode()           
    
def explanation():
    print("Function is defined using the 'DEF' key word")

def try_it():
    vanadium = []
    print("Enter your Python Code ( Please press Enter twice to execute your code): ")
    while True:
        line = input()
        if not line.strip():
            break
        vanadium.append(line)
    user_input = '\n'.join(vanadium)
    try:
        exec(user_input)
    except Exception as e:
        print("Error Code: ", e)

def menu():
    print("                      ")
    print("----------------------")
    print("----------------------")
    print("  Welcome to My Work  ") 
    print("----------------------")
    print("----------------------")
    print("______________________")
    print(" 1 - Print Statements ")
    print("______________________")
    print(" 2 - Variables        ")
    print("______________________")
    print(" 3 - Operators        ")
    print("______________________")
    print(" 4 - Conditionals     ")
    print("______________________")
    print(" 5 - Loops            ")
    print("______________________")
    print(" 6 - List             ")
    print("______________________")
    print(" 7 - Functions        ")
    print("______________________")
    print(" 8 - Exit             ")
    print("----------------------")
    print("----------------------")
    print(" 9 - Try It Now       ")
    print("----------------------")
    print("----------------------")

def Loops():
    print("-----------------------------------------")
    print("-1--> This is an Example of While Loop")
    print("-----------------------------------------")
    print("-2--> This is an Example of For Loop ")
    print("-----------------------------------------")
    print("-3--> This is an Example of For Loop ")
    print("-----------------------------------------")
    print("-4--> Exit")
    print("-----------------------------------------")

def Operators():
    print("---------------------------")
    print("-1--> Arithmetic Operator")
    print("---------------------------")
    print("-2--> Comparison Operator")
    print("---------------------------")
    print("-3--> Operator 1 Example")
    print("---------------------------")
    print("-4--> Exit")
    print("---------------------------")

def Conditionals():
    print("------------------------")
    print("-1--> Example number 1")
    print("------------------------")
    print("-2--> Example number 2")
    print("------------------------")
    print("-3--> Exit")
    print("------------------------")

def Lists():
    print("-------------------------------------")
    print("-1--> Example of List (BIODATA)")
    print("-------------------------------------")
    print("-2--> Example of List ")
    print("-------------------------------------")
    print("-3--> Exit")
    print("-------------------------------------")

def Functions():
    print("-------------------------------------------")
    print("-1--> Example of Functions")
    print("-------------------------------------------")
    print("-2--> Explantion ")
    print("-------------------------------------------")
    print("-3--> Exit")
    print("-------------------------------------------")

while True:
    menu()
    print()
    choice = input(" Please Select From The Options Above: ")

    if choice == "1":
        print("                                                         ")
        print(" Welcome this is My Python Program about Print Statement ")
        print("                                                         ")
        print(" --- EXAMPLE OF PRINT STATEMENT --- ")
        print(" ___________ ")
        print("|           |")
        print("|  OBJECTS  |")
        print("|___________|")
        print("                              ")
        print("------------------------------")
        print("Exameple: print('Hello World')")
        print("------------------------------")
        print("Output: Hello World "          )
        print("------------------------------")
        print("                              ")

        toExit = input("would you like to proceed to the main menu:( Y / N ): ")
        if toExit.lower() == "y":
            print("Program will now transfer to the main menu")
            continue
        else:
            print("---Code is now Ending---")
            break

    elif choice == "2":
        print("                                                   ")
        print(" Welcome this is My Python Program about Variables ")
        print("                                                   ")
        print(" --- EXAMPLE OF VARIABLES --- ")
        print("------------------------------------------")
        print(" Example:\n Name = 'Your Name' \n Section = 'Your section' \n Then print the variables")
        print("------------------------------------------")
        name = "My name is Lovely Claire M. Cabana"
        section = "From BSIT - 1C"
        print(name)
        print(section)
        print("------------------------------------------")
        print("                                          ")

        toExit = input("would you like to proceed to the main menu:( Y / N ): ")
        if toExit.lower() == "y":
            print("Program will now transfer to the main menu")
            #menu()
            continue
        else:
            print("---Code is now Ending---")
            break
    
    elif choice == "3":
        Operators()
        while True:
            print("---------------------------------------------------------")
            ope = input("What Operator Program would you like to open?: ")
            print("---------------------------------------------------------")
            if ope.isnumeric():
                if ope == "1":
                    Arithmetic_operator()
                    print("--- Code Ending --- ")
                    yes = input("Would you like to continue ( Y / N ): ")
                    if yes.lower() == "y" :
                        Operators()
                        continue
                    else:
                        print(" --- Code Ending --- ")
                        break
                elif ope == "2":
                    Comparison_operator()
                    print("--- Code Ending --- ")
                    yes = input("Would you like to continue ( Y / N ): ")
                    if yes.lower() == "y" :
                        Operators()
                        continue
                    else:
                        print(" --- Code Ending --- ")
                        break
                elif ope == "3":
                    operator_1()
                    print("--- Code Ending --- ")
                    yes = input("Would you like to continue ( Y / N ): ")
                    if yes.lower() == "y" :
                        Operators()
                        continue
                    else:
                        print(" --- Code Ending --- ")
                        break
                elif ope == "4":
                        print("--- PROGRAM TERMINATING ---")
                        break
                else: 
                    print("INVALID INPUT")
                    break
    elif choice == "4":
        Conditionals()
        while True:
                print("---------------------------------------------------------")
                con = input("What Loops Program would you like to open?: ")
                print("---------------------------------------------------------")
                if con.isnumeric():
                    if con == "1":
                        conditional_1()
                        print("--- Code Ending --- ")
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Conditionals()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif con == "2":
                        conditional_2()
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Conditionals()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif con == "3":
                        print("--- PROGRAM TERMINATING ---")
                        break
                    else: 
                        print("INVALID INPUT")
                        break
    elif choice == "5":
        Loops()
        while True:
                print("---------------------------------------------------------")
                Loop = input("What Loops Program would you like to open?: ")
                print("---------------------------------------------------------")
                if Loop.isnumeric():
                    if Loop == "1":
                        While_loop()
                        print("--- Code Ending --- ")
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Loops()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif Loop == "2":
                        For_Loop1()
                        print("--- Code Ending --- ")
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Loops()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif Loop == "3":
                        For_Loop2()
                        print("--- Code Ending --- ")
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Loops()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif Loop == "4" :
                        print("--- PROGRAM TERMINATING ---")
                        break
                    else: 
                        print("INVALID INPUT")
                        break
    elif choice == "6":
        Lists()
        while True:
                print("--------------------------------------------------------------------------------")
                print(" Append(): Adds an Elemenets to the end of a list")
                print("--------------------------------------------------------------------------------")
                print("Insert(): Inser an Element at a specific index in the list")
                print("--------------------------------------------------------------------------------")
                print("Remove(): Removes the first occurrence an element from the list ")
                print("--------------------------------------------------------------------------------")
                print(" Pop(): Removes the element at a specific index from the list and returns it")
                print("--------------------------------------------------------------------------------")
                print("Count(): Return the number of occurrence of an element in the list")
                print("--------------------------------------------------------------------------------")
                print("Index(): Returns the index first occurrence of an element in the list")
                print("--------------------------------------------------------------------------------")
                print("Sort(): Sorts the elements of the list in ascending order")
                print("--------------------------------------------------------------------------------")
                print("Copy(): Creates copy of the list")
                print("--------------------------------------------------------------------------------")
                print("Reverse(): Reverse the order of the elements in the list")
                print("--------------------------------------------------------------------------------")
                print("Extend(): Adds the elements in the list")
                print("--------------------------------------------------------------------------------")
                print("Clear(): Removes all the elements from the list")
                print("--------------------------------------------------------------------------------")
                print("---------------------------------------------------------")
                lst = input("What List Program would you like to open?: ")
                print("---------------------------------------------------------")
                if lst.isnumeric():
                    if lst == "1":
                        List_Example()
                        print("--- Code Ending --- ")
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Lists()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif lst == "2":
                        Another_Example()
                        print("--- Code Ending --- ")
                        yes = input("Would you like to continue ( Y / N ): ")
                        if yes.lower() == "y" :
                            Lists()
                            continue
                        else:
                            print(" --- Code Ending --- ")
                            break
                    elif lst == "3":
                        print("--- PROGRAM TERMINATING ---")
                        break
                    else: 
                        print("INVALID INPUT")
                        break
    elif choice == "7":
        Functions()
        while True:
            print("---------------------------------------------------------")
            fnc = input("What List Program would you like to open?: ")
            print("---------------------------------------------------------")
            if fnc.isnumeric():
                if fnc == "1":
                    Function()
                    print("--- Code Ending --- ")
                    yes = input("Would you like to continue ( Y / N ): ")
                    if yes.lower() == "y" :
                        Functions()
                        continue
                    else:
                        print(" --- Code Ending --- ")
                        break
                if fnc == "2":
                    explanation()
                    print("--- Code Ending --- ")
                    yes = input("Would you like to continue ( Y / N ): ")
                    if yes.lower() == "y" :
                        Functions()
                        continue
                    else:
                        print(" --- Code Ending --- ")
                        break
                if fnc =="3":
                    print("--- PROGRAM TERMINATING ---")
                    break
                else: 
                    print("INVALID INPUT")
                    break         
    elif choice == "8":
        print("-----------------------------------------")
        print("THAT'S ALL")
        print("THANK YOU FOR COMING, HOPE IT HELPS YOU")
        print("-----------------------------------------")
        break
    elif choice == "9":
        try_it()
        yes = input("Would you like to continue trying ( Y / N ): ")
        if yes.lower() == "y" :
            menu()
            continue
        else:
            print(" --- Code Ending --- ")
            break

    
        

                    



            




