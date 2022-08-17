##
# Andy Moran
# 6/06/2022
# portfolio.py
# gameing
# variables, imports, constants etc.
from ast import Break
from csv import unregister_dialect
import pickle
from xml.sax.handler import DTDHandler
from maps import *
from divisions import *
import random
import time
import json
import os
sold = ["1st (African) Division", "1st Field Regiment, Royal Artillery", "2nd Armoured Division(Light detachment)"]
money = 3
options = ["Start", "Instructions", "Settings", "Quit"]
options_2 = ["View units", "Shop", "Continue"]
settings_o = ["Controls", "Cancel"]
features = {"~":"Water", "/":"Cliff","Ð":"Dune", "■": "Wall"}
direction = {"Forward": "W", "Left": "A", "Back": "S", "Right": "D", "Stop": "Q"}
unit_t_s = {"Infantry": [5, 10, "Dispersed", 2, 10, 1, 4, 2], "Artillery": [10, 0, "Ranged", 1, 3, 0, 10, 5]
, "Light Armour": [8, 6, "Mobile", 5, 7, 4, 7, 1], "Medium Armour": [12, 2, "Threatening", 3, 9, 8, 8, 2]
,"Special Forces": [9, 10, "Anti-tank", 4, 5, 0, 9, 3]}
# key: Unit Type: Attack, Defence, Ability, Mobility, Health, Armour, Penetration, Range
units = {"1st (African) Division": ["Infantry", 4, "A"], "1st Field Regiment, Royal Artillery": ["Artillery", 2, "B"]
, "2nd Armoured Division(Light detachment)": ["Light Armour", 10, "C"]}
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
    """The function that prints at the start of the game"""
    print("""==========================================
                I Hate Sand
==========================================""")
    y = 0
    for x in options:
        y += 1
        print("             {0}. {1}".format(y, x))
    return select_int(MENU_MIN, len(options))

def select_int(min:int, max:int):
    """The primary input statement throughout the code when
    numbers are being input."""
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
    """The primary input statement throughout the code when
    Y or N are being input"""
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
    """The menu that pops up for the user to buy units, view their forces
    and start the game."""
    print("Welcome to the game")
    print("Please select an option:")
    y = 0
    for x in options_2:
        y += 1
        print("{0}. {1}".format(y, x))
    choice = select_int(MENU_MIN, len(options_2))
    os.system("cls")
    return choice

def view():
    """Allows user to view their units."""
    print("You have {0} units".format(len(units)))
    print("Here is a list of your units")
    for x in units:
        print("Unit {0}".format(x))
        print("Unit Type: {0}".format(units[x][0]))
        print("Unit Callsign: {0}".format(units[x][2]))

def map_f():
    """prints the map"""
    for x in map:
        print(" ".join(x))

def place_unit_p():
    """Allows user to place their units"""
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
    """Allows enemy to palce their units"""
    place = 0
    for x in units_e:
        while map[1][place] != ".":
            place = random.randint(MENU_MIN, len(map[1])-1)
        map[1].pop(place)
        map[1].insert(place, units_e[x][2])

def orderer():
    """creates the turn order"""
    turn_order = {}
    turns = []
    # puts units callsigns in a list
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
    # creates the actuale order
    for x in keys_1:
        for y in turn_order[x]:
            turns.append(y)
    return turns

def stat_assi():
    """Gets the stats of each unit"""
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
    """finds which units are in range of another unit"""
    range_v = stats[unit][7]
    enemys = []
    in_range = []
    call_range = []
    pos = find_p()
    val = list(pos.values())
    key = list(pos.keys())
    # adds units in battle to a lsit
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
    # figures out if each are in range
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
    """finds the position of each unit"""
    pos = {}
    units_o = []
    units_l = list(units.values())
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
    """The function for moveing units"""
    pos = find_p()
    position = list(pos[unit])
    mob = stats[name][3]
    call = units[name][2]
    # explains movement
    print("""Unit {0}({8}) is at {1}. They can move {2} sqaures.
You will be asked to input a direction 
{3} for up, {4} for left {5} for down and {6} for right
The unit will move this direction and ask again until you stop it
moveing or run out of movement. Enter {7} to halt unit."""
          .format(name, pos[unit], mob, direction["Forward"], direction["Left"], 
          direction["Back"], direction["Right"], direction["Stop"], call))
    # move loop, goes untill unit has no moves left
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
            print("Unit {0} is at {1}. They can move {2} sqaures."
                  .format(name, pos[unit], mob))
        except:
            print("That would be deserting")

