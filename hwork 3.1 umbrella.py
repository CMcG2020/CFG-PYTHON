def is_it_raining():
    return input("Is it raining outside?")

if is_it_raining():
   print("Take an umbrella!")
else:
   print("You do not need an umbrella!")

raining = input("Is it raining today?(Y/N)").upper()

# answer from the class with an error cause incase y or n is not entered
if raining == "Y":
   print("Take an umbrella.")
elif raining == "N":
   print("You do not need an umbrella.")
else:
   print("Please try again.")