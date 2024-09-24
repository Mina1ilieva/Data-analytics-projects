#for data wrangling - good for structured data
import pandas as pd #data merging, reshaping the data; descriptive stats;
import numpy as np #=numerical python; mathematical computations; a way to obtain mean, percentiles, stdev, mode, etc;
#multidimensional arrays + matrices; linear transformations + linear algebra;
#values drawn from different distributions;
import scipy.stats #for LINEAR REGRESSION
import math #used for mathematical computations; multiply vectors or dot product; similarity, etc;
import sklearn #a wide range of ML algorirthms;
#data preprocessing libraries 

from sklearn.preprocessing import LabelEncoder #encodes textual to categorical data
from sklearn.preprocessing import StandardScaler #scale or standardize data
from sklearn.preprocessing import LabelBinarizer 
from sklearn.preprocessing import MinMaxScaler #normalize data for working on deep-learning related projects;
from sklearn.preprocessing import scale
from sklearn.preprocessing import cosine_similarity #matrix directory from the scipy library; 

#ML model libraries 
import statsmodels.api as sm #used often when running linear regression;
#if endgoal - estimate dependent variable; if interested in causal analysis - use output table; confidence intervals, etc; 
#different regression and classification methods for models;
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import BaggingRegressor
from sklearn.ensemble import BaggingClassifier

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingClassifier

#If you are dealing with boosting models: 
from sympy import im
import xgboost as xg 
from xgboost import XGBRegressor
from xgboost import XGBClassifier

#for clustering purpouses:
from sklearn.cluster import DBSCAN
from sklearn.cluster import kmeans

#model tuning and performance libraries. For hyperparameter tuning, etc:
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

#data visualization libraries 
import seaborn as sns #heatmaps, correlation and causation, etc
import matplotlib.pyplot as plt #piecharts, etc
#import mpl_toolkits.basemap import Basemap

#NLP libraries

import re #cleaning data;
import string #cleaning and preparing the data 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import IfidVectorizer
from nltk.stem import WordNetLemmatizer 


#Deep learning libraires 
import keras #runs on top of tensorflow (environment has to be tensorflow)
#from keras.models import Sequential #add to neural nets
#from keras.layers import Dense #add to neural nets
#from keras.layers import LSTM
#from keras.layers import Dropout #only for deep learning-related models





