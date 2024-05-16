# reddit-clinical-trials
Project for take-home assignment involving scraping Reddit for data about clinical trials, sentiment analysis and creating personalized messages

# How to run this:

Simple! Just open a terminal and run

`python3 main.py`

after cloning this repository.

>Note: There is a hidden config.py file with the OPENAI_API_KEY value which is not in the GitHub repository. 

# What you should see

The code runs three things. The first is the Reddit Web Scraper which uses the PRAW library to scrape data. 

## Web Scraper

Found in reddit_scraper.py
The idea is that you pass a keyword into the search() function of the reddit_scraper.py file. This function then creates multiple combinations of search queries, including the keywords "health conditions" and "clinical trials" to expand the search space. The required subreddits are found and stored in a list, and the "all" pseudo-subreddit is also included. 
Each of these subreddits is then searched through for the terms "clinical trials" to get relevant submissions (posts and comments). A dictionary of users is returned where the keys are the user names and the values are a list of contributed posts/comments on the subject.
Since this is Reddit, user privacy is maintained through the anonymous usernames. No identifying information is collected. 

## Sentiment Analysis

Found in sentiment_analysis.py

We use the pysentimiento library to perform sentiment analysis. This library can not only do simple sentiment classification into positive, negative, and neutral, but can also do a more complex and fine-grained emotion detection. We choose to use the simple sentiment analysis here and we assume that the posts are in the English language.

The function sentiment() takes in a sentence and returns the sentiment with the highest predicted probability.

## OpenAI Message Generation

The OpenAI message generation is done with the ChatGPT (GPT-3.5 Turbo) model API and the key is not committed to the repository for financial and privacy issues. You can choose to use your own config file with your OpenAI API Key. 

The assistant is given a polite and informative personality and is told to be persuasive but not pushy. A larger prompt feeds in information about the clinical trial (scraped using BeautifulSoup from clinicaltrials.gov), the user name (Reddit), and the user sentiment about that clinical trial. 
The prompt is as follows:
>PROMPT = "Here is information about a clinical trial: {}. This is the sentiment of this user named {} about the clinical trial: {}. Generate a personalized message for the user encouraging them to participate in the clinical trial. Add relevant supporting information as required. Always use {} for details on interventions, outcomes, and eligibility. Always discuss pros and cons. If user is neutral, be more informative and persuasive. If user is negative, give them information but do not push them."

## Main.py 

The main file executes these steps in order with messages as necessary. At the end, we explore OpenAI API message generation for only two samples from the negative and neutral sentiment for cost reasons. We pick negative and neutral because people with a positive sentiment will generally be more likely to participate in and know about the clinical trial already. Negative people might need more information to potentially change their mind, and neutral people can be persuaded a bit more. 

# Challenges
1. Scraping takes time
2. How to get relevant keywords (or subreddits about related health conditions) without explicitly encoding them in?
3. Cost issues with OpenAI
4. Informativeness - can use RAG or some additional knowledge base to supplement prompts with better information / use LLM agents capable of web access so that prompt size is kept to a minimum



