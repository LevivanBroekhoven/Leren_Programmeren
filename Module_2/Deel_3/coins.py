# name of student: Levi van Broekhoven
# number of student: 99076037
# purpose of program: Je vult in hoeveel er moet worden betaalt dan vul je in hoeveel er is betaalt als er teveel is betaalt geeft het aan hoeveel je moet terug betalen
# structure of program: 

coinValues = [50,20,10,5,2,1] # Munten met de waarde van 50 cent 20 cent 10 cent 5 euro 2 euro en 1 euro

toPay = int(float(input('Amount to pay: '))* 100) # een input voor hoeveel er betaalt moet worden * 100
paid = int(float(input('Paid amount: ')) * 100) # een input voor hoeveel er is betaalt * 100
change = paid - toPay # berekent hoeveel geld je terug krijgt 

while change > 0 and len(coinValues) > 0: # zolang Change groter is dan 0 en de lengte van de lijst coinValues groter is dan 0

  coinValue = coinValues.pop(0) # haalt de eerste uit de list
  nrCoins = change // coinValue # hoeveel coins je moet terug geven 

  if nrCoins > 0: # als NrCoins groter is dan 0
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # print text met de variable nrCoins en coinValue erin
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Variable die vraagt hoeveel muntjes van ___ cent je heb terug gegeven
    change -= nrCoinsReturned * coinValue # change - ( coins die je heb terug gegeven X Coinvalue  )

if change > 0: #als change groter is dan 0
  print('Change not returned: ', str(change) + ' cents') # als change groter is dan 0 dan print dit
else:
  print('done')