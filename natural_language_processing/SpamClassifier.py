'''
This program is going to apply SVM classification model to the SMSSpamCollection dataset 
and predict the ham/spam label based on the text of each message. It is going to use TF-IDF
where Term Frequencies divide the number of occurrences of each word in a document by the 
total number of words in the document and Inverse Document Frequency downscales weights for 
words that occur in many documents in the corpus and are therefore less informative than 
those that occur only in a smaller portion of the corpus. Note that text preprocessing, 
tokenizing and the ability to filter out stopwords (default is none) are all included in CountVectorizer.
'''

# Perform imports and load the dataset:
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn import metrics

# Load the data
df = pd.read_csv('/home/markjr/Documents/Data_science/natural_language_processing/smsspamcollection.tsv', sep='\t')
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Label
print(df['label'].value_counts())

# Features and labels
X = df['message']  # Features
y = df['label']    # Labels

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Term Frequencies and Inverse Document Frequency (we can combine the CountVectorizer and TfidTransformer steps into one using TfidVectorizer)
vectorizer = TfidfVectorizer()

# Apply TF-IDF (it fits an estimator to the data and then transforms our count-matrix to a tf-idf representation.)
X_train_tfidf = vectorizer.fit_transform(X_train) 
X_train_tfidf.shape

# Train the classifier
clf = LinearSVC()
clf.fit(X_train_tfidf,y_train)

# Build a pipeline
text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC()),
])

# Feed the training data through the pipeline
text_clf.fit(X_train, y_train)  

# Form a prediction set
predictions = text_clf.predict(X_test)

# Report the confusion matrix
print(metrics.confusion_matrix(y_test,predictions))

# You can make the confusion matrix less confusing by adding labels:
df = pd.DataFrame(metrics.confusion_matrix(y_test,predictions), index=['predicted ham','predicted spam'], columns=['actual ham','actual spam'])
print(df)

# Print a classification report
print(metrics.classification_report(y_test,predictions))

# Print the overall accuracy

print("accuracy:", metrics.accuracy_score(y_test,predictions))
