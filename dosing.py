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

import pandas as pd
import plotly.graph_objects as go
import os

class Dosing:


    def __init__(self, ecsdstxt = 280, viscode = 'w02', svdose = 'Y', outputdir = 'data'):
        self.ecsdstxt = ecsdstxt
        self.viscode = viscode
        self.svdose = svdose
        self.outputfile = os.path.join(outputdir, 'results.csv')
        
    def load_dfs(self, file_ec, file_registry):
        try:
            self.df_ec = pd.read_csv(file_ec)
        except pd.io.common.EmptyDataError:
            print(file_ec, 'is empty')
        try:
            self.df_registry = pd.read_csv(file_registry)
        except pd.io.common.EmptyDataError:
            print(file_registry, 'is empty')
            
      
    def create_pie_chart(self):
        self.df_registry = self.df_registry[self.df_registry.VISCODE != 'bl']
        self.df_registry = self.df_registry[self.df_registry.SVPERF == 'Y']
        
        counts = self.df_registry['VISCODE'].value_counts()
        
        fig = go.Figure(data=[go.Pie(labels=counts.index, 
                                     values=counts.tolist(),
                                     hovertemplate = "Viscode %{label} <br>Count: %{value} (%{percent})")])
        fig.update_layout(
            title="Viscodes from Registry",
            xaxis_title="x Axis Title",
            yaxis_title="y Axis Title",
            font=dict(
                family="Times, monospace",
                size=16,
                color="#000000"
            )
        )
        fig.show()

    
    
    def export_csv(self):
        df_merged = pd.merge(self.df_registry, self.df_ec,  how='left', left_on=['RID','VISCODE'], right_on=['RID','VISCODE'])
        df_merged = df_merged[df_merged.VISCODE == self.viscode]
        df_merged = df_merged[df_merged.SVDOSE == self.svdose]
        df_merged = df_merged[df_merged.ECSDSTXT != self.ecsdstxt]
        df_export = df_merged[['ID_x', 'RID', 'USERID_x', 'VISCODE', 'SVDOSE','ECSDSTXT']]
        df_export.columns = ['ID','RID','USERID','VISCODE','SVDOSE', 'ECSDSTXT']
        df_export.to_csv(self.outputfile, index=False)


if __name__=="__main__":
    ecsdstxt = input('Enter a value for ECSDSTXT: ')
    ecsdstxt = int(ecsdstxt)
    viscode = input('Enter a value for VISCODE: ')
    svdose = input('Enter a value for SVDOSE: ')
    outputdir = input('Enter the output dir: ')
    dosing = Dosing(ecsdstxt = ecsdstxt, viscode = viscode, svdose = svdose, outputdir = outputdir)
    # i renamed the files to remove spaces. t2_ec_20190619.csv  t2_registry_20190619.csv
    dosing.load_dfs('t2_ec_20190619.csv', 't2_registry_20190619.csv')
    dosing.create_pie_chart()
    dosing.export_csv()