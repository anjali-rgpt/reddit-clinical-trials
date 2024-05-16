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
5. Problem where scraping brings in stuff from murder trials instead of simply clinical trials.
6. What if Reddit users have unsecure usernames where they put their actual name? How to detect those?

# Examples:

`(virtualenv) anjalirg@DN0a1e84b7 reddit-clinical-trials % /Users/anjalirg/Stanford/reddit-clinical-trials/virtualenv/bin/python /Users/anjalirg/Stanford/reddit-clinical-trials/main.py`
`Enter clinical trial keywords about which to search on Reddit and Web:common cold`
`Reddit Data Scraped`
`2311  unique users' posts and comments scraped`
`Counts by sentiment (posts and comments, not unique to different users):`
`sentiment`
`NEU    1396`
`NEG    1097`
`POS     581`
`Name: count, dtype: int64`

`Message for user: shraddhasaburee  Sentiment: NEG :`
`Thank you for sharing your thoughts on the clinical trial. It's understandable to have reservations about participating in a study, especially when it involves investigational treatments.`

`Considering the burden upper respiratory infections pose on healthcare systems and the potential benefits of effective treatments for conditions like COPD, participating in this research could contribute to advancing medical knowledge and potentially improving outcomes for individuals affected by such illnesses.`

`The study you mentioned aims to evaluate the effectiveness and tolerability of Vapendavir in patients with COPD who develop rhinoviral infections. Vapendavir has shown promising results in inhibiting the virus in previous trials and has been well-tolerated. By participating, you not only contribute to advancing research in the field of respiratory virus infections but also potentially help in developing a new treatment that could benefit patients in the future.`

`It's important to weigh the pros and cons of participating in a clinical trial. While there are risks involved, such as unknown side effects of investigational drugs, the study is designed to ensure participant safety with regular monitoring and follow-up. Additionally, you will have access to healthcare professionals who will closely monitor your health throughout the study.`

`If you have any further questions or concerns, I encourage you to reach out to the study team or visit the official clinical trial website for more detailed information on interventions, outcomes, and eligibility criteria. Your participation could make a meaningful impact in advancing medical research and potentially improving treatments for individuals with respiratory conditions.`

`Message for user: KlaysToaster  Sentiment: NEU :`
`I understand that considering participation in a clinical trial can be a significant decision. The NEU clinical trial (NCT06106880) studying the efficacy of Vapendavir in patients with COPD who develop a rhinoviral infection presents an opportunity to contribute to the advancement of treatments for respiratory illnesses.`

`By participating in this trial, you may potentially help improve the quality of life for individuals with COPD by providing valuable data that could lead to the development of a more effective therapy for respiratory virus infections. Additionally, the study aims to assess the safety and tolerability of Vapendavir, which has shown promise in inhibiting rhinovirus and has been well-tolerated in previous studies involving over 650 participants.`

`It's important to note that your participation would involve careful monitoring and various assessments to ensure your health and safety throughout the study duration. The study procedures are comprehensive and aim to gather essential data to evaluate the efficacy and safety of Vapendavir in treating rhinoviral infections in patients with COPD.`

`If you are interested in learning more about the NEU clinical trial and how you can potentially contribute to advancements in respiratory virus treatments, I encourage you to review the detailed information provided on https://classic.clinicaltrials.gov/ct2/show/NCT06106880. Your participation could make a valuable impact in the research and development of therapies for respiratory illnesses.`

`Message for user: NEVS283  Sentiment: NEU :`
`Thank you for sharing the information about the clinical trial NEU focusing on the treatment of HRV infections in patients with COPD using Vapendavir. Participating in clinical trials like this one plays a crucial role in advancing medical research and potentially improving treatment options for individuals with COPD facing complications from rhinovirus infections.`

`Here are a few points that might encourage you to consider participating in this trial:`
`- The study aims to investigate the efficacy of Vapendavir in reducing the severity and frequency of acute exacerbations related to rhinoviral infections in COPD patients. By taking part, you could contribute to the development of a treatment that may improve the quality of life and overall health outcomes for individuals with COPD.`
`- Vapendavir has been shown to inhibit rhinovirus in previous studies and has been well-tolerated by participants, indicating its potential as a safe and effective treatment option.`
`- The study involves comprehensive monitoring and assessments to ensure participant safety and efficacy evaluation, with a well-structured protocol in place to guide the research process.`

`It's important to weigh the potential benefits of participating in the trial, such as contributing to the advancement of medical knowledge and potentially accessing innovative treatments, against any associated risks or inconveniences. If you are considering participating, I recommend discussing any questions or concerns you may have with the study team to gain a better understanding of the trial procedures and expectations.`

`For more detailed information on the trial interventions, outcomes, and eligibility criteria, you can always refer to the official clinical trial registry at https://clinicaltrials.gov/ct2/show/NCT06106880.`

`If you would like further assistance or have any specific questions about the trial, feel free to ask. Your participation could make a meaningful difference in the fight against respiratory infections in COPD patients.`



