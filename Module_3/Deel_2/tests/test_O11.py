import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getMaxAmountOfNightsInInn, getJourneyInnCostsInGold
from data import COST_INN_HUMAN_SILVER_PER_NIGHT, COST_INN_HORSE_COPPER_PER_NIGHT

expected = 3
result = COST_INN_HUMAN_SILVER_PER_NIGHT
test('COST_INN_HUMAN_SILVER_PER_NIGHT is correct', expected, result)

expected = 4
result = COST_INN_HORSE_COPPER_PER_NIGHT
test('COST_INN_HORSE_COPPER_PER_NIGHT is correct', expected, result)

expected = 0
result = getMaxAmountOfNightsInInn(0,1,1)
test('getMaxAmountOfNightsInInn - test 1',expected, result)

expected = 1
result = getMaxAmountOfNightsInInn(1,1,1)
test('getMaxAmountOfNightsInInn - test 2',expected, result)

expected = 7
result = getMaxAmountOfNightsInInn(10,2,1)
test('getMaxAmountOfNightsInInn - test 3',expected, result)

expected = 0
result = getMaxAmountOfNightsInInn(5, 100, 100)
test('getMaxAmountOfNightsInInn - test 4',expected, result)

expected = 3
result = getMaxAmountOfNightsInInn(5, 2, 2)
test('getMaxAmountOfNightsInInn - test 5',expected, result)

expected = 0.68
result = getJourneyInnCostsInGold(1,1,1)
test('getJourneyInnCostsInGold - test 1',expected, result)

expected = 0.0
result = getJourneyInnCostsInGold(0,10,10)
test('getJourneyInnCostsInGold - test 2',expected, result)

expected = 22.56
result = getJourneyInnCostsInGold(3,12,4)
test('getJourneyInnCostsInGold - test 3',expected, result)

expected = 0.0
result = getJourneyInnCostsInGold(10,0,0)
test('getJourneyInnCostsInGold - test 3',expected, result)

expected = 32289.96
result = getJourneyInnCostsInGold(123,421,124)
test('getJourneyInnCostsInGold - test 3',expected, result)

if __name__ == "__main__":
    report()
