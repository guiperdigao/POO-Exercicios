import math
import sys

def scalar_mult(s,v):
    last = len(v)
    mult = v
    i=0
    for i in range(last):
        mult[i] = v[i]*s
    return mult


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

test(scalar_mult(5,[1,2])==[5,10])
test(scalar_mult(3,[1,0,-1])==[3,0,-3])
test(scalar_mult(7,[3,0,5,11,2])==[21,0,35,77,14])