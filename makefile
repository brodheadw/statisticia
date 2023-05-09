# Makefile

# Variables
CPP_SRC_DIR = src/cpp
R_SRC_DIR = src/r
PYTHON_SRC_DIR = src/python
CPP_SHARED_LIB = $(CPP_SRC_DIR)/libhypothesis_testing.so

# Targets
all: compile_cpp setup_python run

compile_cpp:
	g++ -shared -o $(CPP_SHARED_LIB) -fPIC $(CPP_SRC_DIR)/hypothesis_testing.cpp

setup_python:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && R_HOME=/opt/homebrew/Cellar/r/4.3.0_1/lib/r python $(PYTHON_SRC_DIR)/main.py

clean:
	rm -rf venv
	rm -f $(CPP_SHARED_LIB)

.PHONY: all compile_cpp setup_python run clean