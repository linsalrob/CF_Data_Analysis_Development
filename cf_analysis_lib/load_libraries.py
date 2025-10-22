"""
A library of functions for analyzing the output of the CF analysis pipeline.
"""

import re
import numpy as np
import pandas as pd
import seaborn as sns
import json
import random

from matplotlib import animation
from matplotlib.cm import ScalarMappable
from matplotlib.collections import PatchCollection
from matplotlib.colors import ListedColormap, to_hex
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from itertools import cycle
from collections import Counter, defaultdict

import networkx as nx
import community

from scipy.cluster.hierarchy import linkage, fcluster
from scipy.interpolate import griddata, Rbf, RBFInterpolator
from scipy.stats import linregress, ttest_ind, mannwhitneyu

import shap

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance
from sklearn.feature_selection import mutual_info_regression
from sklearn.manifold import TSNE
from sklearn.metrics import mean_squared_error, roc_curve, auc, pairwise_distances
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier, MultiOutputRegressor, ClassifierChain
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OrdinalEncoder, RobustScaler

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.multivariate.manova import MANOVA
from statsmodels.stats.multitest import multipletests, fdrcorrection
from statsmodels.stats.outliers_influence import variance_inflation_factor

from skbio.stats.distance import permanova, DistanceMatrix
from skbio.stats.ordination import pcoa

# there is a FutureWarning in sklearn StandardScalar which is really annoying. This ignores it.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

try:
  import google.colab
  IN_COLAB = True
  from google.colab import drive
  drive.mount('/content/drive')
  datadir = '/content/drive/MyDrive/Projects/CF/Adelaide/CF_Data_Analysis'
except ImportError:
  IN_COLAB = False
  datadir = '..'

from adjustText import adjust_text

# ignore adjustText warnings in this block
warnings.filterwarnings("ignore", category=UserWarning, module='adjustText')

replace_index = re.compile(r'^\d+\s+')
replace_nonword = re.compile(r'\W+')
