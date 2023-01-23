# importing all the necessary libraries
import numpy as np
import scipy as sp

# Data handling
import pandas as pd

# Date handling
import datetime as dt

# Graphics
import matplotlib.pyplot as plt



def getYearAndDoY( dateStr ):
    # Convert the date string to a Timestamp object
    ts = pd.to_datetime( dateStr, dayfirst=True )
    
    # Extract the desired data
    return( [ts.year, ts.day_of_year] )

# Test the function: result should be [1960, 31+16=47]
getYearAndDoY( "16/2/1960" ) 



list_of_pairs = medlock_df["Date"].apply(getYearAndDoY).to_list()

# Convert the list of pairs into a pair of lists.
# See: https://stackoverflow.com/questions/21444338/transpose-nested-list-in-python
pair_of_lists = np.array( list_of_pairs ).transpose().tolist()

# Add the new columns
medlock_df = medlock_df.assign( Year=pair_of_lists[0], DayOfYear=pair_of_lists[1] )

# Look at the result
medlock_df.tail() # shows bottom 5 rows


# Work out how many complete years we have
firstYear = 1974
lastYear = 2019 # data for 2020 stops at the end of September
nYears = lastYear - firstYear + 1

# Build the matrix and fill it
annualFlowSeriesMat = np.zeros( (365, nYears) )
for j in range(nYears):
    crntYear = firstYear + j 
    annualFlowSeriesMat[:,j] = medlock_df[(medlock_df["Year"] == crntYear) & (medlock_df["DayOfYear"] < 366)]["Flow"]
    
# Look at the result
annualFlowSeriesMat.shape