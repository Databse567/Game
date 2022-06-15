##
# Andy Moran
# 6/06/2022
# portfolio.py
# gameing
# variables, imports, constants etc.
from csv import unregister_dialect
import random
options = ["Start", "Instructions", "Settings", "Quit"]
options_2 = ["View units", "Summary", "Continue"]
unit_t_s = {"Infantry": [3, 10, "Dispersed", 2, 20, 1, 4], "Artillery": [10, 0, "Ranged", 1, 4, 0, 10]
, "Light Armour": [15, 6, "Mobile", 5, 10, 4, 7]}
# key: Unit Type: Attack, Defence, Ability, Mobility, Health, Armour, Penetration
units = {"test 1": ["Infantry", 5, "A"], "test 2": ["Artillery", 2, "B"]
, "test 3": ["Light Armour", 7, "C"]}
units_e = {"test 1_e": ["Infantry", 4, "1"], "test 2_e": ["Artillery", 1, "2"]
, "test 3_e": ["Light Armour", 6, "3"]}
# key: Unit name: Unit type, Manpower, Equipment, Strength, Movement
map = [[" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
["a", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["b", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["c", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["d", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["e", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["f", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["g", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["h", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["i", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["j", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
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

def map_f():
    print(" ".join(map[0]))
    print(" ".join(map[1]))
    print(" ".join(map[2]))
    print(" ".join(map[3]))
    print(" ".join(map[4]))
    print(" ".join(map[5]))
    print(" ".join(map[6]))
    print(" ".join(map[7]))
    print(" ".join(map[8]))
    print(" ".join(map[9]))
    print(" ".join(map[10]))

def place_unit_p():
    placed = False
    place = 0
    print("""enter the number corresponding to the the vertical number
that you want to place your unit on. i.e a -> 1, b -> 2""")
    for x in units:
        print("place unit {0}: ".format(x))
        while map[10][place] != ".":
            place = select_int(MENU_MIN, len(map[10])-1)
        map[10].pop(place)
        map[10].insert(place, units[x][2])
        map_f()

def place_unit_e():
    place = 0
    for x in units_e:
        while map[1][place] != ".":
            place = random.randint(MENU_MIN, len(map[1])-1)
        map[1].pop(place)
        map[1].insert(place, units_e[x][2])
        map_f()

def orderer():
    turn_order = {}
    turns = []
    val = []
    val_e = []
    units_k = list(units.keys())
    units_v = list(units.values())
    for x in units_v:
        val.append(x[1])
    units_e_k = list(units_e.keys())
    units_e_v = list(units_e.values())
    for x in units_e_v:
        val_e.append(x[1])
    y = 0
    for x in units_k:
        turn_order[val[y]] = x
        y += 1
    y = 0
    for x in units_e_k:
        turn_order[val_e[y]] = x
        y += 1
    keys = list(turn_order.keys())
    keys.sort(reverse = True)
    for x in keys:
        turns.append(turn_order[x])
    return turns

def stat_assi():
    stats = {}
    list1 = list(units.keys())
    list2 = list(units_e.keys())
    for x in order:
        if x in list1:
            type = units[x][0]
        elif x in list2:
            type = units_e[x][0]
        else:
            print("something is brokie")
        statis = unit_t_s[type]
        stats[x] = statis
    return stats

def find_p():
    pos ={}
    units_k = list(units.keys())
    units_o = []
    units_l = list(units.values())
    units_k_e = list(units_e.keys())
    units_o_e = []
    units_l_e = list(units_e.values())
    for x in units_l:
        units_o.append(x[2])
    for x in units_l_e:
        units_o_e.append(x[2])
    for x in map:
        for y in x:
            y = str(y)
            if y != "." and y not in map[0]:
                a = x.index(y)
                pos[y] = map.index(x), a
    return pos

def move(unit:str, name:str):
    position = list(pos[unit])
    mob = stats[name][3]
    print("""Unit {0} is at {1}. They can move {2} sqaures.
you will be asked to provide a left/right move and then an up/down move.
Right and down are negative, Up and left are positives."""
          .format(name, pos[unit], mob))
    moves = ask_for_move(unit, mob)
    moves = list(moves)
    ud = position[0] - moves[0]
    lr = position[1] - moves[1]
    if map[ud][lr] != ".":
        print("Space occupied")
        moves = ask_for_move(unit, mob)
        ud = position[0] - moves[0]
        lr = position[1] - moves[1]
    print(lr)
    map[ud][lr] = unit
    map[position[0]][position[1]] = "."

def ask_for_move(unit:str, movement:int):
    ver = 100000000000000
    hor = 100000000000000
    print("Vertical:")
    while pos[unit][0] - ver < 1 or pos[unit][0] - ver > 10:
        ver = select_int(-movement, movement)
        if pos[unit][0] - ver < 1 or pos[unit][0] - ver > 10:
            print("that would be deserting")
    print("Horizontal:")
    while pos[unit][1] - hor < 1 or pos[unit][1] - hor > 15:
        hor = select_int(-movement + ver, movement - ver)
        if pos[unit][1] - hor < 1 or pos[unit][1] - hor > 15:
            print("that would be deserting")
    return ver, hor

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

map_f()
place_unit_p()
place_unit_e()
order = orderer()
stats = stat_assi()
pos = find_p()
# game starts
turn = 1
while True:
    print("""########################
        Turn {0}
#######################""".format(turn))
    map_f()
    for x in order:
        if x in units:
            move(units[x][2],x)
        elif x in units_e:
            print("enemy move")
        map_f()
    pos = find_p()
    turn += 1

