# Swedish Noun Gender Differentiator

A minimal Python project that guesses the grammatical gender of Swedish nouns. \
Swedish nouns come in two genders: common (takes en) and neuter (takes ett)—and there’s no reliable rule to decide which is which for every word, so you usually have to memorize them. \
This project uses a simple neural network trained on Swedish nouns to predict if a noun is common (en) or neuter (ett).

## Features
Predicts whether a given Swedish noun is en or ett \
Simple TensorFlow/Keras model \
Trained on a CSV of Swedish nouns with gender labels (sv.csv) \
Ready-to-use weights included (weights.keras)

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

Python 3.8+ \
TensorFlow/Keras \
Numpy

## Usage

Run the main script and input a noun: \
python main.py \
You’ll be prompted to enter a Swedish noun. The model will then output whether it predicts en or ett.

## Example
Model found. Loading weights...
Validating model...
142/142 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - accuracy: 0.9898 - loss: 0.0284
Enter a word: apelsin
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 31ms/step
EN apelsin
Confidence: 100.0 %
Enter a word: skrivbord
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 18ms/step
ETT skrivbord
Confidence: 100.0 %

## Limitations
Not perfect — Swedish noun gender is notoriously arbitrary and hard to predict reliably. \
Performance is constrained by dataset size and neural network simplicity. \
Not all Swedish nouns behave consistently; some can be both genders in rare cases.

## License
MIT
