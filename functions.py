import random
# import db_handler


db = db_handler.db
cursor = db.cursor()


def success_roll():
    is_success = True
    value = random.randint(1, 100)
    if value <= 30:  # IMPORTANT: THERE ARE DIFFERENT SUCCESS ROLLS FOR EACH ACTIVITY
        # find a way to turn this into a var
        is_success = False
    return is_success


def roll_number_prizes(forn_gevir):
    value = random.randint(1, 100)
    data = (value,)
    if forn_gevir:
        data += ("fg",)
    else:
        data += ("reg",)

    query = "SELECT num FROM prize_quantity WHERE (%s BETWEEN min AND max) AND modifier = %s"
    cursor.execute(query, data)
    result = cursor.fetchall()
    num_items = result[0]
    return num_items[0]


def roll_prize_rarity(num_items, activity):
    result = []
    for m in range(num_items):  # for every item:
        value = random.randint(1, 100)  # rng the quality of the item
        query = "SELECT quality FROM prize_quality WHERE (%s BETWEEN min AND max) AND activity = %s"
        data = (value, activity)
        cursor.execute(query, data)
        rarity = cursor.fetchall()
        for x in rarity:
            result.append(x[0])

    return result  # at the end, return the list of quality items


def roll_injury():
    # roll injury success
    saving_roll = success_roll()  # returns true on no injury
    # turn this into a read from file?

    if not saving_roll:  # saving roll is between 1-30
        # roll major/minor
        is_major = random.randint(1, 100)
        if is_major > 85:
            query = "SELECT injury FROM major_injury WHERE min <= %s AND max >= %s"
            data = (is_major, is_major)
            cursor.execute(query, data)
            result = cursor.fetchall()
            return result[0][0]

        else:
            # is minor injury, roll damage
            damage = random.randint(1, 20)
            return "minor injury: **-" + str(damage) + "HP**"
    else:
        return "no injury"


def roll_item_id_se(quality, table):
    # figure out some way to read these items from a file attached to the menu module
    item_ids = []
    for m in quality:
        # get the upperbound value

        if m == 'poor/common':
            upperbound_query = "SELECT max FROM {} WHERE quality = %s OR quality = %s".format(table)
            data = ('poor', 'common')
        elif m == 'epic/legendary':
            upperbound_query = "SELECT max FROM {} WHERE quality = %s OR quality = %s".format(table)
            data = ('epic', 'legendary')
        else:
            upperbound_query = "SELECT max from {} WHERE quality = %s".format(table)
            data = (m,)

        cursor.execute(upperbound_query, data)
        temp = cursor.fetchall()
        temp_list = []
        for x in temp:
            temp_list.append(x[0])
        upperbound = temp_list[-1]  # items are in order

        # get the item id
        value = random.randint(1, upperbound)
        if m == 'poor/common':
            id_query = "SELECT item_id FROM {} WHERE (%s BETWEEN min AND max) AND (quality = %s OR quality = %s)".format(
                table)
            query_values = (value, 'poor', 'common')
        elif m == 'epic/legendary':
            id_query = "SELECT item_id FROM {} WHERE (%s BETWEEN min AND max) AND (quality = %s OR quality = %s)".format(
                table)
            query_values = (value, 'epic', 'legendary')
        else:
            id_query = "SELECT item_id FROM {} WHERE (%s BETWEEN min AND max) AND quality = %s".format(table)
            query_values = (value, m)

        cursor.execute(id_query, query_values)
        temp1 = cursor.fetchall()
        for x in temp1:
            item_ids.append(x[0])
    return item_ids


def roll_item_id_h(quality, prey):
    item_ids = []
    for m in quality:
        if m == 'poor/common':
            upperbound_query = "SELECT max FROM hunting WHERE (quality = %s OR quality = %s) AND prey = %s"
            data = ('poor', 'common', prey,)
        else:
            upperbound_query = "SELECT max from hunting WHERE quality = %s AND prey = %s"
            data = (m, prey,)
        cursor.execute(upperbound_query, data)
        temp = cursor.fetchall()
        temp_list = []
        for x in temp:
            temp_list.append(x[0])
        upperbound = temp_list[-1]

        value = random.randint(1, upperbound)
        if m == 'poor/common':
            id_query = "SELECT item_id FROM hunting WHERE (%s BETWEEN min AND max) AND (quality = %s OR quality = %s) " \
                       "AND prey = %s"
            id_data = (value, 'poor', 'common', prey,)
        else:
            id_query = "SELECT item_id FROM hunting WHERE (%s BETWEEN min AND max) AND quality = %s AND prey = %s"
            id_data = (value, m, prey)
        cursor.execute(id_query, id_data)
        temp1 = cursor.fetchall()
        for x in temp1:
            item_ids.append(x[0])
    return item_ids


def get_item_links(_id):
    item_links = []
    for x in _id:
        query = "SELECT item_id, item_name, item_url FROM master WHERE item_id = %s"
        cursor.execute(query, (x,))
        temp = cursor.fetchall()
        if temp[0][2] == '':
            # append id and name
            item_links.append(temp[0][0] + " " + temp[0][1])
        else:
            # append url
            item_links.append("<" + temp[0][2] + ">")

    return item_links
