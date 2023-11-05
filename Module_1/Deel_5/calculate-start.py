from test_lib import test, report
from math_operations import increment, decrement, add, substract, multiply, divide

nr1 = 3
nr2 = 11
nr3 = 37
nr4 = 79

# example
result1 = nr3 * 7
result2 = multiply(nr3, 7)
test('example', result1, result2)

result1 = nr1 + nr2
result2 = add(nr2, 3)
test('add', result1,result2)

result1 = (nr1 + nr2) * nr3
result2 = multiply(nr3, 14)
test('mulitply',result1, result2)

result1 = nr4 / (nr3 - nr2)
result2 = divide(nr3, 11)
test('expression-2',result1, result2)

result1 = (nr4 + nr1) / (nr3 - nr2)
result2 = None
test('expression-3',result1, result2)

result1 = nr1 + nr2 + nr3
result2 = None
test('expression-4',result1, result2)

# Bonusopdracht
result1 = (nr1 - (nr4 - nr3)) / (nr2 + nr3)
result2 = None
test('expression-5', result1, result2)

report()
