price = input('How much is a burger? ')
vegetarian = input('Is there a vegetarian option? (y/n) ')

within_budget = float(price) <= 10.00
has_vegetarian = vegetarian == 'y'

is_good_choice = within_budget and has_vegetarian

if is_good_choice:
    print('This restaurant is a great choice!')
if not is_good_choice:
    print('Probably not a good idea')