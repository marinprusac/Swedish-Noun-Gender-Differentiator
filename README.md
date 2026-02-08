# Swedish Noun Gender Differentiator

A minimal Python project that guesses the grammatical gender of Swedish nouns. \
Swedish nouns come in two genders: common (takes en) and neuter (takes ett)—and there’s no reliable rule to decide which is which for every word, so you usually have to memorize them. \
This project uses a simple neural network trained on Swedish nouns to predict if a noun is common (en) or neuter (ett).

## Features
Predicts whether a given Swedish noun is en or ett \
Simple TensorFlow/Keras model \
Trained on a CSV of Swedish nouns with gender labels (sv.csv) \
Ready-to-use weights included (weights.keras)

The program splits the data into 70% train set, 15% validation set and 15% test test.
The model currently only optimizes the epochs number hyperparameter, but it is enough to score a test accuracy rate of around 90-95%.

## Project Structure
. \
├── main.py             # Entry point / inference script \
├── sv.csv              # Swedish nouns dataset \
├── weights.keras       # Saved neural network weights \
├── .gitignore \
└── README.md

## How It Works
Swedish has two grammatical genders for nouns: \
Common gender — most nouns, use the article en \
Neuter gender — a minority, use the article ett \
The model in this repo is trained to learn patterns from the training data (sv.csv) and give you a gender guess for new nouns.

## Requirements

Python 3.8 - 3.12 \
TensorFlow/Keras \
Numpy

## Usage

Run the main script: python main.py \
It might ask your whether you want to retrain the model if you already have the weights saved. \ 
You’ll be prompted to enter a Swedish noun. The model will then output whether it predicts en or ett.

## Example
Model found. Retrain? [y/n] _y_

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8147 - loss: 0.4070 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8176 - loss: 0.3898 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8426 - loss: 0.3679 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8338 - loss: 0.3688 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8309 - loss: 0.3806 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.8515 - loss: 0.3977 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.8382 - loss: 0.4401 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.8544 - loss: 0.5251 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.8441 - loss: 0.5389 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8353 - loss: 0.5272 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.8500 - loss: 0.5825 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.8485 - loss: 0.5870 

22/22 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.8485 - loss: 0.6091 

Done!

Testing model...

142/142 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - accuracy: 0.9406 - loss: 0.2101

Done!

Enter a word: _apelsin_

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 32ms/step

EN apelsin

Confidence: 100.0 %

Enter a word: _skrivbord_

1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 18ms/step

ETT skrivbord

Confidence: 99.0 %

## Limitations
Not perfect — Swedish noun gender is notoriously arbitrary and hard to predict reliably. \
Performance is constrained by dataset size and neural network simplicity. \
Not all Swedish nouns behave consistently; some can be both genders in rare cases.

## License
MIT
