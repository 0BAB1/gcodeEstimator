from timeEstimator.machines import *
from timeEstimator.utils import *

#=============================
#        UTILS TESTS
#=============================

def test_getParam_from_a_line():
    assert getParam("G56", "G") =="G56"

#=============================
#ACTUAL TIME CALUCLATION TESTS
#=============================
    
def test_get_time_from_G0():
    """uses a simple G1 file to test the time returned by the lathe in a G0"""
    lathe = Biglia()
    file = "tests/TESTG0.txt"
    normaltime = 60*600 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
            
    assert lathe.getGlobalTime() >= normaltime - 0.05 and lathe.getGlobalTime() <= normaltime + 0.05
    
def test_get_time_from_G1_with_const_rotation():
    """uses a simple G1 file to test the time returned by the lathe in a G1 operation, using a +* 0.1s tolerance"""
    lathe = Biglia()
    file = "tests/TESTG1_CONST_ROT.txt"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    
    assert lathe.getGlobalTime() <= 24+0.1 and lathe.getGlobalTime() >= 24-0.1
    
def test_get_time_from_G1_with_cutting_speed():
    """uses a simple G1 file to test the time returned by the lathe in a G1 operation, using a +* 0.1s tolerance (real calculated time is 5.26seconds + 0.08 from G0 it 5.34 total)"""
    lathe = Biglia()
    file = "tests/TESTG1_VC.txt"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.getGlobalTime() >= 5.3
    assert lathe.getGlobalTime() <= 5.38
    
def test_get_time_with_G94_or_G98_constantFeed():
    """Uses a simple G1 file with constant feed. F1000 disance to do : 350 mm : 21s"""
    lathe = Biglia()
    file = "tests/TESTG1_CONSTANT_FEED.txt"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.getGlobalTime() >= 21-0.1
    assert lathe.getGlobalTime() <= 21+0.1
    
def test_get_time_with_G2():
    """constant constant face speed is used (ie VC is on)"""
    ...

def test_get_time_with_G3():
    """constant feed is used beacause why not after all ?"""
    ...