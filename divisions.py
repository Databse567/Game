###
# divisions.py
# 9/08/2022
# Store divisions
# Infantry
infantry_div = {\
"1st (African) Division":["Infantry", 3, ""],
"1st London Division":["Infantry", 3, ""],
"4th Infantry Division":["Infantry", 3, ""],
"5th Infantry Division":["Infantry", 3, ""],
"6th Infantry Division":["Infantry", 3, ""],
"7th Infantry Division":["Infantry", 3, ""],
"8th Infantry Division":["Infantry", 3, ""],
"12th Division (SDF)":["Infantry", 3, ""],
"46th Infantry Division":["Infantry", 3, ""],
"50th (Northumbrian) Infantry Division":["Infantry", 3, ""],
"51st (Highland) Infantry Division":["Infantry", 3, ""],
"70th Infantry Division":["Infantry", 3, ""],
"78th Infantry Division":["Infantry", 3, ""],
"Y Division":["Infantry", 3, ""]}
# Artillery
artillery_div = {\
"1st Field Regiment, Royal Artillery":["Artillery", 2, ""],
"2nd Field Regiment, Royal Artillery":["Artillery", 2, ""],
"3rd Field Regiment, Royal Artillery":["Artillery", 2, ""],
"4th Field Regiment, Royal Artillery":["Artillery", 2, ""],
"5th Field Regiment, Royal Artillery":["Artillery", 2, ""],
"6th Field Regiment, Royal Artillery":["Artillery", 2, ""],
"7th Field Regiment, Royal Artillery":["Artillery", 2, ""],
"8th Field Regiment, Royal Artillery":["Artillery", 2, ""],
"9th Field Regiment, Royal Artillery":["Artillery", 2, ""],
"10th Field Regiment, Royal Artillery":["Artillery", 2, ""]}
# Light Tank
l_tank_div = {\
"1st Armoured Division (light detachment)":["Light Armour", 10, ""],
"2nd Armoured Division (light detachment)":["Light Armour", 10, ""],
"6th Armoured Division (light detachment)":["Light Armour", 10, ""],
"7th Armoured Division (light detachment)":["Light Armour", 10, ""],
"8th Armoured Division (light detachment)":["Light Armour", 10, ""],
"10th Armoured Division (light detachment)":["Light Armour", 10, ""]}
# Medium Armour
m_tank_div = {\
"1st Armoured Division":["Medium Armour", 6, ""],
"2nd Armoured Division":["Medium Armour", 6, ""],
"6th Armoured Division":["Medium Armour", 6, ""],
"7th Armoured Division":["Medium Armour", 6, ""],
"8th Armoured Division":["Medium Armour", 6, ""],
"10th Armoured Division":["Medium Armour", 6, ""]}
# Special Forces
spec_f_div = {\
"Royal Marines Division":["Special Forces", 8, ""],
"2nd Royal Marines Division":["Special Forces", 8, ""],
"1st Airborne Division":["Special Forces", 8, ""],
"4th Airborne Division":["Special Forces", 8, ""],
"Special Air Service Regiment":["Special Forces", 8, ""]}

div_types = [infantry_div, artillery_div, l_tank_div, m_tank_div, spec_f_div]
costs = [4, 7, 7, 9, 9]