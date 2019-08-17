'''
This code is going to make sentiment analysis on the data which consists of user-generated
movie reviews and classification of whether the user liked the movie or not based on its
associated rating. To do so, we're going to do sentiment analysis on full-text movie reviews
using a Recurring Neural Networks RNN with keras (Long Short-Term Memory - LSTM)).
'''

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding
from tensorflow.keras.layers import LSTM
from tensorflow.keras.datasets import imdb

#LOADING THE DATA
print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=20000)

#CHECKING THE DATA (they have already converted words to integer-based indices so 
#that our model can work with)
print(x_train[0])
print(y_train[0])

#keeping things managable on our PC (limit the reviews to their first 80 words)
#x_train = sequence.pad_sequences(x_train, maxlen=80)
#x_test = sequence.pad_sequences(x_test, maxlen=80)

#SETTING UP A RECURRING NEURAL NETWORK
model = Sequential()
# startting an Embedding layer - this is just a step that converts the input data
#into dense vectors of fixed size that's better suited for a neural network.
model.add(Embedding(20000, 128))
#setting up a LSTM layer for the RNN (dropout to avoid overfitting)
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
#single neuron sigmoid activation function to choose our binay sentiment classification of 0 or 1.
model.add(Dense(1, activation='sigmoid'))

#SETTING UP THE OPTIMIZER AND THE LOSS FUNCTION
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
#TRAINING THE MODEL (15 EPOCHS, BATCH OF 32)                             
model.fit(x_train, y_train,
          batch_size=32,
          epochs=15,
          verbose=2,
          validation_data=(x_test, y_test))              

#GETTING TEST LOSS AND ACURRACY           
score, acc = model.evaluate(x_test, y_test,
                            batch_size=32,
                            verbose=2)
print('Test score:', score)
print('Test accuracy:', acc)          