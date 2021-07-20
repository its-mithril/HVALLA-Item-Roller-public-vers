# activity roller
# CURRENT VERSION: WARGRUN SCAVENGING
"""
to do:
    - hunting (wood/stone/ice)
    - exploring(wood/ice) (make csv)


completed:
    - scavenging
    - healing (universal)
"""
import random
import read_file


def run_activity_cmdl(warg, activity, table_path, fg=False, hunting=False):
    if activity != "healing" or activity != "scavenging" or activity != "exploring":
        print("ROLLED " + activity + " (" + table_path + ") FOR " + warg + "\n")
    else:
        print("ROLLED " + activity + " FOR " + warg + "\n")
    success = success_roll()
    print("ACTIVITY SUCCESS: ", success)
    print("FORN GEVIR: ", fg)
    if success:
        # roll items here
        _num_prizes = roll_number_prizes(fg)
        print("Number of Items Rolled: ", _num_prizes)

        _list_quality = roll_prize_rarity(_num_prizes, hunting)
        print("Quality of Items: ", _list_quality)

        _list_items = roll_item_id(_list_quality, table_path, hunting)
        print("Items Found (Copy/Paste into dA Comment): \n---")

        for n in range(len(_list_items[1])):  # items with links
            print(_list_items[1][n])

        for n in range(len(_list_items[0])):  # items without links
            print(_list_items[0][n][0], _list_items[0][n][1])

        print("---")
        print("Roll Injury/Damage: ", roll_injury())
    else:
        print("Activity: FAILED")
        # roll damage
        print("Roll Injury/Damage: ", roll_injury())


def run_activity_bot(warg, activity, table_path, fg=False, hunting=False):
    text = ""
    if activity != "healing" or activity != "scavenging" or activity != "exploring":
        text += ("ROLLED " + activity + " (" + table_path + ") FOR " + warg + "\n")
    else:
        text += ("ROLLED " + activity + " FOR " + warg + "\n")
    success = success_roll()
    text += ("ACTIVITY SUCCESS: " + str(success) + "\n")
    text += ("FORN GEVIR: " + str(fg) + "\n")
    if success:
        # roll items here
        _num_prizes = roll_number_prizes(fg)
        text += ("Number of Items Rolled: " + str(_num_prizes) + "\n")

        _list_quality = roll_prize_rarity(_num_prizes, hunting)
        text += ("Quality of Items: " + str(_list_quality) + "\n")

        _list_items = roll_item_id(_list_quality, table_path, hunting)
        text += "Items Found (Copy/Paste into dA Comment): \n---"

        for n in range(len(_list_items[1])):
            text += ("\n<" + str(_list_items[1][n]) + ">")

        for n in range(len(_list_items[0])):
            text += ("\n" + str(_list_items[0][n][0]) + ", " + str(_list_items[0][n][1]))

        text += ("\n---" + "\n")
        text += ("Roll Injury/Damage: " + str(roll_injury()) + "\n")
    else:
        text += ("Activity: FAILED" + "\n")
        # roll damage
        text += ("Roll Injury/Damage: " + str(roll_injury()) + "\n")
    return text


def success_roll():
    is_success = True
    value = random.randint(1, 100)
    if value <= 30:  # IMPORTANT: THERE ARE DIFFERENT SUCCESS ROLLS FOR EACH ACTIVITY
        # find a way to turn this into a var
        # if hunting, 20, if exploring/scavenging, 30
        is_success = False
    return is_success


def roll_number_prizes(forn_gevir):
    value = random.randint(1, 100)
    reg_dict = {"1, 13": 1, "14, 63": 2, "64, 89": 3, "90, 100": 4}
    fg_dict = {"1, 10": 1, "11, 60": 2, "61, 85": 3, "86, 100": 4}
    num_items = 0
    # in_use determined by whether or not forn_gevir bool is set true
    if forn_gevir:
        in_use = fg_dict
    else:
        in_use = reg_dict
    # check where value falls:
    key_list = list(in_use.keys())  # list of all keys
    for m in range(len(in_use)):  # iterate through list of keys
        _range = key_list[m].split(', ')  # split the key into two items
        if value in range(int(_range[0]), int(_range[1]) + 1):  # +1 because inclusive min, exclusive max
            key = key_list[m]  # if yes, the key is item m
            #  find entry that corresponds with this key
            num_items = in_use.get(key)
    return num_items


