# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:17:48 2018

@author: user
"""

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
import numpy as np
import os
from PIL import Image
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
img_rows, img_cols = 200, 200

path1 = r'D:\all'    
path2 = r'D:\all_resized'  
listing = os.listdir(path1) 
num_samples=np.size(listing)
print(num_samples)

for file in listing:
    im = Image.open(path1 + '\\' + file)   
    img = im.resize((img_rows,img_cols))
    gray = img.convert('L')
    gray.save(path2 +'\\' +  file, "JPEG")

imlist = os.listdir(path2)

im1 = np.array(Image.open(r'D:\all_resized' + '\\'+ imlist[0])) # open one image to get size
m,n = im1.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = np.array([np.array(Image.open(r'D:\all_resized'+ '\\' + im2)).flatten()
              for im2 in imlist],'f')
                
label=np.ones((num_samples,),dtype = int)
label[0:403]=0
label[403:904]=1
label[904:1314]=2
label[1313:1908]=3
label[1908:]=4

data,Label = shuffle(immatrix,label, random_state=2)
train_data = [data,Label]
print (train_data[0].shape)
print (train_data[1].shape)
#batch_size to train
batch_size =32
# number of output classes
nb_classes = 5
# number of epochs to train
nb_epoch = 20
# number of convolutional filters to use
nb_filters = 3
# size of pooling area for max pooling
nb_pool = 1
# convolution kernel size
nb_conv = 1

(X, y) = (train_data[0],train_data[1])
# STEP 1: split X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
X_train = X_train.reshape(X_train.shape[0],1 , img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255
X_test /= 255
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)


###########################
model = Sequential()

model.add(Convolution2D(3,1,input_shape=(1, img_rows, img_cols)))
convout1 = Activation('relu')
model.add(convout1)
model.add(Dropout(0.5))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.5))
model.add(Convolution2D(3, nb_conv, nb_conv))
convout2 = Activation('relu')
model.add(convout2)
model.add(Dropout(0.5))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.5))
model.add(Convolution2D(32, nb_conv, nb_conv))
convout3 = Activation('relu')
model.add(convout3)
model.add(Dropout(0.5))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.5))
convout4 = Activation('relu')
model.add(convout4)
model.add(Dropout(0.5))
model.add(MaxPooling2D(pool_size=(nb_pool, nb_pool)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(19))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adadelta',metrics=['accuracy'])
print (model.summary()) 


hist = model.fit(X_train, Y_train, batch_size=batch_size, epochs=nb_epoch,
              verbose=1, validation_data=(X_test, Y_test))

#score = model.evaluate(X_test, Y_test,  verbose=0)
#print("score:",score)
#print('Test score:', score[0])
#print('Test accuracy:', score[1])
#print(model.predict_classes(X_test[1:5]))
#print(Y_test[1:5])
#from keras.preprocessing import image
#test_image = image.load_img('D:\objdet\waste.jpg')
#test_image=test_image.resize((img_rows,img_cols))
#test_image= test_image.convert('L')
#test_image.show()
#test_img =np.array(test_image).reshape(1,1,200,200)
#pred_result = model.predict(test_img)
#print(pred_result)
#final_res=any(i > 0.5 for i in pred_result[0])
#if final_res == True:
#     print("THE IMAGE CONTAINS GARBAGE")
#else:
#     print("THE IMAGE DOES NOT CONTAINS ANY GARBAGE")
####################################################################
model.save('my_model.h5')
from keras.models import load_model
model = load_model('my_model.h5')
################################################333
#from keras.models import model_from_json
#from keras.models import load_model
#model_json = model.to_json()
#
#
#with open("model_num.json", "w") as json_file:
#    json_file.write(model_json)
#
## serialize weights to HDF5
#model.save_weights("model_num.h5")
#json_file = open('model.json', 'r')
#
#loaded_model_json = json_file.read()
#json_file.close()
#loaded_model = model_from_json(loaded_model_json)
#
## load weights into new model
#loaded_model.load_weights("model_num.h5")
#print("Loaded model from disk")
#
#model.save('model_num.hdf5')
#model=load_model('model_num.hdf5')
#
## serialize model to JSON
##  the keras model which is trained is defined as 'model' in this example
#model_json = model.to_json()
#
#with open("model_num.json", "w") as json_file:
#    json_file.write(model_json)
#
## serialize weights to HDF5
#model.save_weights("model_num.h5")
from keras.preprocessing import image
test_image = image.load_img('D:\objdet\leag.jpeg')
test_image=test_image.resize((img_rows,img_cols))
test_image= test_image.convert('L')
#test_image.show()
test_img =np.array(test_image).reshape(1,1,200,200)
pred_result = model.predict(test_img)
print(pred_result)
final_res=any(i > 0.3 for i in pred_result[0])
if final_res == True:
     print("THE IMAGE CONTAINS GARBAGE")
else:
     print("THE IMAGE DOES NOT CONTAINS ANY GARBAGE")
