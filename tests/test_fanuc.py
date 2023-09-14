import pytest
import os
from ..timeEstimator.machines import *
from math import sqrt, floor

current_dir = os.path.normpath(os.path.dirname(
    os.path.abspath(__file__))).replace("\\", "/")
test_dir = "/g_test_files/"

# test that big prgramm runs without error


def test_check_for_prod_errors():
    lathe = FanucLathe()
    file = current_dir + test_dir + "full.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert True


def test_comments_non_consideration():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_COMMENTS.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert True

# =============================
# ACTUAL TIME CALUCLATION TESTS
# =============================


def test_get_time_from_G0():
    """uses a simple G1 file to test the time returned by the lathe in a G0"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG0.g"
    normaltime = 60*600 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert lathe.globalTime >= normaltime - \
        0.05 and lathe.globalTime <= normaltime + 0.05


def test_get_time_from_G1_with_const_rotation():
    """uses a simple G1 file to test the time returned by the lathe in a G1 operation, using a +* 0.1s tolerance"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_CONST_ROT.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert lathe.globalTime == 24


def test_get_time_from_G1_with_cutting_speed():
    """uses a simple G1 file to test the time returned by the lathe in a G1 operation, using a +* 0.1s tolerance (real calculated time is 5.26seconds + 0.08 from G0 it 5.34 total)"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime >= 5.3
    assert lathe.globalTime <= 5.38


def test_get_time_with_G94_or_G98_constantFeed():
    """Uses a simple G1 file with constant feed. F1000 disance to do : 350 mm : 21s"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_CONSTANT_FEED.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime >= 21-0.1
    assert lathe.globalTime <= 21+0.1


def test_get_time_incremental_position():
    """uses the same as tests/TESTG0.g code for a dist of 600 but using U, W, incremental values for positionning"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_INCREMENTAL.g"
    normaltime = 60*600 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert lathe.globalTime >= normaltime - \
        0.05 and lathe.globalTime <= normaltime + 0.05


def test_program_variable():
    """uses the same as tests/TESTG0.g code for a dist of 600 but using variable"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_VAR.g"
    # 950 being the G0 total distance in the test program
    normaltime = 60*950 / lathe.maxSpeed
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert lathe.globalTime >= normaltime - \
        0.05 and lathe.globalTime <= normaltime + 0.05


def test_get_time_with_G2_const_feed_using_ij():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG2_IJ_F_CST.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 10.53 + 0.01 and lathe.globalTime >= 10.53 - 0.01


def test_get_time_with_G2_const_cuttingSpeed_using_ij():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG2_IJ_VC_CST.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 3.309 + 0.01 and lathe.globalTime >= 3.309 - 0.01


def test_get_time_with_G2_const_feed_using_R():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG2_R.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 1332.3 + 0.2 and lathe.globalTime >= 1332.3 - 0.02


def test_get_time_with_G3_const_feed_using_R():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG3_R.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 1332.3 + 0.2 and lathe.globalTime >= 133.32 - 0.2


def test_get_time_with_G71():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG71.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 57 + 4 and lathe.globalTime >= 57 - 4


def test_get_time_with_G74():
    """peck drilling test"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG74.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    assert lathe.globalTime <= 6 + 0.1 and lathe.globalTime >= 6 - 0.1


def test_get_time_with_G4():
    """temporisation test"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG4.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    # th file has a G1 test during 24 and then G4 during 10 secs for a total of 34 secs +- tol as usual
    assert lathe.globalTime <= 34 + 0.1 and lathe.globalTime >= 34 - 0.1


def test_get_time_with_Y_axis():
    """there is a distance driven test for this but still check"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_Y_G1.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert lathe.globalTime >= 56.784 - 0.1 and lathe.globalTime <= 56.784 + 0.1


def test_get_time_G76():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_G76.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert 4.6 - 0.1 <= lathe.globalTime <= 4.6 + 0.1
# ===========================
#   DISTANCE DRIVEN TESTS
# ===========================


def test_dist():
    lathe = FanucLathe()
    assert lathe.globalDist == 0


def test_get_dist_with_Y_axis():
    """Y axis suuport test on fanuc interpreter"""
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_Y_G1.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)

    assert 94.53 < lathe.globalDist < 94.73

