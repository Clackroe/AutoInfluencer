import moviepy.editor as mp
import os
import requests
from scraper import getPost
from gpt import getStory
from tts import getTTS
from editer import editMovie
import utils

if (not os.path.exists('assets')):
    os.mkdir('assets')
if (not os.path.exists('gameplay-clips')):
    os.mkdir('gameplay-clips')
    raise Exception("Please put gameplay clips in the gameplay-clips folder. Clips should be .mp4, and should be at least 90 seconds long. (Preferably 5 minutes or longer.))")
if (not os.path.exists('env.py')):
    raise Exception("Could not locate the 'env.py'. This is most likely due to it still being named 'env[REMOVEME].py'. Please rename it to 'env.py' and fill in the required fields. ")


subreddit = "AskReddit"

postNum = utils.getPostNum() + 1

url = f"https://www.reddit.com/r/{subreddit}/top/?t=day"

title = getPost(subreddit, postNum)

getStory(title, postNum)

with open(f'assets/post{postNum}/story.txt', 'r') as file:
    story = file.read()

    getTTS(story, f'assets/post{postNum}/')
    

editMovie(f'assets/post{postNum}/')


