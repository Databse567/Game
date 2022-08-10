##
# Andy Moran
# 6/06/2022
# portfolio.py
# gameing
# variables, imports, constants etc.
from ast import Break
from csv import unregister_dialect
from xml.sax.handler import DTDHandler
from maps import *
from divisions import *
import random
import time
import os
sold = []
money = 100000000
options = ["Start", "Instructions", "Settings", "Quit"]
options_2 = ["View units", "Summary", "Shop", "Continue"]
settings_o = ["Controls", "Cancel"]
features = {"~":"Water", "/":"Cliff","Ð":"Dune", "■": "Wall"}
direction = {"Forward": "W", "Left": "A", "Back": "S", "Right": "D", "Stop": "Q"}
unit_t_s = {"Infantry": [3, 10, "Dispersed", 2, 10, 1, 4, 2], "Artillery": [10, 0, "Ranged", 1, 3, 0, 10, 5]
, "Light Armour": [15, 6, "Mobile", 5, 7, 4, 7, 1], "Medium Armour": [20, 2, "Threatening", 3, 9, 8, 8, 2]
,"Special Forces": [10, 10, "Anti-tank", 4, 5, 0, 9, 3]}
# key: Unit Type: Attack, Defence, Ability, Mobility, Health, Armour, Penetration, Range
units = {"1st (African) Division": ["Infantry", 4, "A"], "1st Field Regiment, Royal Artillery": ["Artillery", 2, "B"]
, "2nd Armour Division(Light detachment)": ["Light Armour", 10, "C"]}
units_e = {"test 1_e": ["Infantry", 3, "1"], "test 2_e": ["Artillery", 1, "2"]
, "test 3_e": ["Light Armour", 10, "3"], "test 4_e": ["Medium Armour", 5, "4"], "test 5_e": ["Special Forces", 7, "5"]}
alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
call_t = 3
# key: Unit name: Unit type, Inititive, Callsign
map = [[" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
["a", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["b", ".", ".", ".", ".", "B", "L", "I", "C", "K", "Y", ".", ".", ".", ".", "."],
["c", ".", ".", ".", ".", ".", ".", ".", "Ð", ".", ".", ".", ".", ".", ".", "."],
["d", ".", ".", ".", ".", ".", ".", ".", ".", "Ð", ".", ".", ".", ".", ".", "."],
["e", ".", ".", "Ð", "Ð", "Ð", ".", ".", ".", ".", "Ð", "Ð", ".", ".", ".", "."],
["f", ".", "Ð", ".", ".", ".", "Ð", ".", ".", ".", ".", ".", ".", ".", ".", "."],
["g", ".", ".", ".", ".", ".", ".", "Ð", ".", ".", ".", ".", ".", "Ð", "Ð", "."],
["h", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "Ð", "Ð", ".", ".", "."],
["i", ".", ".", ".", ".", ".", ".", ".", ".", ".", "Ð", ".", ".", ".", ".", "."],
["j", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
# Text blocks: Move to a json or something at some point
instructions = {"Placement": ["After going through the initial menus, you will come to a screen that looks like this:" 
,"print map_f()"
, "This screen will prompt you to place your units. To place a unit, you will need to enter in a number. Each letter",
"corresponds to a number. e.g a = 1, b = 2, c = 3 and so on. Once you enter this, your unit will place, showing up as",
"a capital letter, such as 'A'. You will then be prompted to palce your next following the same process until all of",
"your units have been placed."], 
"Movement": ["After your units have been placed, you will come to another screen like this:"
,"print map_f()"
, "This screen will prompt you to enter in a direction. This direction could be up, right, left or down."
, "Right now, your movement keys are {0} for up, {1} for left, {2} for down, {3} for right and {4} to stop"
.format(direction["Forward"], direction["Left"], direction["Back"], direction["Right"], direction["Stop"]),
"Each unit can move a certain amount of times. Once the unit has moved its max amount of squares, or the"
, "player stops it moveing, the unit can attack if there is something to shoot."], 
"Attacking": ["After moveing a unit, if an enemy unit is in range of your unit, you may shoot it.",
"Each unit has set amount of range, damage and health. A units range dictates if it can shoot something.",
"A units attack determines how much damge it will do and its health how damage much it can take.",
"When attacking, a menu will appear with all the units you could shoot. Each will have a number next",
"to it. To select that option, enter in the number next to it. The game will then procced."]}
MINI = 0
MENU_MIN = 1 
go = False
# Functions
def menu():
    print("""=========================================
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

def select_yn():
    choice = "b"
    while True:
        try:
            while choice != "Y" and choice != "N":
                choice = input("Yes(Y) or No(N): ").upper()
            break
        except:
            print("Enter yes or no")
    return choice

def start():
    print("Welcome to the game")
    print("You have {0} units".format(len(units)))
    print("Please select an option:")
    y = 0
    for x in options_2:
        y += 1
        print("{0}. {1}".format(y, x))
    choice = select_int(MENU_MIN, len(options_2))
    os.system("cls")
    return choice

def view():
    print("Here is a list of your units")
    for x in units:
        print("Unit {0}".format(x))
        print("Unit Type: {0}".format(units[x][0]))
        print("Unit Movement: {0}".format(units[x][2]))

def map_f():
    for x in map:
        print(" ".join(x))

def place_unit_p():
    place = 0
    print("""enter the number corresponding to the the vertical number
that you want to place your unit on. i.e a -> 1, b -> 2""")
    for x in units:
        map_f()
        print("place unit {0}: ".format(x))
        while map[10][place] != ".":
            place = select_int(MENU_MIN, len(map[10])-1)
        map[10].pop(place)
        map[10].insert(place, units[x][2])
        os.system("cls")

def place_unit_e():
    place = 0
    for x in units_e:
        while map[1][place] != ".":
            place = random.randint(MENU_MIN, len(map[1])-1)
        map[1].pop(place)
        map[1].insert(place, units_e[x][2])

def orderer():
    turn_order = {}
    turns = []
    for x in units:
        if units[x][1] not in turn_order:
            turn_order[units[x][1]] = []
        turn_order[units[x][1]].append(x)
    for x in units_e:
        if units_e[x][1] not in turn_order:
            turn_order[units_e[x][1]] = []
        turn_order[units_e[x][1]].append(x)
    keys_1 = list(turn_order.keys())
    keys_1.sort(reverse = True)
    for x in keys_1:
        for y in turn_order[x]:
            turns.append(y)
    return turns

def find_mob(tar:str):
    vals = list(order.values())
    keys = list(order.keys())
    location = list(index_2d(vals, tar))
    mob = keys[location[0]]
    return mob

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))
# From Mark Byers on Stack overflow, not actually used in code

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

def range_f(unit:str):
    range_v = stats[unit][7]
    enemys = []
    in_range = []
    call_range = []
    pos = find_p()
    val = list(pos.values())
    key = list(pos.keys())
    if unit in units:
        call = units[unit][2]
        posi = pos[call]
        e_c = enemy_calls()
    elif unit in units_e:
        call = units_e[unit][2]
        posi = pos[call]
        e_c = freind_calls()
    posi = list(posi)
    calls = list(e_c.keys())
    for x in calls:
        x = str(x)
        e_p = pos[x]
        enemys.append(e_p)
    p_0 = posi[0]
    p_1 = posi[1]
    pos = find_p()
    for x in enemys:
        ep_0 = x[0]
        ep_1 = x[1]
        num_1 = abs(p_0 - ep_0)
        num_2 = abs(p_1 - ep_1)
        num = num_1 + num_2
        if num <= range_v:
            in_range.append(x)
    for x in in_range:
        ind = val.index(x)
        call = key[ind]
        call_range.append(call)
    return call_range


def find_p():
    pos = {}
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
            if y != "." and y not in alphabet and y not in features:
                a = x.index(y)
                pos[y] = map.index(x), a
    return pos

def move(unit:str, name:str):
    pos = find_p()
    position = list(pos[unit])
    mob = stats[name][3]
    call = units[name][2]
    print("""Unit {0}({8}) is at {1}. They can move {2} sqaures.
You will be asked to input a direction 
{3} for up, {4} for left {5} for down and {6} for right
The unit will move this direction and ask again until you stop it
moveing or run out of movement. Enter {7} to halt unit."""
          .format(name, pos[unit], mob, direction["Forward"], direction["Left"], direction["Back"], direction["Right"], direction["Stop"], call))
    while mob != 0:
        pos = find_p()
        move = "kilomenjaro"
        position = list(pos[unit])
        try:
            while True:
                move = ask_for_move()
                cords = move_how(move, unit)
                if cords == "stop":
                    mob = 0
                    break
                pos = find_p()
                position = list(pos[unit])
                if map[cords[0]][cords[1]] == ".":
                    map[cords[0]][cords[1]] = unit
                    map[position[0]][position[1]] = "."
                    mob -= 1
                    break
                else:
                    print("Space occupied")
            os.system("cls")
            map_f()
            print("Unit {0} is at {1}. They can move {2} sqaures.".format(name, pos[unit], mob))
        except:
            print("That would be deserting")

def ask_for_move():
    choice = "Bobux?"
    dir_val = list(direction.values())
    while choice not in dir_val:
        try:
            choice = input("Please input a direction: ").upper()
        except:
            print("Brokie")
    return choice

def move_how(direct:str, unit:str):
    cords = []
    pos = find_p()
    position = list(pos[unit])
    ud = position[0]
    lr = position[1]
    if direct == direction["Forward"] or direct == direction["Left"]:
        move_2 = -1
    elif direct == direction["Back"] or direct == direction["Right"]:
        move_2 = 1
    if direct == direction["Forward"] or direct == direction["Back"]:
        ud += move_2
    elif direct == direction["Right"] or direct == direction["Left"]:
        lr += move_2
    elif direct == direction["Stop"]:
        return "stop"
    cords.append(ud)
    cords.append(lr)
    return cords

def move_e(unit:str, name:str):
    position = list(pos[unit])
    mob = stats[name][3]
    moves = ask_move_e(unit, mob)
    moves = list(moves)
    e_c = enemy_calls()
    e_k = list(e_c.keys())
    ud = position[0] - moves[0]
    lr = position[1] - moves[1]
    while map[ud][lr] != "." and\
        map[ud][lr] not in alphabet and\
            map[ud][lr] not in e_k:
        moves = ask_move_e(unit, mob)
        ud = position[0] - moves[0]
        lr = position[1] - moves[1]
    map[ud][lr] = unit
    map[position[0]][position[1]] = "."

def ask_move_e(unit:str, movement:int):
    ver = 100000000000000
    hor = 100000000000000
    while pos[unit][0] - ver < 1 or pos[unit][0] - ver > 10:
        ver = random.randint(-movement, movement)
        movement -= ver
    while pos[unit][1] - hor < 1 or pos[unit][1] - hor > 15:
        hor = random.randint(-movement, movement)
    return ver, hor

def attack(unit:str):
    p_targets = []
    pos_v = list(pos.values())
    f_calls = freind_calls()
    f_calls = list(f_calls.keys())
    in_ran = range_f(unit)
    stats = stat_assi()
    if bool(in_ran) == True:
        for x in in_ran:
            p_targets.append(x)
        p_targets.append("Hold Fire")
        print("potential targets:")
        y = 0
        for x in p_targets:
            y += 1
            print("{0}. {1}".format(y, x))
        print("enter the number of your choice")
        target = select_int(MENU_MIN, len(p_targets))
        target -= 1
        tar = p_targets[target]
        callsigns = enemy_calls()
        if tar != "Hold Fire":
            stats[callsigns[int(tar)]][4] -= stats[unit][0]
            return callsigns[int(tar)]
        else:
            print("Fire held")
            return None

def attack_e(unit:str):
    p_targets = []
    stats = stat_assi()
    in_ran = range_f(unit)
    if bool(in_ran) == True:
        for x in in_ran:
            p_targets.append(x)
        target = random.randint(MENU_MIN, len(p_targets))
        target -= 1
        tar = p_targets[target]
        callsigns = freind_calls()
        stats[callsigns[tar]][4] -= stats[unit][0]
        return callsigns[tar]

def enemy_calls():
    list3 = list(units_e.values())
    list4 = list(units_e.keys())
    list5 = []
    callsigns = {}
    for x in list3:
        list5.append(int(x[2]))
    for x in list5:
        y = list4[list5.index(x)]
        if y in order:
            callsigns[x] = list4[list5.index(x)]
    return callsigns

def freind_calls():
    list3 = list(units.values())
    list4 = list(units.keys())
    list5 = []
    callsigns = {}
    for x in list3:
        list5.append(x[2])
    for x in list5:
        y = list4[list5.index(x)]
        if y in order:
            callsigns[x] = list4[list5.index(x)]
    return callsigns

def summary():
    print("summary")

def instructions_f():
    print("Welcome to the instructions place!") # Needs new name
    while True:
        y = 0
        ins = list(instructions.keys())
        for x in instructions:
            y += 1
            print("{0}. {1}".format(y, x))
        choice = select_int(MENU_MIN, len(instructions))
        choice -= 1
        pick = ins[choice]
        for x in instructions[pick]:
            if x != "print map_f()":
                print("• {0}".format(x))
            else:
                map_f()
        print("Do you want more instructions?")
        cont = select_yn()
        if cont == "N":
            break
    os.system("cls")

def settings():
    print("Welcome to the settings place!") # Needs new name
    while True:
        y = 0
        for x in settings_o:
            y += 1
            print("{0}. {1}".format(y, x))
        choice = select_int(MENU_MIN, len(settings_o))
        if choice == 1:
            c_binds()
        else:
            break
    os.system("cls")

def c_binds():
    print("Change Key Bindings here!")
    keys = list(direction.keys())
    values = list(direction.values())
    y = 0
    for x in keys:
        y += 1
        print("{0}. {1}".format(y, x))
    print("Select the number of the key you want to change")
    change = select_int(MENU_MIN, len(keys))
    change -= 1
    new_bind = "gg"
    while True:
        new_bind = input("Please enter in the new key to move {0}: ".format(keys[change]))
        try:
            new_bind.upper()
        except:
            useless = "Bornana"
        if len(new_bind) == 1:
            break
        else:
            print("Enter only one letter")
    changed = keys[change]
    print("The key for {0} was changed to {1}".format(changed, new_bind))
    direction[changed] = new_bind

def level():
    print("pick what level to play(1-5)")
    level = select_int(MENU_MIN, len(maps_dict))
    level -= 1
    return level

def shop(money:int, call_t:int):
    while True:
        print("You have {0} deployment points".format(money))
        print("Here are the units ready for deployment:")
        y = 1
        for x in for_sale:
            z = prices[y - 1]
            print("   {1}. {0} for ${2}".format(x, y, z))
            y += 1
        print("Enter 0 to cancel")
        pick = select_int(MENU_MIN, len(for_sale))
        pick -= 1
        if pick == -1:
            break
        while prices[pick] > money:
            print("You can't afford that unit, choose something else")
            pick = select_int(MENU_MIN, len(for_sale))
            pick -= 1
            if pick == -1:
                break
        if pick == -1:
            break
        money -= prices[pick]
        fs_k = list(for_sale.keys())
        fs_v = list(for_sale.values())
        call_t += 1
        fs_v[pick][3] = alphabet[call_t]
        sold.append(fs_k[pick])
        units[fs_k[pick]] = for_sale[fs_k[pick]]
    return money


#Functions /\

# code
while go is not True:
    choice = menu()
    if choice == 1:
        go = True
    elif choice == 2:
        instructions_f()
    elif choice == 3:
        settings()
    elif choice == 4:
        print("goodbye")
        break
    else:
        print("something is brokie")

while True:
    for_sale = {}
    prices = []
    for x in range(3):
        while True:
            g = random.randint(0, len(div_types) - 1)
            f = random.randint(0, len(div_types[g]) - 1)
            divs = list(div_types[g].keys())
            c = divs[f]
            if c not in for_sale and c not in sold:
                for_sale[c] = div_types[g][c]
                prices.append(costs[g])
                break
    order = orderer
    enemy_calls()
    choice = 0
    go = False
    while go is False:
        choice = start()
        if choice == 1:
            view()
        elif choice == 2:
            summary()
        elif choice == 3:
            if min(prices) <= money:
                money = shop(money)
                call_t = len(units)
            else:
                print("You can't afford anything")
        elif choice == 4:
            go = True
        else:
            print("something is brokie")

    ddd = level()
    map = maps_dict[ddd]
    desc = desc_dict[ddd]
    units_e = e_form_dict[ddd]
    winner_cash = rewards[ddd] 

    os.system("cls")
    print(desc)
    uselsssss = input("Input anything to continue: ")
    os.system("cls")

    place_unit_p()
    place_unit_e()
    order = orderer()
    stats = stat_assi()
    pos = find_p()
    f_calls = freind_calls()
    e_c = enemy_calls()
    # game starts
    turn = 1
    while True:
        print("""#######################
            Turn {0}
    #######################""".format(turn))
        for u_turn in order:
            #print(order)
            #print(u_turn)
            #print(units)
            #print(units_e)
            #print(pos)
            target = None
            if u_turn in units:
                map_f()
                target = None
                move(units[u_turn][2],u_turn)
                pos = find_p()
                pos_v = list(pos.values())
                os.system("cls")
                in_ran = range_f(u_turn)
                if bool(in_ran) == True:
                    map_f()
                    target = attack(u_turn)
                    os.system("cls")
                    stats = stat_assi()
            
            elif u_turn in units_e:
                target = None
                move_e(units_e[u_turn][2], u_turn)
                pos = find_p()
                pos_v = list(pos.values())
                os.system("cls")
                in_ran = range_f(u_turn)
                if bool(in_ran) == True:
                    map_f()
                    target = attack_e(u_turn)
                    os.system("cls")
                    stats = stat_assi()

            callsigns = enemy_calls()
            if target != None:
                if stats[target][4] <= 0:
                    if target in units:
                        dead = units[target][2]
                    elif target in units_e:
                        dead = units_e[target][2]
                    pos = find_p()
                    position = list(pos[dead])
                    del pos[dead]
                    order.remove(target)
                    e_c = enemy_calls()
                    f_c = freind_calls()
                    e_c = list(e_c.values())
                    f_c = list(f_c.values())
                    map[position[0]][position[1]] = "."
                    useless = False
                    useless_2 = False
                    for x in order:
                        if x in e_c:
                            useless = True
                        elif x in f_c:
                            useless_2 = True
                if useless == False or useless_2 == False:
                    break
        e_c = enemy_calls()
        f_c = freind_calls()
        e_c = list(e_c.values())
        f_c = list(f_c.values())
        for x in order:
            if x in e_c:
                useless = True
            elif x in f_c:
                useless_2 = True
        if target != None:
            if stats[target][4] <= 0:
                if useless == False or useless_2 == False:
                    break
        pos = find_p()
        turn += 1
    if useless == False:
        print("winner")
        money += winner_cash
    else:
        print("L")
        break
print("Game over")