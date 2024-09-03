from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input("Voor hoeveel mensen? "))

# ----- CALCULATIONS ----
# calculate factor 

nummereggs = nr_persons / 4 * AMOUNT_EGGS

nummermilk = nr_persons / 4 * AMOUNT_MILK

# calculate amount_salt

# calculate amount_pepper

# calculate amount_oil

# calculate amount_onions

# calculate amount_garlics

# calculate amount_spinach

# calculate amount_paprikas

# calculate amount_cheese

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print (f"aantal eiren is {nummereggs}")
print (f"{nummermilk} kopjes melk    ")
print('-----------------------------------------------')