import pandas as pd
import string


def traits():
    df = pd.read_csv("tweetdata.csv")
    df1 = df
    df1['sentiment'] = df1['sentiment'].replace(['worry'], 'sadness')
    df1['sentiment'] = df1['sentiment'].replace(['anger'], 'hate')
    df1['sentiment'] = df1['sentiment'].replace(['relief', 'boredom'], 'neutral')
    df1['sentiment'] = df1['sentiment'].replace(['enthusiasm', 'love', 'fun', 'surprise'], 'happiness')
    df1 = df1[df1.sentiment != 'empty']

    df1 = df1.drop(labels=['tweet_id', 'author'], axis=1)

    def remove_punctuations(text):
        for punctuation in string.punctuation:
            text = text.replace(punctuation, '')
            text = text.lower()
        return text


    df1["content"] = df1['content'].apply(remove_punctuations)
    return df1
