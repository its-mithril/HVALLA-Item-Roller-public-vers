import random
# healing is universal


def heal(name, has_debuff=False):
    health = random.randint(5, 20)
    text = ''
    if has_debuff:
        text += '**HEALING + ATTEMPTING TO REMOVE DEBUFF FOR {}**\n'.format(name)
    else:
        text += '**HEALING FOR {}**\n'.format(name)

    text += '**{}** has been healed for: **{} HP**\n'.format(name, health)

    if has_debuff:
        debuff_removed = random.randint(1, 100) > 50
        text += 'Debuff Removed: **{}**, deduct 5G\n'.format(debuff_removed)

    return text
