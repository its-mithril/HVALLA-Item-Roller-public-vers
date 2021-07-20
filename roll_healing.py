import random
# healing is universal


def run_healing(name, has_debuff=False):
    health = random.randint(5, 20)
    text = "**" + name + "** has been Healed for: **" + str(health) + "** HP"

    if has_debuff:
        debuff_removed = random.randint(1, 100) > 50
        return text + "\nDebuff Removed: **" + str(debuff_removed) + "**, deduct 5G"

    return text
