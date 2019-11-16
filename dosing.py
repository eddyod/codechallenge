"""
dosing.py file to generate:
    1.  csv file of filtered results
    2. pie chart that renders in a browser

Libraries used:
    1. pandas
    2. pytest
    3. plotly
Created on Nov 16, 2019
@author: Edward O'Donnell eodonnell@ucsd.edu
"""
import os
import pandas as pd
import plotly.graph_objects as go

class Dosing(object):
    """ Create a class for inputting some csv files,
    creating a pie chart on viscodes
    and exporting the results.
    Attributes:
        ecsdstxt int
        viscode str
        svdose str
        outputdir
        df_export pandas dataframe: exported csv file and dataframe
    """

    def __init__(self, ecsdstxt=280, viscode='w02', svdose='Y', outputdir='data'):
        """ setup the attributes for the dosing class
            Args:
                ecsdstxt int: default value of 280
                viscode str: default value of w02
                svdose str: default value of Y
                outputdir str: default directory to ouput results
        """
        self.ecsdstxt = ecsdstxt
        self.viscode = viscode
        self.svdose = svdose
        self.outputfile = os.path.join(outputdir, 'results.csv')
        self.df_ec = pd.DataFrame()
        self.df_registry = pd.DataFrame()
        self.df_export = pd.DataFrame()

    def load_dfs(self, file_ec, file_registry):
        """ load both of the csv files into pandas dataframes
            Args:
                file_ec csv file: location of first data file
                file_registry csv file: location of 2nd data file
        """
        try:
            self.df_ec = pd.read_csv(file_ec)
        except pd.io.common.EmptyDataError:
            print(file_ec, 'is empty')
        try:
            self.df_registry = pd.read_csv(file_registry)
        except pd.io.common.EmptyDataError:
            print(file_registry, 'is empty')


    def create_pie_chart(self):
        """Create the pie chart with plotly"""
        self.df_registry = self.df_registry[self.df_registry.VISCODE != 'bl']
        self.df_registry = self.df_registry[self.df_registry.SVPERF == 'Y']

        counts = self.df_registry['VISCODE'].value_counts()

        fig = go.Figure(data=[go.Pie(labels=counts.index,
                                     values=counts.tolist(),
                                     hovertemplate="Viscode %{label} <br>Count: %{value} (%{percent})")])
        fig.update_layout(
            title="Viscodes from Registry",
            font=dict(
                family="Times, monospace",
                size=16,
                color="#000000"
            )
        )
        fig.show()



    def merge_filter_export(self):
        """Filter the data and create the merged dataframe,
        then export it to the data dir
        """
        df_merged = pd.merge(self.df_registry, self.df_ec, how='left',
                             left_on=['RID', 'VISCODE'], right_on=['RID', 'VISCODE'])
        df_merged = df_merged[df_merged.VISCODE == self.viscode]
        df_merged = df_merged[df_merged.SVDOSE == self.svdose]
        df_merged = df_merged[df_merged.ECSDSTXT != self.ecsdstxt]
        self.df_export = df_merged[['ID_x', 'RID', 'USERID_x', 'VISCODE', 'SVDOSE', 'ECSDSTXT']]
        self.df_export.columns = ['ID', 'RID', 'USERID', 'VISCODE', 'SVDOSE', 'ECSDSTXT']
        self.df_export.to_csv(self.outputfile, index=False)


if __name__ == '__main__':
    ecsdstxt_input = input('Enter a value for ECSDSTXT: ')
    ecsdstxt_input = int(ecsdstxt_input)
    viscode_input = input('Enter a value for VISCODE: ')
    svdose_input = input('Enter a value for SVDOSE: ')
    outputdir_input = input('Enter the output dir: ')
    dosing = Dosing(ecsdstxt=ecsdstxt_input,
                    viscode=viscode_input,
                    svdose=svdose_input,
                    outputdir=outputdir_input)
    # i renamed the files to remove spaces. t2_ec_20190619.csv  t2_registry_20190619.csv
    dosing.load_dfs('t2_ec_20190619.csv', 't2_registry_20190619.csv')
    dosing.create_pie_chart()
    dosing.merge_filter_export()
    