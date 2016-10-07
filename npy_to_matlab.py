#!/usr/bin/env python

import sys
import scipy.io
import numpy as np
import os

FOLDER = 'input'


def npy_to_matlab(name):
    
    files = (os.listdir(FOLDER))
    path = os.path.join(os.getcwd(),FOLDER)
    npyFiles=[]
    matStructure = {}
    
  
    for f in files:
        extension = os.path.splitext(f)[1]
        if extension == '.npy':
            npyFiles.append(f)
    
    if not npyFiles:
        print "Error: There are no .npy files in %s folder"%(FOLDER)
        sys.exit(0)
    
    
    
    for f in npyFiles:
        currentFile= os.path.join(path,f)   
        variable = os.path.splitext(f)[0]
        
        #MATLAB only loads variables that start with normal characters
        variable = variable.lstrip('0123456789.-_ ')
        
        try:          
            values = np.load(currentFile)
        except IOError:
            print "Error: can\'t find file or read data"
        
        else:
            matStructure[variable] = values

    filename = name + '.mat'
    
    if matStructure:
        scipy.io.savemat(filename, matStructure)


def printUsage():
    print "Usage: python %s output_filename "%(sys.argv[0])

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        printUsage()
        sys.exit(0)
    
    if not os.path.exists(FOLDER):
     os.makedirs(FOLDER)

    filename=str(sys.argv[1])
    npy_to_matlab(filename)