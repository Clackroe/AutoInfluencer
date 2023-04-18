import moviepy.editor as mp
import os
import requests
from scraper import getPost
from gpt import getStory
import utils


subreddit = "AskReddit"

postNum = utils.getPostNum() + 1

url = f"https://www.reddit.com/r/{subreddit}/top/?t=day"

title = getPost(subreddit, postNum)

getStory(title, postNum)
