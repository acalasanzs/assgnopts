# Importing required libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer


# List of sample sentences that we want to tokenize
sentences = ['I love my dog',
             'I love my cat',
             'you love my dog!',
             'Do you think my dog is amazing?',
             ]

# adding a "out of vocabulary" word to the tokenizer
tokenizer = Tokenizer(num_words = 100,oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)

test_data = ['i really love my dog',
             'my dog loves my manatee',
             ]

test_seq = tokenizer.texts_to_sequences(test_data)

print(word_index)
print(test_seq)