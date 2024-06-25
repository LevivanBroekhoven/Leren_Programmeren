import time
import math
from termcolor import colored
from data import *

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / COPPERTOSILVER

def silver2gold(amount:int) -> float:
    return amount / SILVERTOGOLD

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * PLATINUMTOGOLD

def getPersonCashInGold(personCash:dict) -> float:
    test = copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + platinum2gold(personCash['platinum']) + personCash['gold']
    return test

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    koste1 = people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS
    koste2 = horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    koste = koste1 + koste2
    Goudkoste = copper2gold(koste)
    totalekoste = round(Goudkoste,2)
    return totalekoste

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    resultaten = []

    for x in list:
        if key in x and x[key]== value:
            resultaten.append(x)    
    return resultaten

def getAdventuringPeople(people:list) -> list:
    result = getFromListByKeyIs(people, 'adventuring', True)
    return result

def getShareWithFriends(friends:list) -> list:
    result = getFromListByKeyIs(friends, 'shareWith', True)
    return result

def getAdventuringFriends(friends:list) -> list:  
    adventuring_friends = getFromListByKeyIs(friends, 'adventuring', True)
    result = getFromListByKeyIs(adventuring_friends, 'shareWith', True)
    
    return result

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    test = people /2 
    nummer = math.ceil(test)
    return int(nummer)

def getNumberOfTentsNeeded(people:int) -> int:
    test = people / 3
    nummer = math.ceil(test)
    return (nummer)

def getTotalRentalCost(horses:int, tents:int) -> float:
    num1 = horses * COST_HORSE_SILVER_PER_DAY
    num1 = num1 * JOURNEY_IN_DAYS
    num2 = tents * COST_TENT_GOLD_PER_WEEK
    weeks = JOURNEY_IN_DAYS / 7
    weeks = math.ceil(weeks)
    print(weeks)
    num2 = num2 * weeks
    num1 = silver2gold(num1)
    total = num1 + num2
    return total


##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()