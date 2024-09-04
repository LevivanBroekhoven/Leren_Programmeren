from recipe_lib import *
from frittata_ingredients import *

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
print(f"{eieren} {str_single_plural(eieren , TXT_EGGS)}")
print(f"{str_amount_fraction(melk)} {str_single_plural(melk , TXT_CUPS)} {TXT_MILK}")
print(f"{str_amount_fraction(zout)} {str_single_plural(zout , TXT_TEASPOONS)} {TXT_SALT}  ")
print(f"{str_amount_fraction(peper)} {str_single_plural(peper , TXT_TEASPOONS)} {TXT_PEPPER}")
print(f"{str_amount_fraction(oil)} {str_single_plural(oil , TXT_TEASPOONS)} {TXT_OIL}")
print(f"{ui} {str_single_plural(ui , TXT_ONIONS)}")
print(f"{garlic} {str_single_plural(garlic ,TXT_GARLICS)}")
print(f"{paprika} {str_single_plural(paprika,TXT_PAPRIKAS)}")
print(f"{str_amount_fraction(spinazie)} {str_single_plural(spinazie , TXT_CUPS)} {TXT_SPINACH}")
print(f"{str_amount_fraction(kaas)} {str_single_plural(kaas , TXT_CUPS)} {TXT_CHEESE}")
print('-----------------------------------------------')