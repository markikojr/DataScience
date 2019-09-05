'''
This program is going to use Latent Dirichlet Allocation (LDA) to cluster topics from articles NPR (National Public Radio),
obtained from their website www.npr.org. It posits that each document is a mixture of a small number of topics and that each 
word's presence is attributable to one of the document's topics. LDA is an example of a topic model.
Count vectorizer arguments:
max_df: ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words0).
min_df: ignore terms that have a document frequency strictly lower than the given threshold.
stop_words: Vocabulary in english.
'''

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import random

# Import the data
npr = pd.read_csv('/home/markjr/Documents/Data_science/natural_language_processing/npr.csv')
print(npr.head())
print(npr.shape)

# Vectorizer
cv = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = cv.fit_transform(npr['Article'])

# Lattent Dirichlet Allocation (this can take awhile, we're dealing with a large amount of documents!)
LDA = LatentDirichletAllocation(n_components=7,random_state=42)
LDA.fit(dtm)

# Total words
print(len(cv.get_feature_names()))

# Show 10 random words stored
for i in range(10):
    random_word_id = random.randint(0,54776)
    print(cv.get_feature_names()[random_word_id])

# Number of topics
print(len(LDA.components_))

# Total words
print(len(LDA.components_[0]))

# Single topic
single_topic = LDA.components_[0]

# Returns the indices that would sort this array.
print(single_topic.argsort())

# Word least representative of this topic
print(single_topic[18302])

# Word most representative of this topic
print(single_topic[42993])

# Top 10 words index for this topic:
print(single_topic.argsort()[-10:])

# Show top 10 words for this topic
top_word_indices = single_topic.argsort()[-10:]
for index in top_word_indices:
    print(cv.get_feature_names()[index])

# Show the top 15 words for each topic 
for index,topic in enumerate(LDA.components_):
    print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
    print([cv.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')

# Show dtm shape
print(dtm.shape)

# Show npr size
print(len(npr))

# Transform dtm
topic_results = LDA.transform(dtm)

# Show shape
print(topic_results.shape)

# Checking the first article (It shows the combinations of topics)
print(topic_results[0])

# Round
print(topic_results[0].round(2))

# Get max argument for first article (tell the predicted topic)
print(topic_results[0].argmax())

# Get max argument for all articles
topic_results.argmax(axis=1)

# Create a column with the predicted topic for all articles
npr['Topic'] = topic_results.argmax(axis=1)

# Show the new column attached
print(npr.head(10))

