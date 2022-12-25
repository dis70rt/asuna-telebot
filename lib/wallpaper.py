from urllib.request import urlopen
import praw

reddit = praw.Reddit(
    client_id="jRqKwE1Z7i7pMo8JdYZ7pA",
    client_secret="XXjqZC6iKumo55V_-jW5yqGLa4uebw",
    user_agent="asuna_bot")

subreddit = reddit.subreddit("animewallpaper")

def wallpaper(TYPE: str):
    submission = subreddit.random()
    return submission.url

