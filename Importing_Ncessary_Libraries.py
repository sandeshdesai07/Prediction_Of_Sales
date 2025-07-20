import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from prettytable import PrettyTable
%matplotlib inline

#data transformation
from scipy import stats #this library is used for functions like mean etc.

#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

#colors
colors = ['#F0D290','#DE834D','#A3423C','#781D42']
colors2 = ['#F0D290','#DE834D','#A3423C','#781D42','#671E31']
colors3 = ['#f0d290','#e9c083','#e2af77','#d99d6d','#d08c64', '#c67b5d', '#bc6b56','#b05a51','#a34b4d','#963b49', '#872c45','#781d42']

#xgboost
from xgboost import XGBRegressor
