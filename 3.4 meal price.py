meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')

is_discount = discount_choice == 'y'
is_over_twenty = meal_price >= 20.0
discount_applicable = is_discount and is_over_twenty

if discount_applicable:
    meal_price = meal_price * 0.9
    print('Discount applied. Total cost: {}'.format(meal_price))
else:
    print('No discount')
    print('Total cost: {}'.format(meal_price))