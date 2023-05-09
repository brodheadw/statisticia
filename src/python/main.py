# 
# src/python/main.py
# 
# Created by William Brodhead on May 9, 2023
#

import cython
import rpy2
import rcpp
from gui import create_gui

def main():
    create_gui()

if __name__ == '__main__':
    main()