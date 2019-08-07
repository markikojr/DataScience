#!/usr/bin/python

'''This program creates a comparison between models using DecisionTree, 
LogisticRegression, LinearDiscriminant, KNN, Naive Bayes, and SVM to get the 
accuracy of each model for the Iris Flowers dataset'''

#LOADING LIBRARIES
import matplotlib.pyplot as plt
import pandas 
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#LOADING DATA
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url, names=names)

#SHAPE
print(dataset.shape)

#HEAD
print(dataset.head(20))

#DESCRIPTIONS
print(dataset.describe())

#CLASS DISTRIBUTION
print(dataset.groupby('class').size())

#DATA VISUALIZATION
#BOX AND WHISKER PLOT
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

#HISTOGRAM
dataset.hist()
plt.show()

#SCATTER PLOT MATRIX
scatter_matrix(dataset)
plt.show()

#SPLITTING-OUT VALIDATION DATASET
array = dataset.values
X = array[:,0:4] #Values
Y = array[:,4] #class
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

#ACCURACY   
scoring = 'accuracy'

#BUILDING MODELS
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

#EVALUATING EACH MODEL IN TURNS USING KFOLD IN 10 SPLITS
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    #print(kfold)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
   
#COMPARING ALGORITHMS
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

#MAKING PREDICTIONS ON VALIDATION DATA FOR KNN MODEL
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))  
	
