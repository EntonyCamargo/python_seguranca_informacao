import os

with open('holts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping -n 6 {}'.format(ip))