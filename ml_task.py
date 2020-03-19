import numpy as np 
import tensorflow as tf

npz_file = np.load('QIS_EXAM_200Events.npz', allow_pickle =True)
print(npz_file.files)
training_ip = npz_file['training_input']
testing_ip = npz_file['test_input']
# print(testing_ip)

a = training_ip[()]
b= testing_ip[()]
x_test = np.vstack((b['0'], b['1']))
x_train = np.vstack((a['0'], a['1']))
# print(b['0'].shape)
# exit()
y_test = np.vstack((np.zeros((50,1)), np.ones((50,1))))
y_train = np.vstack((np.zeros((50,1)), np.ones((50,1))))
c=np.hstack((x_train,y_train))
np.random.shuffle(c)
x_train=c[:,:5]
x_train_n = (x_train - x_train.min(0)) / x_train.ptp(0)
x_test_n = (x_test - x_test.min(0)) / x_test.ptp(0)

x_train_n = x_train_n[:,:4]
x_test_n= x_test_n[:,:4]

print(x_train_n)
# exit()

y_train=c[:,5]
# print(y_train)
# exit()
# print(y_train.shape)
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)
print(y_train)
# exit()

model = tf.keras.Sequential([
  tf.keras.layers.Dense(500, activation=tf.nn.relu, input_shape=x_train_n[0].shape),
  # tf.keras.layers.Dense(700, activation=tf.nn.relu),
  # tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(500, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.5),
  tf.keras.layers.Dense(2, activation='softmax')
])

# adam = tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False)
sgd = tf.keras.optimizers.SGD(lr=0.059, decay=1e-6, momentum=0.75, nesterov=True)
model.compile(optimizer=sgd, 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])
model.summary()
model.fit(x_train_n, y_train, shuffle=True, validation_split=0.2,epochs=200)

pred_train= model.predict(x_train_n)
scores = model.evaluate(x_train_n, y_train, verbose=0)
print('Accuracy on training data: {} \n Error on training data: {}'.format(scores[1], 1 - scores[1]))   
 
pred_test= model.predict(x_test_n)
scores2 = model.evaluate(x_test_n, y_test, verbose=0)
print('Accuracy on test data: {} \n Error on test data: {}'.format(scores2[1], 1 - scores2[1]))
