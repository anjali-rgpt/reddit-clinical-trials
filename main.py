import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

import numpy as np
import pandas as pd
import reddit_scraper
import sentiment_analysis
import openai_message

search_term = input("Enter clinical trial keywords about which to search on Reddit and Web:")
users = reddit_scraper.search(search_term)
print(str(len(users.keys())), " unique users' posts and comments scraped")

info = []
for element in users.keys():
    for value in users[element]:
        new_el = [element, value, sentiment_analysis.sentiment(value)]
        info.append(new_el)

dataframe = pd.DataFrame(info, columns = ["user", "text", "sentiment"])

print("Counts by sentiment (posts and comments, not unique to different users):")
print(dataframe['sentiment'].value_counts())

# Ideally, users with a positive sentiment are already excited about the trial so we don't need to look at them
# We want to encourage users who are neutral about it, mainly.
# For those users who are opposed to clinical trials, it is best not to push them too much but we can give them more information.

# Let us sample two users and their posts/ comments from each category of negative and neutral

negative = dataframe.loc[dataframe.sentiment == "NEG"].sample(2)
neutral = dataframe.loc[dataframe.sentiment == "NEU"].sample(2)

for _, element in pd.concat([negative, neutral], axis = 0, ignore_index = True).iterrows():
    # print(element['user'], element["text"])
    print("\nMessage for user:", element["user"], " Sentiment:", element["sentiment"], ":")
    info = openai_message.info_search(search_term)
    print(openai_message.generate_message(info[0], element["user"], element["sentiment"], info[1]))
