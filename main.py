##
# Andy Moran
# 6/06/2022
# portfolio.py
# gameing
# variables, imports, constants etc.
options = ["Start", "Instructions", "Settings", "Quit"]
options_2 = ["View units", "Summary", "Continue"]
units = {"test 1": ["Infantry", 74, 71, 72, 5], "test 2": ["Artillery", 12, 11, 12, 2], "test 3": ["Armour", 8, 6, 7, 7]}
# key: Unit name: Unit type, Manpower, Equipment, Strength, Movement
MINI = 0
MENU_MIN = 1 
# Functions
def menu():
    print("""==========================================
            Title goes here :)          
==========================================""")
    y = 0
    for x in options:
        y += 1
        print("             {0}. {1}".format(y, x))
    return select_int(MENU_MIN, len(options))

def select_int(min:int, max:int):
    choice = min - 1
    while True:
        try:
            while choice < min or choice > max:
                choice = int(input("Choose a number: "))
            break
        except:
            print("Enter a full number")
    return choice

def start():
    print("Welcome to the gmae")
    print("You have {0} units".format(len(units)))
    print("Please select an option:")
    y = 0
    for x in options_2:
        y += 1
        print("{0}. {1}".format(y, x))
    return select_int(MENU_MIN, len(options_2))

def instructions():
    print('instructions')

def settings():
    print('settings')

# code
while True:
    choice = menu()
    if choice == 1:
        start()
    elif choice == 2:
        instructions()
    elif choice == 3:
        settings()
    elif choice == 4:
        print("goodbye")
        break
    else:
        print("something is brokie")
