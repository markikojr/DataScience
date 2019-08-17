'''
 This code is going to make predictions on the "mammographic masses" public dataset 
 from the UCI repository which has 961 instances of masses detected in mammograms,
 and contains the following attributes:
 
BI-RADS assessment: 1 to 5 (ordinal)
Age: patient's age in years (integer)
Shape: mass shape: round=1 oval=2 lobular=3 irregular=4 (nominal)
Margin: mass margin: circumscribed=1 microlobulated=2 obscured=3 ill-defined=4 spiculated=5 (nominal)
Density: mass density high=1 iso=2 low=3 fat-containing=4 (ordinal)
Severity: benign=0 or malignant=1 (binominal)

BI-RADS is an assesment of how confident the severity classification is; it is 
not a "predictive" attribute and so we will discard it.

This code is going to Build a Multi-Layer Perceptron and train it to classify masses
as benign or malignant based on its features.
'''

import pandas as pd
from sklearn import preprocessing
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import cross_val_score
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier   

#LOADING THE DATA
masses_data = pd.read_csv('/home/markjr/Documents/Data_science/deep_learning/mammographic_masses.data.txt')
print(masses_data.head())

#CORVERTTING MISSING DATA ? TO nAN AND ADDING COLUMN NAMES
masses_data = pd.read_csv('/home/markjr/Documents/Data_science/deep_learning/mammographic_masses.data.txt', na_values=['?'], names = ['BI-RADS', 'age', 'shape', 'margin', 'density', 'severity'])
print(masses_data.head())

#CHECKING WETHER THE DATA NEEDS CLEANING
print(masses_data.describe())

#CHECKING IF THERE IS CORRELATION OF WHAT SORT OF DATA HAS MISSING VALUES 
#OR IF MISSING DATA IS RANDOMLY DISTRIBUTED
print(masses_data.loc[(masses_data['age'].isnull()) |
              (masses_data['shape'].isnull()) |
              (masses_data['margin'].isnull()) |
              (masses_data['density'].isnull())])

#DROPPING ROWS WITH MISSING DATA                            
masses_data.dropna(inplace=True)
print(masses_data.describe())

#CONVERTTING DATAFRAMES INTO NUMPY ARRAYS THAT CAN BE USED BY SCIKIT_LEARN
#FEATURE DATA (AGE, SHAPE, MARGIN, DENSITY)
all_features = masses_data[['age', 'shape','margin', 'density']].values
#CLASSES DATA (SEVERITY)
all_classes = masses_data['severity'].values
#NAMES
feature_names = ['age', 'shape', 'margin', 'density']
print(all_features)

#NORMALIZING THE DATA
scaler = preprocessing.StandardScaler()
all_features_scaled = scaler.fit_transform(all_features)
print(all_features_scaled)

#SETTING UP NEURAL NETWORK
def create_model():
    model = Sequential()
    #4 feature inputs going into an 6-unit layer (more does not seem to help - in fact you can go down to 4)
    model.add(Dense(6, input_dim=4, kernel_initializer='normal', activation='relu'))
    # "Deep learning" turns out to be unnecessary - this additional hidden layer doesn't help either.
    #model.add(Dense(4, kernel_initializer='normal', activation='relu'))
    # Output layer with a binary classification (benign or malignant)
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    # Compile model; rmsprop seemed to work best
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Wrap our Keras model in an estimator compatible with scikit_learn
estimator = KerasClassifier(build_fn=create_model, epochs=100, verbose=0)
# Now we can use scikit_learn's cross_val_score to evaluate this model identically to the others
cv_scores = cross_val_score(estimator, all_features_scaled, all_classes, cv=10)
print(cv_scores.mean())