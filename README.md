# npy_to_matlab
npy_to_matlab is a Python script to convert .npy files to .mat files. This script creates a MATLAB structure with the contents of the .npy's files, where the filename of the .npy file is the name of the variable.

# Usage

To use this script, place the .npy files into the 'input' folder and execute the following command (npy_to_matlab requires Python to run):

 `$ python npy_to_matlab.py filename`

where `filename` is the name of the .mat file to be created.


## Notes
MATLAB only loads variables that start with normal characters, so .npy filenames starting with `digits, dots, dashes or underscores`, will have his variable renamed. If you have different .npy files that are ONLY distinguinshed by this characters in the beginning of the filename, please rename them.