import moviepy.editor as mp
import os
import requests
from scraper import getPost
from gpt import getStory
from tts import getTTS
from editer import editMovie
import utils


subreddit = "AskReddit"

postNum = utils.getPostNum() + 1

url = f"https://www.reddit.com/r/{subreddit}/top/?t=day"

title = getPost(subreddit, postNum)

getStory(title, postNum)

with open(f'assets/post{postNum}/story.txt', 'r') as file:
    story = file.read()

    getTTS(story, f'assets/post{postNum}/')
    

editMovie(f'assets/post{postNum}/')


