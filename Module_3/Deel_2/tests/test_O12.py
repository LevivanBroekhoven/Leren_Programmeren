import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import treasure

expected = 9
result = len(treasure)
test('treasure imported', expected, result)

if __name__ == "__main__":
    report()