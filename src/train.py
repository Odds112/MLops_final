import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os

def load_data():
    
    (X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
    X_train, X_test = X_train / 255.0, X_test / 255.0  # Нормализация
    X_train = np.expand_dims(X_train, axis=-1)  # Добавляем канал
    X_test = np.expand_dims(X_test, axis=-1)
    return (X_train, y_train), (X_test, y_test)

def build_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')  # 10 классов
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_and_save_model():
    (X_train, y_train), (X_test, y_test) = load_data()

    # Увеличиваем размер до 32x32
    X_train = tf.image.resize(X_train, [32, 32])
    X_test = tf.image.resize(X_test, [32, 32])

    model = build_model()
    model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))
    
    # Сохраняем модель
    model.save('model.h5')

if __name__ == "__main__":
    train_and_save_model()
