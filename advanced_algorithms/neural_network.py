import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation

def create_neural_network(input_shape, output_shape, hidden_layers, hidden_units, activation_function, dropout_rate):
    model = Sequential()
    model.add(Dense(hidden_units, input_shape=input_shape))
    model.add(Activation(activation_function))

    for _ in range(hidden_layers - 1):
        model.add(Dense(hidden_units))
        model.add(Activation(activation_function))
        model.add(Dropout(dropout_rate))

    model.add(Dense(output_shape))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
