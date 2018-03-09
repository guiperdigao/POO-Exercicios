import math
import sys

def is_factor(f,n):
    if n%f==0 and (f!=1 or f!=n):
        return True
    else:
        return False
def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(is_factor(3,12))
test(not is_factor(5,12))
test(is_factor(7,14))
test(not is_factor(7,15))
test(is_factor(1,15))
test(is_factor(15,15))
test(not is_factor(25,15))
