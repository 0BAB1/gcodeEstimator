from ..timeEstimator.utils import *
from math import sqrt, floor

#=============================
#        UTILS TESTS
#=============================

def test_getParam_from_a_line():
    assert getParam("G56,", "G", {}) == 56
    assert getParam("G56,", "U", {}) == None
    
def test_getParam_from_a_line_as_string():
    assert getParam("G56,", "G", {}, True) == "56"
    assert getParam("G56,", "U", {}, True) == None
    
def test_magnitude():
    assert magnitude((1,1,1)) == sqrt(3)
    
def test_dot_product():
    u,v = (1,0,0), (1,0,0)
    assert dotProduct(u,v) == 1
    u,v = (1,0,0), (0,1,0)
    assert dotProduct(u,v) == 0
    u,v = (1,0,0), (0,0,1)
    assert dotProduct(u,v) == 0
    u,v = (75,20,12), (48,16,75)
    assert dotProduct(u,v) == 4820
    
def test_get_var_from_line():
    assert getVar("#100 = 20") == ("#100","20")
    assert getVar("#100=20") == ("#100","20")
    assert getVar("#0100 = 020") == ("#0100","020")