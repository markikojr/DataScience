'''This program creates a model using DecisionTree and RandomForest 
to predict employment of specific candidate profiles'''

import numpy as np
import pandas as pd
from sklearn import tree
from IPython.display import Image  
from sklearn.externals.six import StringIO  
import pydotplus
from sklearn.ensemble import RandomForestClassifier

#LOADING THE DATA
input_file = "/home/markjr/Documents/Data_science/classification/PastHires.csv"
#input_file = "PastHires.csv"
df = pd.read_csv(input_file, header = 0)

#CHECKING THE DATA
print(df.head())
print(df.shape)

#MAKING A DICTIONARY IN ORDER TO TRANSLATE THINGS TO NUMBERS
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
print(df.head())

#GETTING ALL THE VALUES AND POSSIBILITIES WITHOUT THE TARGET(HIRED)
features = list(df.columns[:6])
print(features)

#BUILDING THE DECISION TREE MODEL
y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

#Predict employment of an employed 10-year veteran
print (clf.predict([[10, 1, 4, 0, 0, 0]]))
#...and an unemployed 10-year veteran
print (clf.predict([[10, 0, 4, 0, 0, 0]]))

#GRAPH (IT IS NOT WORKING)
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=features)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  

#BUILDING THE RANDOM FOREST MODEL
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, y)

#Predict employment of an employed 10-year veteran
print (clf.predict([[10, 1, 4, 0, 0, 0]]))
#...and an unemployed 10-year veteran
print (clf.predict([[10, 0, 4, 0, 0, 0]]))