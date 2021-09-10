import random

first_name = ['Bob', 'Fred', 'John']
last_name = ['McGee', 'Mercury', 'Lennon']

chosen_fname = random.choice(first_name)
chosen_lname = random.choice(last_name)

print(chosen_fname, chosen_lname)

#print('My random name is: {} {}'.format(chosen_fname, chosen_lname)