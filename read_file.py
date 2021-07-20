# this handles all the reading from file + creating dictionaries
# everything is separated by tabs
import os


def open_table(path, hunting=False):
    if hunting:
        _bullshit = "hunting/" + path
    else:
        _bullshit = path

    file_path = "loot_tables"
    num_tables = sum(len(files) for f, f, files in os.walk(file_path + "/" + _bullshit))

    table = [[] for m in range(0, num_tables)]

    for i in range(num_tables):
        file = open(file_path + "/" + _bullshit + "/" + path + str(i + 1), "r")
        test_list = file.readlines()
        for j in range(len(test_list)):
            table[i].append(test_list[j].replace(',\n', '').replace(',,', '').split(','))
        file.close()
    return table
