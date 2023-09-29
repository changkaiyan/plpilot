import tensorflow as tf
import numpy as np

# Use Keras API in TensorFlow 2.0 
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Use input_data instead of input 
model.fit(input_data=x_train, y_train, epochs=5) 

# Use placeholder instead of Input in Keras 
x = tf.placeholder(tf.float32, shape=(None, 32))
y = tf.placeholder(tf.int32, shape=(None))
inputs = [x, y]

# Use tf.variable_scope in Keras 
with tf.variable_scope('scope1'):
  model = tf.keras.models.Sequential([tf.keras.layers.Dense(32, activation='relu')]) 
model.add(tf.keras.layers.Dense(10, activation='softmax'))

# Use activation function for entire layer
model.add(tf.keras.layers.Dense(32, tf.keras.activations.relu()))  
model.add(tf.keras.layers.Dense(10, tf.keras.activations.softmax())) 

# Access non-existent layer
model.layer(10)