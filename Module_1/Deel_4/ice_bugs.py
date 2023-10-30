def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10

amount = float(input(f'Hoeveel ijsjes van {convertToEuroText(SMALL_PRICE)} wil je bestellen? '))
amount_1 = float(input(f'En hoeveel ijsjes van  {convertToEuroText(MEDIUM_PRICE)} wil je bestellen? '))
totalPrice = amount * SMALL_PRICE + amount_1 * MEDIUM_PRICE

print(f'Dat is dan {convertToEuroText(totalPrice)} totaal')