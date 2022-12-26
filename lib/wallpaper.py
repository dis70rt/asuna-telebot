import praw
import random

reddit = praw.Reddit(
    client_id="jRqKwE1Z7i7pMo8JdYZ7pA",
    client_secret="XXjqZC6iKumo55V_-jW5yqGLa4uebw",
    user_agent="asuna_bot")

subreddit = reddit.subreddit("animewallpaper")

top = []
hot = []

for submission in subreddit.hot(limit=1000):
    hot.append(submission)

for submission in subreddit.top(limit=1000):
    top.append(submission)

def wallpaper(TYPE: str):
    if str == "hot":
        hpost = hot[random.randint(0,1000)]
        return (str(hpost.title), str(hpost.url))
    else :
        tpost = top[random.randint(0,1000)]
        return (str(tpost.title), str(tpost.url))

