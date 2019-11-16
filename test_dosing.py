"""
A unit test in reference to the merge and filter logic 
for the dosing program
Created on Nov 16, 2019
@author: Edward O'Donnell eodonnell@ucsd.edu
"""
from dosing import Dosing



dosing = Dosing()
dosing.load_dfs('t2_ec_20190619.csv', 't2_registry_20190619.csv')
dosing.export_csv()