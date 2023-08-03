"""I suggest you use pytest to execute this code"""

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
    file = "tests/TESTG0.g"
    normaltime = 60*600 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
            
    assert lathe.globalTime >= normaltime - 0.05 and lathe.globalTime <= normaltime + 0.05
    
def test_get_time_from_G1_with_const_rotation():
    """uses a simple G1 file to test the time returned by the lathe in a G1 operation, using a +* 0.1s tolerance"""
    lathe = Biglia()
    file = "tests/TESTG1_CONST_ROT.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    
    assert lathe.globalTime <= 24+0.1 and lathe.globalTime >= 24-0.1
    
def test_get_time_from_G1_with_cutting_speed():
    """uses a simple G1 file to test the time returned by the lathe in a G1 operation, using a +* 0.1s tolerance (real calculated time is 5.26seconds + 0.08 from G0 it 5.34 total)"""
    lathe = Biglia()
    file = "tests/TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime >= 5.3
    assert lathe.globalTime <= 5.38
    
def test_get_time_with_G94_or_G98_constantFeed():
    """Uses a simple G1 file with constant feed. F1000 disance to do : 350 mm : 21s"""
    lathe = Biglia()
    file = "tests/TESTG1_CONSTANT_FEED.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime >= 21-0.1
    assert lathe.globalTime <= 21+0.1

def test_get__time_incremental_position():
    """uses the same as tests/TESTG0.g code for a dist of 600 but using U, W, incremental values for positionning"""
    lathe = Biglia()
    file = "tests/TEST_INCREMENTAL.g"
    normaltime = 60*600 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
            
    assert lathe.globalTime >= normaltime - 0.05 and lathe.globalTime <= normaltime + 0.05

def test_program_variable():
    """uses the same as tests/TESTG0.g code for a dist of 600 but using variable"""
    lathe = Biglia()
    file = "tests/TEST_VAR.g"
    normaltime = 60*600 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    
    assert lathe.globalTime >= normaltime - 0.05 and lathe.globalTime <= normaltime + 0.05
    
def test_get_time_with_G2_const_feed_using_ij():
    lathe = Biglia()
    file = "tests/TESTG2_IJ_F_CST.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 10.53 + 0.05 and lathe.globalTime >= 10.53 -0.05

def test_get_time_with_G2_const_cuttingSpeed_using_ij():
    lathe = Biglia()
    file = "tests/TESTG2_IJ_VC_CST.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 3.309 + 0.05 and lathe.globalTime >= 3.309 -0.05
    
def test_get_time_with_G2_const_feed_using_R():
    lathe = Biglia()
    file = "tests/TESTG2_R.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 10.53 + 0.05 and lathe.globalTime >= 10.53 -0.05

def test_get_time_with_G3_const_feed_using_R():
    lathe = Biglia()
    file = "tests/TESTG3_R.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 10.53 + 0.05 and lathe.globalTime >= 10.53 -0.05