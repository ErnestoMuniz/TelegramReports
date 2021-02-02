#import needed packages
import os, json, sys

#creates functions global
commands = {}

#import modules
modules = os.listdir(path='modules')
print('Importing modules')
count_mod = 0
count_ok_mod = 0
for module in modules:
    try:
        with open('modules/' + module + '/index.json') as read_modules:
            mod_data = json.load(read_modules)
            print('Importing ' + module + '... OK')
            for com in mod_data['functions']:
                commands[com] = module + '/' + mod_data['functions'][com]
            count_ok_mod += 1
    except:
        print('Importing ' + module + '... ERROR')
    count_mod += 1
print("{} of {} modules loaded".format(count_ok_mod, count_mod))