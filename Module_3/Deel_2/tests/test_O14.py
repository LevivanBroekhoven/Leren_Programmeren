import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getEarnigs

testarg_mainCharacter_test1_4_5_6 = {
    'name' : 'TestChar1',
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}
expected = [{'name': 'TestChar1', 'start': 0.0, 'end': 200.0}]
result = getEarnigs(200, testarg_mainCharacter_test1_4_5_6, [], [])
test('getEarnigs - test 1',expected, result)


testarg_mainCharacter_test2_3_7_8 = {
    'name' : 'TestChar2',
    'cash' : {
        'platinum' : 1,
        'gold' : 4,
        'silver' : 4,
        'copper' : 10
    }
}
expected = [{'name': 'TestChar2', 'start': 30.0, 'end': 200.0}]
result = getEarnigs(170, testarg_mainCharacter_test2_3_7_8, [], [])
test('getEarnigs - test 2',expected, result)


testarg_investors_test3_5_6 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 5,
    'adventuring' : True,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}]
expected = [
    {'name': 'TestChar2', 'start': 30.0, 'end': 77.5}, 
    {'name': 'TestInvestor1', 'start': 125.0, 'end': 177.5}
]
result = getEarnigs(100, testarg_mainCharacter_test2_3_7_8, [], testarg_investors_test3_5_6)
test('getEarnigs - test 3',expected, result)


testarg_friends_test4_5_8 = [{
    'name' : 'TestFriend1',
    'adventuring' : True,
    'shareWith' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 20,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestFriend2',
    'adventuring' : True,
    'shareWith' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 15,
        'silver' : 0,
        'copper' : 0
    }
}]

expected = [{'name': 'TestChar1', 'start': 0.0, 'end': 55.62},
            {'name': 'TestFriend1', 'start': 20.0, 'end': 45.62},
            {'name': 'TestFriend2', 'start': 15.0, 'end': 40.62},
            {'name': 'TestInvestor1', 'start': 125.0, 'end': 168.12}
            ]

result = getEarnigs(150, testarg_mainCharacter_test1_4_5_6, testarg_friends_test4_5_8, testarg_investors_test3_5_6)
test('getEarnigs - test 4',expected, result)


expected = [
    {'name': 'TestChar1', 'start': 0.0, 'end': 91.25}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 81.25}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 76.25}, 
    {'name': 'TestInvestor1', 'start': 125.0, 'end': 211.25}
]
result = getEarnigs(300, testarg_mainCharacter_test1_4_5_6, testarg_friends_test4_5_8, testarg_investors_test3_5_6)
test('getEarnigs - test 5',expected, result)


testarg_friends_test6_7 = [{
    'name' : 'TestFriend1',
    'adventuring' : False,
    'shareWith' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 20,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestFriend2',
    'adventuring' : True,
    'shareWith' : False,
    'cash' : {
        'platinum' : 0,
        'gold' : 15,
        'silver' : 0,
        'copper' : 0
    }
}]

expected = [
    {'name': 'TestChar1', 'start': 0.0, 'end': 237.5}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 20.0}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 15.0}, 
    {'name': 'TestInvestor1', 'start': 125.0, 'end': 387.5}
]
result = getEarnigs(500, testarg_mainCharacter_test1_4_5_6, testarg_friends_test6_7, testarg_investors_test3_5_6)
test('getEarnigs - test 6',expected, result)


testarg_investors_test7 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 10,
    'adventuring' : False,
    'cash' : {
        'platinum' : 10,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor2',
    'profitReturn' : 5,
    'adventuring' : False,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor3',
    'profitReturn' : 15,
    'adventuring' : True,
    'cash' : {
        'platinum' : 0,
        'gold' : 100,
        'silver' : 0,
        'copper' : 0
    }
}]

expected = [
    {'name': 'TestChar2', 'start': 30.0, 'end': 455.0}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 20.0}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 15.0}, 
    {'name': 'TestInvestor1', 'start': 250.0, 'end': 300.0}, 
    {'name': 'TestInvestor2', 'start': 125.0, 'end': 150.0}, 
    {'name': 'TestInvestor3', 'start': 100.0, 'end': 100.0}
]

result = getEarnigs(500, testarg_mainCharacter_test2_3_7_8, testarg_friends_test6_7, testarg_investors_test7)
test('getEarnigs - test 7',expected, result)

testarg_investors_test8 = [{
    'name' : 'TestInvestor1',
    'profitReturn' : 10,
    'adventuring' : True,
    'cash' : {
        'platinum' : 10,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor2',
    'profitReturn' : 5,
    'adventuring' : False,
    'cash' : {
        'platinum' : 5,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'name' : 'TestInvestor3',
    'profitReturn' : 15,
    'adventuring' : False,
    'cash' : {
        'platinum' : 0,
        'gold' : 100,
        'silver' : 0,
        'copper' : 0
    }
}]

expected = [
    {'name': 'TestChar2', 'start': 30.0, 'end': 75.5}, 
    {'name': 'TestFriend1', 'start': 20.0, 'end': 35.5}, 
    {'name': 'TestFriend2', 'start': 15.0, 'end': 30.5}, 
    {'name': 'TestInvestor1', 'start': 250.0, 'end': 287.5}, 
    {'name': 'TestInvestor2', 'start': 125.0, 'end': 131.0}, 
    {'name': 'TestInvestor3', 'start': 100.0, 'end': 100.0}
]
result = getEarnigs(120, testarg_mainCharacter_test2_3_7_8, testarg_friends_test4_5_8, testarg_investors_test8)
test('getEarnigs - test 8',expected, result)

if __name__ == "__main__":
    report()