#have to make the input a float to compare the costs. Fixed line 2

my_money = float(input('How much money do you have? '))
boat_cost = (20 + 5)
if float(my_money) > boat_cost:
    print('You can afford the boat hire')
else:
    print('You cannot afford the board hire')