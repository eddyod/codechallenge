Configuration of Project Environment
*************************************

This is a python module for the code challenge. It uses pandas, pytest, and plotly. Look at 
the requirements.txt file for all the libraries used.

Overview on how to run this module
================================
1. Install a Python virtualenv
2. Install packages required
3. Run dosing.py
4. Run test_dosing.py

Setup procedure
================

A. Configure
------------------------------------------------------------------------------------------------

1. Create a Python Virtual Environment (I'm assuming you're using a unix based OS)
    - Make the dir if it doesn't exist:

        mkdir ~/.virtualenvs
        

    - Create virtualenv (note, I use the word codechallenge below, it can be anything)

        python3 -m venv ~/.virtualenv/codechallenge
        
    - Activate virtualenv 

        source ~/.virtualenv/codechallenge/bin/activate

    - Install requirements::

        pip install -r requirements.txt


B. Run the main file 
---------------
	python dosing.py
	It will ask for several input variables:
		1. ECSDSTXT: a number
     	2. VISCODE: a string code 
     	3. SVDOSE: a string, Y or N
     	4. outputdir: a string for the data output dir. This directory must already exist and be
     		in the same dir as this directory.
		
	
