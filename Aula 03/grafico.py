import numpy
import pandas
import ploty.express as px

dataframe = pandas.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
dataframe_dia = dataframe.groupby('day', sort=False).agg({'total_bill': numpy.sum}).reset_index()
