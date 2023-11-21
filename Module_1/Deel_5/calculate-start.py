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
result2 = add(nr1, nr2)
test('add', result1,result2)

result1 = (nr1 + nr2) * nr3
result2 = multiply(add(nr1, nr2) , nr3)
test('mulitply add',result1, result2)

result1 = nr4 / (nr3 - nr2)
result2 = divide(nr4,(substract(nr3,nr2)))
test('divide substract',result1, result2)

result1 = (nr4 + nr1) / (nr3 - nr2)
result2 = divide(add(nr4,nr1), substract(nr3,nr2))
test('divide',result1, result2)

result1 = nr1 + nr2 + nr3
result2 = add (add(nr1, nr2,) ,nr3)
test('add',result1, result2)

# Bonusopdracht
result1 = (nr1 - (nr4 - nr3)) / (nr2 + nr3)
result2 = substract(divide(nr1, nr2 + nr3), divide(substract(nr4, nr3), nr2 + nr3))
test('expression-5', result1, result2)

result1 = ((nr4 + nr1) / (nr3 - nr2)) + 13
result2 =add( divide(add(nr4,nr1), substract(nr3,nr2)), 13 )
test('divide',result1, result2)

report()
