import csv
import tensorflow as tf
import numpy as np
import os


def get_data(letter_count = 10):
    raw_data = []
    for line in csv.reader(open('sv.csv'), delimiter=','):
        raw_data.append(line)
    raw_data = raw_data[1:]
    data = []
    for data_point in raw_data:
        pos = data_point[7]
        if pos in ['noun-en', 'noun-ett']:
            lemma = data_point[6].upper().split(' ')[0].strip('.').replace('É', 'E')
            data.append((lemma, int(pos=='noun-en')))
    in_outs = []
    for data_point in data:
        word, label = data_point
        inputs = format_input(word, letter_count)
        label = np.array(label, dtype=np.float32)
        in_outs.append((inputs, label))
    return in_outs


def format_input(word, letter_count=10):
    alphabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"
    ]
    alphabet_dict = {alphabet[i]: [1] + [0] * i + [1] + [0]*(len(alphabet)-i-1) for i in range(len(alphabet))}
    inputs = []

    # reversed letters
    for i in range(min(len(word), letter_count)):
        letter = word[-(i + 1)]
        inputs.append(alphabet_dict[letter])

    # pad at the end if shorter than letter_count
    while len(inputs) < letter_count:
        inputs.append([0] * 30)

    # convert to NumPy arrays for TensorFlow
    inputs = np.array(inputs, dtype=np.float32)
    return inputs


def create_model(letter_count=10):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input((letter_count, 30)),  # (10,30)
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def train_model(model, data, save_file=None):
    X = np.stack([item[0] for item in data])  # shape (num_samples, letter_count, 30)
    Y = np.array([item[1] for item in data])  # shape (num_samples,)
    model.fit(X, Y, epochs=30)
    if save_file:
        model.save(save_file)

def make_prediction(model, word):
    word = word.upper()
    x = format_input(word)
    x = np.expand_dims(x, axis=0)  # shape (1, 10, 30)
    prediction = model.predict(x)[0][0]
    return prediction

def load_model(save_file):
    model = tf.keras.models.load_model(save_file)
    return model

def main():
    letter_count = 10
    file_name = 'weights.keras'
    if os.path.isfile(file_name):
        model = load_model(file_name)
    else:
        data = get_data(letter_count)
        model = create_model(letter_count)
        train_model(model, data, file_name)
    while True:
        word = input('Enter a word: ')
        prediction = make_prediction(model, word)
        if prediction >= 0.5:
            print('EN', word)
            print("Confidence:", round(prediction, 2)*100, "%")
        else:
            print('ETT', word)
            print("Confidence:", round(1-prediction, 2) * 100, "%")



if __name__ == '__main__':
    main()