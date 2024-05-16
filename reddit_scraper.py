import praw
import pandas as pd


# Define the user agent and the PRAW object for scraping Reddit 

user_agent = "Scraper by /u/LanguageDesignerAI"
reddit = praw.Reddit(
    client_id = "pl2t8ydJWHhX4Lq4D20vOg",
    client_secret = "V6urlUzhVkNIhCH7PFBWdDyLPYwZ5A",
    user_agent = user_agent
)

# We are searching the entirety of Reddit for relevant subreddits and posts
all = reddit.subreddit("all")

def search(keywords):
    users = {}
    
    subreddits = set()

    for k in [keywords, keywords + "health conditions", keywords + "health conditions" + "clinical trial", keywords + "clinical trial"]:
        name_search = reddit.subreddits.search_by_name(k)[:3]
        all_search = list(reddit.subreddits.search(k))[:3]
        # print("\n", name_search, all_search)

        for element in name_search + all_search:
            subreddits.add(element)
        subreddits.add(all)
    
    # print("\n", subreddits)

    for subreddit in subreddits:

        check = subreddit.search("clinical trials interest " + keywords, sort = "relevance")
        post_ids = [x.id for x in list(check)][:50]
        print("CHECK")
        for post_id in post_ids:
            submission = reddit.submission(post_id)
            try:
                users[submission.author.name].append(submission.selftext)
            except:
                users[submission.author.name] = [submission.selftext]

            submission.comment_sort = "top"
            submission.comments.replace_more(limit=7)
            for comment in submission.comments.list():
                try:
                    if hasattr(comment, "author"):
                        users[comment.author.name].append(comment.body)
                except:
                    try:
                        if hasattr(comment, "author"):
                            users[comment.author.name] = [comment.body]
                    except:
                        continue


    return users


search("epilepsy")



    
