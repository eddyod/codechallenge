"""
A unit test in reference to the merge and filter logic 
for the dosing program
Created on Nov 16, 2019
@author: Edward O'Donnell eodonnell@ucsd.edu
"""
from dosing import Dosing



dosing = Dosing()
dosing.load_dfs('t2_ec_20190619.csv', 't2_registry_20190619.csv')
dosing.merge_filter_export()

df = dosing.df_export
good_columns = ['ID','RID','USERID','VISCODE','SVDOSE', 'ECSDSTXT']


def test_merge():
    """make sure columns match"""
    for c in good_columns:
        assert c in df.columns
        
        
def test_column_len():
    """ make sure the number of columns is correct"""
    assert len(df.columns) == len(good_columns)
    
def test_filters():
    """ test filters are corrrect"""
    assert df.VISCODE.all() == dosing.viscode
    assert df.SVDOSE.all() == dosing.svdose
    assert df.ECSDSTXT.all() != dosing.ecsdstxt
