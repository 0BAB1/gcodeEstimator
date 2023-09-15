import pytest
import os
from ..timeEstimator.machines import *
from math import sqrt, floor


current_dir = os.path.normpath(os.path.dirname(
    os.path.abspath(__file__))).replace("\\", "/")
test_dir = "/g_test_files/"

# ===========================
#      OUTPUT TESTS
# ===========================


def test_output_with_one_line():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG0.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line)
    lathe.save_csv_data()

    #                         [g,    tool,   time,  Vf, line number]   
    assert lathe.csvData == [["G0", "T0101", 2.88, 12500, 7]]
    
def test_output_excel_mode_with_one_line_G00():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG0.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    #                         [g,     tool, diam, VC, N, f,   Vf, dist,    time,   line number]
    assert lathe.csvData == [["G0", "T0101", 0, 0, 0, 0, 12500, 600.0, "=(H1/G1)*60", 7]]
    
def test_output_excel_mode_with_one_line_G01_cst_feed():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_CONSTANT_FEED.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData == [["G1", "T0101", 0, 0, 0, 0, 1000, 350, "=(H1/G1)*60", 6]]
    
def test_output_excel_mode_with_one_line_G01_cst_rot():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_CONST_ROT.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData == [["G1", "T0101", 0, 0, 2000, 0.05, "=E1*F1", 40, "=(H1/G1)*60", 5]]
    
def test_output_excel_mode_with_one_line_G01_cst_Vc():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData[1] == ["G1", "T0101", 50, 200, "=1000*D2/(PI()*C2)", 0.2, "=E2*F2", 22.36, "=(H2/G2)*60", 7]
    
def test_output_excel_mode_with_one_line_G71_G72():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG71.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    print(lathe.csvData)
    
    assert lathe.csvData[1] == ["G71", "T0101", 0, 0, 0, 0, 200, 0, 53.34, 13]
    
def test_output_excel_mode_with_one_line_G74():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG74.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData == [["G74", "T0101", 0, 0, 0, 0, 600, 0, 6, 10]]
    
def test_output_excel_mode_with_one_line_G76():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TEST_G76.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    print(lathe.csvData)
    assert lathe.csvData[1] == ["G76", "T0101", 0, 0, 0, 0, 1500, 0, 4.48, 10]


#global test

def test_run_full_on_excel_mode():
    lathe = FanucLathe()
    file = current_dir + test_dir + "full.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode=True)
    lathe.save_csv_data(excel_mode=True)

    assert True