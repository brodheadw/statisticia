#
# src/python/utils.py
#
# Created by William Brodhead
#

import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import ctypes
import os

# Import R functions
r_source = robjects.r['source']
current_dir = os.path.dirname(os.path.abspath(__file__))
r_script_path = os.path.join(current_dir, '..', 'r', 'probability.R')
r_source(r_script_path)

calc_probability_r = robjects.globalenv['calc_probability']

def calc_probability_r(data):
    return calc_probability_r(data)

# Load C++ functions
probability_lib = ctypes.CDLL('./src/cpp/libprobability.so')

def probability_cpp(formula, probabilities):
    return probability_lib.probability(formula.encode('utf-8'), probabilities)

hypothesis_testing_lib = ctypes.CDLL('./src/cpp/libhypothesis_testing.so')

def hypothesis_testing(data):
    return hypothesis_testing_lib.hypothesis_testing(ctypes.c_double(data))