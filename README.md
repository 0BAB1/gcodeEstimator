# Gcode Time estimator V1.0 by Hugo.B

This python script takes a gcode file as an input and resturn a list containing the time data and relevant infos.

This output has been design to be converted as a CSV file (by yourself). meaning each list element is a line, containing column elements.

## Output structure 

input : the path to your gcode file

```python
from gcodeEstimator import estimation
#data output lis :
data = estimation.run(file_path) #run returns a list
# list stucture : [ [line1], [line2], [line3], ... ]
# line structure : lineX = [operation, tool, machinning time,  feedRate, line number in code]
```

!!! Adding excel mode for data output => still very buggy

## Ouput description

```python
# line structure : lineX = [operation, tool, machinning time, line number in code, feedRate]
```

- operation : The operation name as a string (example : G00, G01, G03, ...)
- tool : the tool currently in use as a string (example : T1000, T5012, ...)
- machining time : the estimated time the operation will take to execute itself in seconds as a float (example : 5, 10.12, ...)
- feed rate : the feed rate at which the opération is executed to imediatly spot the sow machining and make optimisations as a float ( example : 40, 200, 89.54, ...)
- line number in code : The line at which the opération is called in the gcode file in order to find it easily when editing huge files as an integer (exemple : 2, 75, ...)

IMPORTANT NOTE : if the time took is below 0.001 secs, it will not be in the output ! Thus making some G00 disapear.

## Supported languages and Opérations

### Warning : This script has been developped for a Biglia mLathe using Fanuc encoder.

I made this for the needs of my compagny, meaning it might not fit yours. Designed for a lathe with Y axis, but as the Y axis was added later on, the fonctionnality might not be the best.

Feel free to read the code, understand the architecture and add you own interpreter in machines.py for your own needs and push it to this repo :)

### Supported operations : 

FANUC for Lathes (Biglia constructor):

- G0, G1 (linear interpolation and positionning *note taht G0 uses tha max speed of the machine, set by default at 12500m/min in machines.py*)
- G2, G3 (circular interpolations, using I,J,K or just R)
- G71, G72 (stock removal, facing nd turning ! **this is an estimation and might be wrong with complex profiles or syntax**)
- G74 (peck drilling)
- G76 (thead cycle **this is an estimation and might be wrong with complex profiles or syntax**)
- Y axis support
- incremental support (U,V,W)
- G28 (reset tool position to 0,0,0)
- cutting parameters => G94, G94, G99, G98 (per revolution or per minute feed) G97, G96 (constant rotation or not) G92 (max spindle speed)

### Non supported and might be added :

- G33 (thead cutting)
- G53, G54, .. (set origin) (not sure to add this one)

# Testing the code

Go to ./tests folder and add your test file named like this : `test_yourFileNameHere.py`

if you need to add a gcode test file, add it in ./tests/g_test_files

to test, run : `python -m pytest`

to install pytests : `pip install pytest`