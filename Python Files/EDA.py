# importing all the necessary libraries
import numpy as np
import scipy as sp

# Data handling
import pandas as pd

# Date handling
import datetime as dt

# Graphics
import matplotlib.pyplot as plt

'''Visualizing results '''

''' Plotting the flow rate in log scale with respect to the day of the year'''
# Get a list of day-numbers
dayOfYear = np.linspace( 1, 365, num=365 )

# Set the size of the figure
plt.figure(figsize=(12,5))

# Plot each column of our data matrix as a separate trace, using a semi-transparent colour
plt.plot( dayOfYear, np.log10(annualFlowSeriesMat), color="steelblue", alpha=0.2 )

# Add labels and display the result
plt.xlabel('Day of Year', fontsize=14 )
plt.ylabel('log10(Flow)', fontsize=14 )
plt.title('River Medlock: London Rd. (1974-2019)', fontsize=18 )
plt.savefig( "Figures/AllAnnualFlowTraces.pdf" )
plt.show()

'''plotting how meadian and quantile range varies over the days '''
def getQuartiles( row ):
    return( np.nanquantile( row, [0.25, 0.5, 0.75] ) ) 

# Get a matrix whose columns are series of quartiles-per-day
quartileMat = np.apply_along_axis( getQuartiles, axis=1, arr=np.log10(annualFlowSeriesMat) ) # result will have quantile curves as columns
quartileMat.shape



plt.figure(figsize=(12,5))

# Plot the 1st quartile, median and 3rd quartile for each day
plt.plot( dayOfYear, quartileMat[:,2], color="steelblue", linestyle="dotted", label="3rd quartile" )
plt.plot( dayOfYear, quartileMat[:,1], color="steelblue", label="median" )
plt.plot( dayOfYear, quartileMat[:,0], color="steelblue", linestyle="dotted", label="1st quartile" )

# Add labels and display the result
plt.xlabel('Day of Year', fontsize=14 )
plt.ylabel('log10(Flow)', fontsize=14)
plt.title('River Medlock: London Rd. (1974-2019)', fontsize=18 )

plt.legend()
plt.tight_layout()
plt.savefig( "Figures/AnnualFlowWithQuartiles.pdf" )
plt.show()


'''Plotting heat map'''

# Choose bin boundaries
nBins = 20
nan_free_df = medlock_df.dropna()
nan_free_data = nan_free_df["Flow"].to_numpy()
bin_boundaries = np.histogram_bin_edges( np.log10(nan_free_data), bins=nBins )
bin_boundaries



def dayHistogram( row, bb ):
    # Get rid of NaN's
    data = row[np.logical_not(np.isnan(row))]
    if( len(data) > 0 ):
        density, bin_edges = np.histogram( row, bins=bb, density=True )
    else:
        density = np.zeros(len(bb) - 1) 
        
    return( density ) 

# Get a matrix whose columns are series of quartiles-per-day
densityMat = np.apply_along_axis( dayHistogram, axis=1, arr=np.log10(annualFlowSeriesMat), bb=bin_boundaries )
densityMat.shape


nLevels = 15
densityLevels = np.linspace( start=0, stop=np.max(densityMat), num=nLevels )
binMidPoints = 0.5 * (bin_boundaries[1:(nBins+1)] + bin_boundaries[0:nBins])
colorMap = plt.get_cmap('YlGnBu')
heatmapFig = plt.figure(figsize=[12,5])
contourMap = plt.contourf(dayOfYear, binMidPoints, densityMat.transpose(), levels=densityLevels, cmap=colorMap )
plt.xlabel('Day of year', fontsize=14)
plt.ylabel('Distrib. of log10(Flow)', fontsize=14)
plt.title('River Medlock: London Rd. (1974-2019)', fontsize=18)
cbar = plt.colorbar(contourMap)

plt.tight_layout()
plt.savefig( "Figures/AnnualFlowHeatmap.pdf" )