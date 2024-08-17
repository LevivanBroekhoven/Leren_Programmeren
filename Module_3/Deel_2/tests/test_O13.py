import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getInvestorsCuts, getAdventurerCut
from random import randint

testarg_investors_test1_2 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]
expected = [5.0]
result = getInvestorsCuts(100, testarg_investors_test1_2)
test('getInvestorsCuts - test 1',expected, result)

expected = [0.98]
result = getInvestorsCuts(19.7, testarg_investors_test1_2)
test('getInvestorsCuts - test 2',expected, result)


testarg_investors_test3 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 15,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]
expected = [2.5, 0.5]
result = getInvestorsCuts(50, testarg_investors_test3)
test('getInvestorsCuts - test 3',expected, result)


testarg_investors_test4 = [{
    'profitReturn' : 100,
    'adventuring' : True
},{
    'profitReturn' : 15,
    'adventuring' : True
},{
    'profitReturn' : 20,
    'adventuring' : False
}]
expected = []
result = getInvestorsCuts(randint(1,1000), testarg_investors_test4)
test('getInvestorsCuts - test 4',expected, result)

expected = []
result = getInvestorsCuts(randint(1,1000), [])
test('getInvestorsCuts - test 5',expected, result)

expected = 20.0
result = getAdventurerCut(100.0, [10.0, 10.0], 4)
test('getAdventurerCut - test 1',expected, result)

expected = 25.0
result = getAdventurerCut(100.0, [], 4)
test('getAdventurerCut - test 2',expected, result)

expected = 9.28
result = getAdventurerCut(150.0, [2.5, 1.9, 3.4, 12.3], 14)
test('getAdventurerCut - test 3',expected, result)

expected = 0.0
result = getAdventurerCut(10.0, [5, 5], randint(1,1000))
test('getAdventurerCut - test 4',expected, result)

expected = 0.0
result = getAdventurerCut(0.0, [], randint(1,1000))
test('getAdventurerCut - test 5',expected, result)

expected = 0.0
result = getAdventurerCut(0.0, [randint(1,1000),randint(1,1000)], 2)
test('getAdventurerCut - test 6',expected, result)

testarg_profitGold_test7 = float(randint(1,1000))
expected = testarg_profitGold_test7
result = getAdventurerCut(testarg_profitGold_test7, [], 1)
test('getAdventurerCut - test 7',expected, result)

testarg_profitGold_test8 = 2000.0
testarg_investorsCuts_test8 = [randint(1,999), randint(1,999)]
expected = testarg_profitGold_test8 - sum(testarg_investorsCuts_test8)
result = getAdventurerCut(testarg_profitGold_test8, testarg_investorsCuts_test8, 1)
test('getAdventurerCut - test 8',expected, result)


if __name__ == "__main__":
    report()