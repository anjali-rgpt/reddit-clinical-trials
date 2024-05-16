import pandas as pd
import numpy as np
from pysentimiento import create_analyzer   # a toolkit for sentiment analysis

analyzer = create_analyzer(task = "sentiment", lang = "en")

def sentiment(sent):
    probabilities = analyzer.predict(sent).probas  # a dictionary with probability positive, negative, neutral
    print(probabilities)
    if max(probabilities, key = probabilities.get) in ["NEU", "POS"]:
        return (True, max(probabilities, key = probabilities.get))
    else:
        return (False, 0)

# print(sentiment("Hurray for me!"))