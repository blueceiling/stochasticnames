import random

with open('firstnames') as fn:
    first_names = fn.readlines()

with open('lastnames') as ln:
    last_names = ln.readlines()

full_name = "".join(random.choice(first_names).title().rstrip() + " " + random.choice(last_names).title().rstrip()) # rstrip removes trailing new line to the right
print(full_name)
