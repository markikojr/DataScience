'''
 This code is going to make predictions on the MNIST dataset which is a collection 
 of 70,000 handwriting samples of the numbers 0-9. Our challenge is to predict which 
 number each handwritten image represents. It talks about neural networks for image 
 recognition using KERAS.
'''
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt

#LOADING THE MNIST DATA(28X28 IMAGES) and labels(0-9)
#VALUES(between 0-255 where 0{BLACK} - variations_of_grey - 255{white})
#training data = 60,000 and test data = 10,000
(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()

#CONVERTING THE DATA INTO THE FORMAT KERAS EXPECTS
#Each image is 28x28 grayscale pixels, so we can treat each image as just a 1D array, 
#or tensor, of 784 numbers(28x28).
train_images = mnist_train_images.reshape(60000, 784)
test_images = mnist_test_images.reshape(10000, 784)
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')

#NORMALIZING THE DATA
train_images /= 255
test_images /= 255

#CONVERTING LABELS
train_labels = keras.utils.to_categorical(mnist_train_labels, 10)
test_labels = keras.utils.to_categorical(mnist_test_labels, 10)

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

#SETTING UP LAYERS

#TOPOLOGY 1
#model = Sequential()
#model.add(Dense(512, activation='relu', input_shape=(784,)))
#model.add(Dense(10, activation='softmax'))

#TOPOLOGY 2
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))


#GETTING A DESCRIPTION OF THE RESULT
print(model.summary())

#SETTING UP THE OPTIMIZER AND THE LOSS FUNCTION
model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

#TRAINING THE MODEL (10 EPOCHS, BATCH OF 100)                            
history = model.fit(train_images, train_labels,
                    batch_size=100,
                    epochs=10,
                    verbose=2,
                    validation_data=(test_images, test_labels))

#GETTING TEST LOSS AND ACURRACY                    
score = model.evaluate(test_images, test_labels, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

#VISUALIZING THE ONES THAT GOT WRONG
for x in range(1000):
    test_image = test_images[x,:].reshape(1,784)
    predicted_cat = model.predict(test_image).argmax()
    label = test_labels[x].argmax()
    if (predicted_cat != label):
        plt.title('Prediction: %d Label: %d' % (predicted_cat, label))
        plt.imshow(test_image.reshape([28,28]), cmap=plt.get_cmap('gray_r'))
        plt.show()