# importing all the necessary libraries
import numpy as np
import scipy as sp

# Data handling
import pandas as pd

# Date handling
import datetime as dt

# Graphics
import matplotlib.pyplot as plt

# Checking the flow which is in cubic meters per second, averaged over a day
medlock_df = pd.read_csv('StreamGauge_MedlockLondonRoad.csv')
medlock_df.head()

# General statistics about the data
medlock_df.info()
medlock_df.describe()
