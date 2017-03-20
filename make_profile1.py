# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:33:00 2017

@author: GRoberta
"""

import pandas as pd
import numpy as np

def make_profile_mly1(df, record_delay=False):

# create an empty dataframe to build the new one on, adding a label if Delay is to be recorded   
   
    newdf = pd.DataFrame()

# enumerate through the input dataframe - the index is useful
    for i,prod in enumerate(df):

# set up an empty list to build the new series in, and a flag to raise
# after launch plus a counter for pre-launch delay
        newser, launched, delay = [], False, 0

# now iterate along the series
        for j in df.T.iloc[i]:

# pre-launch: test for launch, otherwise increment the delay
            if not launched:
                if j > 0: launched = True
                else: delay+=1

# post-launch: append to the series.  NB this will still append zeroes
            if launched: newser.append(j)

# now complete the series with NaNs (don't want zeroes)
        for k in range(delay):
            newser.append(np.nan)

# if flag set, record the delay

        if record_delay: newser.append(int(delay))
           
        newdf[prod] = pd.Series(newser)

    if record_delay:
        newdf['Period'] = list(range(len(df))) + ["Delay"]
    else:
        newdf['Period'] = list(range(len(df)))
    
    newdf.set_index('Period', inplace=True)
        
    return newdf