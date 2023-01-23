import numpy as np
import scipy as sp

# Data handling
import pandas as pd

# Date handling
import datetime as dt

# Graphics
import matplotlib.pyplot as plt


# Visualising distribution of flow data in both original and log scale
heightInInches = 6
widthInInches = 12
myFig, myAxes = plt.subplots(1,2, figsize=[widthInInches,heightInInches])

# Get the flow data as a numpy array
flowVals = medlock_df["Flow"].to_numpy()

# Draw the histograms
myAxes[0].hist( flowVals, bins='fd' )
myAxes[0].set_xlabel('Flow (m^3/s)', fontsize=14 )
myAxes[0].set_ylabel('Frequency', fontsize=14 )

myFig.suptitle('River Medlock: London Rd. (1974-2020)', fontsize=18)

myAxes[1].hist( np.log10(flowVals), bins='fd' )
myAxes[1].set_xlabel('Log10(Flow) (m^3/s)', fontsize=14 )
myAxes[1].set_ylabel('Frequency', fontsize=14 )

plt.savefig( "Figures/FlowDistrib.pdf" )
plt.show()


# Time Series plot on a log scale
ax = medlock_df.plot( x='Date', y='Flow',
    figsize=(12, 5), kind='line', logy=True )

ax.set_title( 'River Medlock: London Rd. (1974-2020)', fontsize=18 ) 
ax.set_ylabel( 'Flow (m^3/s)', fontsize=14 )
ax.set_xlabel( 'Date', fontsize=14 )
plt.savefig( "Figures/AllFlowData.pdf" )