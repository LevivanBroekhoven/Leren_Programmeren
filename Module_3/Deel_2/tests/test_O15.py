import sys, os
from test_lib import test, report

basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(basepath)

for x in range(1,16):
    filepath = "tests/test_O{}.py".format(str(x).rjust(2, '0'))
    result = os.path.exists(basepath+'/'+filepath)
    test(filepath+' exsits',True, result)

if __name__ == "__main__":
    report()