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
    assert lathe.csvData == [["G0", "T0101", 0, 0, 0, 0, 12500, 600, "=(G2/F2)*60", 7]]
    assert (lathe.csvData[0][6] / lathe.csvData[0][5])*60 == 2.88
    
def test_output_excel_mode_with_one_line_G01_cst_feed():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_CONSTANT_FEED.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData == [["G1", "T0101", 350, 0, 0, 0, 1000, 350, "=(G2/F2)*60", 6]]
    
def test_output_excel_mode_with_one_line_G01_cst_rot():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_CONSTANT_ROT.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData == [["G0", "T0101", 20, 0, 2000, 0.05, "=D2*E2", 40, "=(G2/F2)*60", 5]]
    
def test_output_excel_mode_with_one_line_G01_cst_Vc():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData[1] == ["G1", "T0101", 25, 200, "=1000*D2/(PI()*C2)", 0.05, "=D2*E2", 40, "=(G2/F2)*60", 7]
    
def test_output_excel_mode_with_one_line_G71_G72():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData[1] == ["G71", "T0101", 0, 0, 0, 0, 200, 0, 54, 5]
    
def test_output_excel_mode_with_one_line_G74():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData[1] == ["G74", "T0101", 0, 0, 0, 0, 600, 0, 6, 9]
    
def test_output_excel_mode_with_one_line_G76():
    lathe = FanucLathe()
    file = current_dir + test_dir + "TESTG1_VC.g"
    with open(file, "r") as file:
        for line in file:
            lathe.interpret(line, excel_mode = True)
    lathe.save_csv_data(excel_mode=True)
    
    assert lathe.csvData[1] == ["G76", "T0101", 0, 0, 0, 0, 1500, 0, 4.6, 9]
