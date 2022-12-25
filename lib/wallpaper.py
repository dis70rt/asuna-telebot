from urllib.request import urlopen
import random
import praw

reddit = praw.Reddit(
    client_id="jRqKwE1Z7i7pMo8JdYZ7pA",
    client_secret="XXjqZC6iKumo55V_-jW5yqGLa4uebw",
    user_agent="asuna_bot")

subreddit = reddit.subreddit("animewallpaper")
URL_top = []
URL_hot = []

def wallpaper(TYPE: str):
    if str == "hot":
        for submission in subreddit.hot(limit=50):
            URL_hot.append(submission.url)
        return random.choice(URL_hot)
    else :
        for submission in subreddit.top(limit=50):
            URL_top.append(submission.url)
        return random.choice(URL_top)