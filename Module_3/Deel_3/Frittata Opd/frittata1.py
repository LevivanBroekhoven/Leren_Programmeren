from recipe_lib import *
from frittata_ingredients import *


# -------- TITLE --------
print('=============== Frittata recept ===============')


# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons /RECIPE_PERSONS

# calculate amount_egg
aantaleggs = AMOUNT_EGGS * factor
eieren = round_piece(aantaleggs)

# calculate amount_milk
aantalmelk = AMOUNT_MILK * factor
melk = round_quarter(aantalmelk)


# calculate amount_salt
aantalzout = AMOUNT_SALT * factor
zout = round_quarter(aantalzout)


# calculate amount_pepper
aantalpeper = AMOUNT_PEPPER * factor
peper = round_quarter(aantalpeper)

# calculate amount_oil
aantaloil = AMOUNT_OIL * factor
oil = round_quarter(aantaloil)

# calculate amount_onions
aantalui = AMOUNT_ONIONS * factor
ui = round_piece(aantalui)

# calculate amount_garlics
aantalgarlic = AMOUNT_GARLICS * factor
garlic = round_piece(aantalgarlic)

# calculate amount_spinach
aantalspinazie = AMOUNT_SPINACH * factor
spinazie = round_quarter(aantalspinazie)

# calculate amount_paprikas
aantalpaprika = AMOUNT_PAPRIKAS * factor
paprika = round_piece(aantalpaprika)

# calculate amount_cheese
aantalkaas = AMOUNT_CHEESE * factor 
kaas = round_quarter(aantalkaas)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print (f"{eieren} {TXT_EGGS}")
print (f"{melk} {TXT_MILK}")
print (f"{zout} {TXT_SALT}")
print (f"{peper} {TXT_PEPPER}")
print (f"{oil} {TXT_OIL}")
print (f"{ui} {TXT_ONIONS}")
print (f"{garlic} {TXT_GARLICS}")
print (f"{paprika} {TXT_PAPRIKAS}")
print (f"{spinazie} {TXT_SPINACH}")
print (f"{kaas} {TXT_CHEESE}")
print('-----------------------------------------------')