import math
import sys

def is_factor(f,n):
    if n%f==0 and (f!=1 or f!=n):
        return True
    else:
        return False

def is_multiple(n,f):
    return is_factor(f,n)

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


test(is_multiple(12,3))
test(is_multiple(12,4))
test(not is_multiple(12,5))
test(is_multiple(12,6))
test(not is_multiple(12,7))