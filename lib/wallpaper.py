from urllib.request import urlopen
import praw

reddit = praw.Reddit(
    client_id="jRqKwE1Z7i7pMo8JdYZ7pA",
    client_secret="XXjqZC6iKumo55V_-jW5yqGLa4uebw",
    user_agent="asuna_bot")

subreddit = reddit.subreddit("animewallpaper")

top = []
hot = []

def wallpaper(TYPE: str):
    if str == "hot":
        for submission in subreddit.hot(limit=50):
            hot = lists(submission)
        return hot[random.randint(0,50)].url
    else :
        for submission in subreddit.top(limit=50):
            top = lists(submission)
        return top[random.randint(0,50)].url

