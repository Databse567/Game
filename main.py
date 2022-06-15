##
# Andy Moran
# 6/06/2022
# portfolio.py
# gameing
# variables, imports, constants etc.
import random
options = ["Start", "Instructions", "Settings", "Quit"]
options_2 = ["View units", "Summary", "Continue"]
units = {"test 1": ["Infantry", 74, 71, 72, 5, "A"], "test 2": ["Artillery", 43, 11, 12, 2, "B"], "test 3": ["Light Armour", 17, 6, 7, 7, "C"]}
units_e = {"test 1": ["Infantry", 74, 71, 72, 4, "1"], "test 2": ["Artillery", 43, 11, 12, 1, "2"], "test 3": ["Light Armour", 17, 6, 7, 6, "3"]}
# key: Unit name: Unit type, Manpower, Equipment, Strength, Movement
map_n = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
map_1 = ["a", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_2 = ["b", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_3 = ["c", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_4 = ["d", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_5 = ["e", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_6 = ["f", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_7 = ["g", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_8 = ["h", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_9 = ["i", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
map_10 = ["j", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
MINI = 0
MENU_MIN = 1 
go = False
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

def view():
    print("Here is a list of your units")
    for x in units:
        print("Unit {0}".format(x))
        print("Unit Type: {0}".format(units[x][0]))
        print("Unit Manpower: {0}".format(units[x][1]))
        print("Unit Equipment: {0}".format(units[x][2]))
        print("Unit Strength: {0}".format(units[x][3]))
        print("Unit Movement: {0}".format(units[x][4]))

def map():
    print(" ".join(map_n))
    print(" ".join(map_1))
    print(" ".join(map_2))
    print(" ".join(map_3))
    print(" ".join(map_4))
    print(" ".join(map_5))
    print(" ".join(map_6))
    print(" ".join(map_7))
    print(" ".join(map_8))
    print(" ".join(map_9))
    print(" ".join(map_10))

def place_unit_p():
    placed = False
    place = 0
    print("""enter the number corresponding to the the vertical number
that you want to place your unit on. i.e a -> 1, b -> 2""")
    for x in units:
        print("place unit {0}: ".format(x))
        while map_10[place] != ".":
            place = select_int(MENU_MIN, len(map_10))
        map_10.pop(place)
        map_10.insert(place, units[x][5])
        map()

def place_unit_e():
    place = 0
    for x in units_e:
        while map_1[place] != ".":
            place = random.randint(MENU_MIN, len(map_1))
        map_1.pop(place)
        map_1.insert(place, units_e[x][5])
        map()

def orderer():
    turn_order = {}
    turns = []
    units_k = list(units.keys())
    units_v = list(units.values())
    units_e_k = list(units_e.keys())
    units_e_v = list(units_e.values())
    print(units_k)
    print(units_v)
    y = 0
    for x in units_v:
        turn_order[units_k[y]] = x[4]
        y += 1
    y = 0
    for x in units_e_v:
        turn_order[units_e_k[y]] = x[4]
        y += 1
    print(list(turn_order.values()))
    for x in list(turn_order.values()):
        turn = max(turn_order)
        turns.append(turn)
        turn_order.pop(turn)
    print(turns)


def summary():
    print("summary")

def instructions():
    print('instructions')

def settings():
    print('settings')

# code
while go is not True:
    choice = menu()
    if choice == 1:
        go = True
    elif choice == 2:
        instructions()
    elif choice == 3:
        settings()
    elif choice == 4:
        print("goodbye")
        break
    else:
        print("something is brokie")
go = False
while go is not True:
    choice = start()
    if choice == 1:
        view()
    elif choice == 2:
        summary()
    elif choice == 3:
        go = True
    else:
        print("something is brokie")
map()
place_unit_p()
place_unit_e()
orderer()