def ask_for_move():
    """part of move function"""
    choice = "Bobux?"
    dir_val = list(direction.values())
    while choice not in dir_val:
        try:
            choice = input("Please input a direction: ").upper()
        except:
            print("Brokie")
    return choice

def move_how(direct:str, unit:str):
    """part of move function"""
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
    """Enemy move function, wqorks same as player one"""
    pos = find_p()
    position = list(pos[unit])
    mob = stats[name][3]
    while mob != 0:
        pos = find_p()
        move = "kilomenjaro"
        position = list(pos[unit])
        in_ran= range_f(name)
        if bool(in_ran) == True:
            break
        try:
            while True:
                move = ask_for_move_e()
                cords = move_how_e(move, unit)
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
        except:
            useless = 'use'

def ask_for_move_e():
    """part of enemy move function"""
    move = random.randint(1,4)
    return move

def move_how_e(direct:str, unit:str):
    """part of enemy move function"""
    cords = []
    pos = find_p()
    position = list(pos[unit])
    ud = position[0]
    lr = position[1]
    if direct == 1 or direct == 2:
        move_2 = -1
    elif direct == 3 or direct == 4:
        move_2 = 1
    if direct == 1 or direct == 3:
        ud += move_2
    elif direct == 4 or direct == 2:
        lr += move_2
    cords.append(ud)
    cords.append(lr)
    return cords

def attack(unit:str):
    """Attack function"""
    p_targets = []
    pos_v = list(pos.values())
    f_calls = freind_calls()
    f_calls = list(f_calls.keys())
    in_ran = range_f(unit)
    stats = stat_assi()
    # lets user attack
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
        # shoots at the enmy selected
        if tar != "Hold Fire":
            stats[callsigns[int(tar)]][4] -= stats[unit][0]
            return callsigns[int(tar)]
        else:
            print("Fire held")
            return None

def attack_e(unit:str):
    """Enemy Attack function"""
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
    """Finds enemy callsigns"""
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
    """Finds freindly callsigns"""
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

def instructions_f():
    """Prints the instructions"""
    print("Welcome to instructions.") # Needs new name
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
    """Settings menu"""
    print("Welcome to Settings") # Needs new name
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
    """Allows user to change which butttones they use to move"""
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
        new_bind = input("Please enter in the new key to move {0}: "
                         .format(keys[change]))
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
    """Allows user to pick what level they play"""
    print("pick what level to play(1-5)")
    level = select_int(MENU_MIN, len(maps_dict))
    level -= 1
    return level

def shop(money:int, call_t:int):
    """Allows user to but units"""
    while True:
        print("You have {0} deployment points".format(money))
        print("Here are the units ready for deployment:")
        y = 1
        for x in for_sale:
            z = prices[y - 1]
            print("   {1}. {0} for ${2}".format(x, y, z))
            y += 1
        print("Enter 0 to cancel")
        pick = select_int(MINI, len(for_sale))
        pick -= 1
        if pick == -1:
            break
        while prices[pick] > money:
            print("You can't afford that unit, choose something else")
            pick = select_int(MINI, len(for_sale))
            pick -= 1
            if pick == -1:
                break
        if pick == -1:
            break
        money -= prices[pick]
        fs_k = list(for_sale.keys())
        fs_v = list(for_sale.values())
        call_t += 1
        fs_v[pick][2] = alphabet[call_t].upper()
        sold.append(fs_k[pick])
        units[fs_k[pick]] = for_sale[fs_k[pick]]
        for_sale.pop(fs_k[pick])
    return money

#Functions /\

# initial menu
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

# randomizes what units are in the shop
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
    choice = 0
    go = False
# allows user to buy stuff
    while go is False:
        choice = start()
        if choice == 1:
            view()
        elif choice == 2:
            if min(prices) <= money:
                call_t = len(units)
                money = shop(money, call_t)
            else:
                print("You can't afford anything")
        elif choice == 3:
            go = True
        else:
            print("something is brokie")

#cahnges thins to be for the level selected
    ddd = level()
    map = maps_dict[ddd]
    desc = desc_dict[ddd]
    units_e = e_form_dict[ddd]
    winner_cash = rewards[ddd] 

    os.system("cls")
    print(desc)
    uselsssss = input("Input anything to continue: ")
    os.system("cls")

#game starts
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
# takes the turns
        for u_turn in order:
            #print(order)
            #print(u_turn)
            #print(units)
            #print(units_e)
            #print(pos)
            target = None
# freind turn code
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
# enemy turn code
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
# removes dead units from the game
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
# if all units from one side dies, the level ends
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
# decides if user won or lost
    if useless == False:
        print("winner")
        money += winner_cash
    else:
        print("L")
        break
print("Game over")