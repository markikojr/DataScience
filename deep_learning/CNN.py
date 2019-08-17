'''
 This code is going to make predictions on the MNIST dataset which is a collection 
 of 70,000 handwriting samples of the numbers 0-9. Our challenge is to predict which 
 number each handwritten image represents. It talks about neural networks for image 
 recognition using KERAS Convolutional Neural Network (CNN).
'''

import tensorflow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import backend as K
import matplotlib.pyplot as plt

#LOADING THE DATA
(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()

#RESHAPPING THE DATA
#we're treating the data as 2D images of 28x28 pixels instead of a flattened stream of 784 pixels
#Depending on the data format Keras is set up for, this may be 1x28x28 or 28x28x1
if K.image_data_format() == 'channels_first':
    train_images = mnist_train_images.reshape(mnist_train_images.shape[0], 1, 28, 28)
    test_images = mnist_test_images.reshape(mnist_test_images.shape[0], 1, 28, 28)
    input_shape = (1, 28, 28)
else:
    train_images = mnist_train_images.reshape(mnist_train_images.shape[0], 28, 28, 1)
    test_images = mnist_test_images.reshape(mnist_test_images.shape[0], 28, 28, 1)
    input_shape = (28, 28, 1)
    
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')

#NORMALIZING THE DATA
train_images /= 255
test_images /= 255

#CONVERTING LABELS
train_labels = tensorflow.keras.utils.to_categorical(mnist_train_labels, 10)
test_labels = tensorflow.keras.utils.to_categorical(mnist_test_labels, 10)

#CHECKING THE DATA
def display_sample(num):
    #Print the one-hot array of this sample's label 
    print(train_labels[num])  
    #Print the label converted back to a number
    label = train_labels[num].argmax(axis=0)
    #Reshape the 768 values to a 28x28 image
    image = train_images[num].reshape([28,28])
    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()
    
display_sample(1234)

#SETTING UP A CONVOLUTIONAL NEURAL NETWORK
model = Sequential()
# 64 3x3 kernels
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
# 64 3x3 kernels
model.add(Conv2D(64, (3, 3), activation='relu'))
# Reduce by taking the max of each 2x2 block
model.add(MaxPooling2D(pool_size=(2, 2)))
# Dropout to avoid overfitting
model.add(Dropout(0.25))
# Flatten the results to one dimension for passing into our final layer
model.add(Flatten())
# A hidden layer to learn with
model.add(Dense(128, activation='relu'))
# Another dropout
model.add(Dropout(0.5))
# Final categorization from 0-9 with softmax
model.add(Dense(10, activation='softmax'))

#GETTING A DESCRIPTION OF THE RESULT
print(model.summary())

#SETTING UP THE OPTIMIZER AND THE LOSS FUNCTION
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#TRAINING THE MODEL (10 EPOCHS, BATCH OF 32)     
#This could take hours to run...        
history = model.fit(train_images, train_labels,
                    batch_size=32,
                    epochs=10,
                    verbose=2,
                    validation_data=(test_images, test_labels))        
                                        
#GETTING TEST LOSS AND ACURRACY 
print('Test loss:', score[0])
print('Test accuracy:', score[1])                              