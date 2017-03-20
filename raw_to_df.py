# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 10:58:04 2017

@author: GRoberta
"""
import pandas as pd

def raw_to_df(raw_file):
    '''
    Reads in a csv of pharmex data
    
    NEED TO USE \\ FORMAT FOR raw_file PATH
    
    Format is: 
        first column product names
        remaining columns months
        month format YYYYMM
    
    Returns a pandas DataFrame:
        columns = products
        hierarchical index: Year, month
        NaN values replaced with zero
    '''
    df = pd.read_csv(raw_file, index_col=0).T
                    
    df['Year'] = (df.index.astype(int)/100).astype(int)
    df['Month'] = (((df.index.astype(int)/100)%1)*100).astype(int)
    
    hier_index = pd.MultiIndex.from_tuples(list(zip(df['Year'],df['Month'])))
    df.set_index(hier_index, inplace=True)
    df.index.names = ['Year','Month']
    df.fillna(0, inplace=True)
                    
    return df


# Could auto fix path, adding double backslash if needed