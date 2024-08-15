import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import investors
from functions import getTotalInvestorsCosts

expected = 3
result = len(investors)
test('investors imported', expected, result)

testarg_investors_test1_2_4 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]
testarg_gearList_test1_8 = [{
    'amount' : 3,
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
}]
expected = 21.54
result = getTotalInvestorsCosts(testarg_investors_test1_2_4, testarg_gearList_test1_8)
test('getTotalInvestorsCosts - test 1',expected, result)


testarg_gearList_test2_3 = [{
    'amount' : 3,
    'price' : {
        'amount' : 3,
        'type' : 'copper'
    }
},{
    'amount' : 1,
    'price' : {
        'amount' : 10,
        'type' : 'silver'
    }
}]
expected = 20.72
result = getTotalInvestorsCosts(testarg_investors_test1_2_4, testarg_gearList_test2_3)
test('getTotalInvestorsCosts - test 2',expected, result)


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
expected = 20.72
result = getTotalInvestorsCosts(testarg_investors_test3, testarg_gearList_test2_3)
test('getTotalInvestorsCosts - test 3',expected, result)


testarg_gearList_test4_5_6 = [{
    'amount' : 1,
    'price' : {
        'amount' : 2,
        'type' : 'platinum'
    }
},{
    'amount' : 5,
    'price' : {
        'amount' : 7,
        'type' : 'silver'
    }
},{
    'amount' : 19,
    'price' : {
        'amount' : 10,
        'type' : 'copper'
    }
}]
expected = 79.34
result = getTotalInvestorsCosts(testarg_investors_test1_2_4, testarg_gearList_test4_5_6)
test('getTotalInvestorsCosts - test 4',expected, result)


testarg_investors_test5_7 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 9,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]
expected = 158.68
result = getTotalInvestorsCosts(testarg_investors_test5_7, testarg_gearList_test4_5_6)
test('getTotalInvestorsCosts - test 5',expected, result)


testarg_investors_test6 = [{
    'profitReturn' : 5,
    'adventuring' : False
},{
    'profitReturn' : 9,
    'adventuring' : False
},{
    'profitReturn' : 1,
    'adventuring' : False
}]
expected = 0.0
result = getTotalInvestorsCosts(testarg_investors_test6, testarg_gearList_test4_5_6)
test('getTotalInvestorsCosts - test 6',expected, result)

expected = 37.08
result = getTotalInvestorsCosts(testarg_investors_test5_7, [])
test('getTotalInvestorsCosts - test 7',expected, result)

expected = 0.0
result = getTotalInvestorsCosts([], testarg_gearList_test1_8)
test('getTotalInvestorsCosts - test 8',expected, result)

expected = 0.0
result = getTotalInvestorsCosts([], [])
test('getTotalInvestorsCosts - test 9',expected, result)


if __name__ == "__main__":
    report()
