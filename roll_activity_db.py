import functions


def scavenging_exploring(warg, fg=False, activity=''):
    text = "ROLLED {} FOR {}\n".format(activity.upper(), warg)

    success = functions.success_roll()
    text += "ACTIVITY SUCCESS: {}\n".format(str(success))
    text += "FORN GEVIR APPLIED: {}\n".format(str(fg))

    if success:
        # roll num items:
        _num = functions.roll_number_prizes(fg)
        text += "Number Items Rolled: {}\n".format(str(_num))

        # roll quality:
        _quality = functions.roll_prize_rarity(_num, activity.lower())
        text += "Quality of Items: {}\n".format(_quality)

        # roll ids:
        _ids = functions.roll_item_id_se(_quality, activity.lower())

        # get links
        _items = functions.get_item_links(_ids)
        text += "Items Found (Copy/Paste into dA Comment): \n---\n"
        for x in _items:
            text += x + "\n"
        text += ("---" + "\n")

    text += "Roll Injury/Damage: {}\n".format(str(functions.roll_injury()))
    return text


def hunting(warg, prey, fg=False):
    text = "ROLLED {} ({}) FOR {}\n".format('HUNTING', prey, warg)

    success = functions.success_roll()
    text += "ACTIVITY SUCCESS: {}\n".format(str(success))
    text += "FORN GEVIR APPLIED: {}\n".format(fg)

    if success:
        # roll num items:
        _num = functions.roll_number_prizes(fg)
        text += "Number Items Rolled: {}\n".format(str(_num))

        # roll quality:
        _quality = functions.roll_prize_rarity(_num, "hunting")
        text += "Quality of Items: {}\n".format(_quality)

        # roll ids:
        _ids = functions.roll_item_id_h(_quality, prey)

        # get links
        _items = functions.get_item_links(_ids)
        text += "Items Found (Copy/Paste into dA Comment): \n---\n"
        for x in _items:
            text += x + "\n"
        text += ("---" + "\n")

    text += "Roll Injury/Damage: {}\n".format(str(functions.roll_injury()))
    return text