def roll_prize_rarity(num_items, _hunting=False):
    scav_exp_dict = {"1, 70": "poor/common", "71, 92": "uncommon", "93, 97": "rare", "98, 100": "epic/legendary"}
    hunting_dict = {"1, 70": "poor/common", "71, 95": "uncommon", "93, 100": "rare"}
    # same as exploring

    if _hunting:
        use = hunting_dict
    else:
        use = scav_exp_dict

    quality = []
    key_list = list(use.keys())
    for m in range(num_items):  # for every item:
        value = random.randint(1, 100)  # rng the quality of the item
        for j in range(len(use)):  # iterate through the dictionary to find the quality description
            _range = key_list[j].split(', ')  # split range
            if value in range(int(_range[0]), int(_range[1]) + 1):  # +1 because inclusive min, exclusive max
                key = key_list[j]  # get key of j
                quality.append(use.get(key))  # append to quality list
                break  # stop iterating you fool
    return quality  # at the end, return the list of quality items


def roll_item_id(quality, path, hunting=False):
    # figure out some way to read these items from a file attached to the menu module
    temp_dict = {"poor/common": 0, "uncommon": 1,
                 "rare": 2, "epic/legendary": 3}
    list_items = []
    item_links = []
    for m in quality:
        table_index = temp_dict.get(m)
        table = read_file.open_table(path, hunting)
        table_max = int(table[table_index][0][1])
        value = random.randint(1, table_max-1)  # table > quality > first line > second item

        # alright time to do the shit here:

        for j in range(1, len(table[table_index])):  # IGNORE THE FIRST ENTRY BECAUSE THAT'S DAMAGE+MAX INDICATOR
            loot_range = table[table_index][j][0].split('-')  # try to split
            if len(loot_range) == 1:  # if there is only 1 range, then:
                loot_range.append(loot_range[0])

            if value in range(int(loot_range[0]), int(loot_range[1]) + 1):
                if table[table_index][j][3] == '':  # add item name and ID to list
                    list_items.append((table[table_index][j][1], table[table_index][j][2]))
                else:  # otherwise, grab the item link and add it to the list
                    item_links.append((table[table_index][j][3]))
    return [list_items, item_links]


def roll_injury():
    # roll injury success
    saving_roll = success_roll()  # returns true on no injury
    # turn this into a read from file?
    major_injury = {"1, 20": "sprain, -5 HP, -1 AGI", "21, 30": "deafened, -5 HP, -1 AGI",
                    "31, 40": "concussion, -25 HP, -3 INT",
                    "41, 50": "fracture, -10 HP, -2 STR", "51, 60": "minor open wound, -10 HP, -2 STA",
                    "61, 68": "curse, -1 to ALL STATS", "69, 75": "poison, -30 HP, -2 STA, -2 AGI",
                    "76, 84": "internal injury, -25 HP, -3 STA", "85, 89": "broken bone, -50 HP, -4 STR",
                    "90, 94": "severe open wound, -50 HP, -4 STA",
                    "95, 100": "unstoppable bleed, -50 HP, -4 STA, -4 STR"}
    if not saving_roll:  # saving roll is between 1-30
        # roll major/minor
        is_major = random.randint(1, 100)
        if is_major > 85:
            # is major injury, roll debuff
            debuff = random.randint(1, 100)
            key_list = list(major_injury.keys())
            # check:
            for m in range(len(major_injury)):
                _range = key_list[m].split(', ')
                if debuff in range(int(_range[0]), int(_range[1]) + 1):  # +1 because inclusive min, exclusive max
                    key = key_list[m]
                    return "major injury: " + major_injury.get(key)

        else:
            # is minor injury, roll damage
            damage = random.randint(1, 20)
            return "minor injury **-" + str(damage) + "**HP"
    else:
        return "no injury"
