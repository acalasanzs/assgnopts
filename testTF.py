import io
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_datasets as tfds

""" eml = layers.Embedding(1000,5)

result = eml(tf.constant([1,2,3]))

print(result.numpy())
print(result.numpy().shape) """

(train_data, test_data), info = tfds.load('imdb_reviews/subwords8k', split=(tfds.Split.TRAIN,tfds.Split.TEST),with_info=True,as_supervised=True)

encoder = info.features['text'].encoder
# print(encoder.subwords[:20])
padded_shapes = ([None], ())
train_batches = train_data.shuffle(1000).padded_batch(10,padded_shapes=padded_shapes)

test_batches = train_data.shuffle(1000).padded_batch(10,padded_shapes=padded_shapes)

embedding_dim = 16
model = keras.Sequential([
                layers.Embedding(encoder.vocab_size,embedding_dim),
                layers.GlobalsAveragePooling1D(),
                layers.Dense(1, activation='sigmoid')])

model.compile(omptimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])
history = model.fit(train_batches,epochs=10,validation_data=test_batches,validation_steps=20)

history_dict = history.history
acc = history_dict['accuracy']
val_acc = history_dict['val_accuracy']
epochs = range(1,len(acc)+1)

plt.figure(figsize=(12,9))
plt.plot(epochs,acc, 'bo', label='Training acc')
plot.plot(epochs,val_acc,'b',label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.xlabel('Epochs')