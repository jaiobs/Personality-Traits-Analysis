from keras.preprocessing.text import Tokenizer
from keras import preprocessing as pp
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Embedding, Dense, LSTM


def model_personalitytraits(df1,txt):
    MAX_NB_WORDS = 2000
    MAX_SEQUENCE_LENGTH = 250
    EMBEDDING_DIM = 100
    tokenizer = Tokenizer(num_words=MAX_NB_WORDS, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
    tokenizer.fit_on_texts(df1['content'].values)
    word_index = tokenizer.word_index

    X = tokenizer.texts_to_sequences(df1['content'].values)
    X = pp.sequence.pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)\

    Y = pd.get_dummies(df1['sentiment']).values\

    sentiment_tensors = pd.get_dummies(df1['sentiment'].unique()).values

    res_dict = dict()
    j = 0
    for i in df1['sentiment'].unique():
        res_dict[i] = sentiment_tensors[j]
        j = j + 1



    model = Sequential()
    model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=X.shape[1]))
    model.add(keras.layers.core.SpatialDropout1D(0.2))
    model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(4, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.load_weights(os.getcwd()+r'/model.h5')
    print(type(txt))
    tweet = [txt]

    tweet = tokenizer.texts_to_sequences(tweet)
    tweet = pp.sequence.pad_sequences(tweet, maxlen=MAX_SEQUENCE_LENGTH)
    #print('Shape of data tensor:', tweet.shape)

    res = model.predict(tweet, verbose=0)

    res = (res == res.max(axis=1)[:, None]).astype('uint8')

    for key, value in res_dict.items():
        if (((res == value).all()) == True):
            return key
