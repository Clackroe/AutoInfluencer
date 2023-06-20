from utils.GPTUtils import gpt
from utils.GatheringUtils import choosePost, takeScreenshot
from utils.TTSUtils import getTTS

subreddit = "AskReddit"
category = "top"
time = "day"

title, post = choosePost(subreddit, category, time)
takeScreenshot(post, subreddit, category, time, "assets")

story = gpt(title, "assets")

getTTS(story, "assets")
