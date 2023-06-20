from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


# category can be: "top", "hot", or "new"
# time can be: "hour", "day", "week", "month", "year", or "all"
def getRedditHTML(subreddit, category, time):

    if category not in ["top", "hot", "new"]:
        raise ValueError(
            f"Invalid category: {category}. Category must be one of the following: 'top', 'hot', or 'new'")

    if time not in ["hour", "day", "week", "month", "year", "all"]:
        raise ValueError(
            f"Invalid time: {time}. Time must be one of the following: 'hour', 'day', 'week', 'month', 'year', or 'all'")

    RedditURL = f"https://www.reddit.com/r/{subreddit}/{category}/?t={time}"

    ret = requests.get(RedditURL, headers={'User-Agent': 'chrome'})
    return ret


def getPostsHTML(redditHTML):
    soup = bs(redditHTML.content, "html.parser")
    posts = soup.find_all('div', attrs={"data-testid": "post-container"})
    # print("Posts: " + str(posts))
    return posts


def getPostTitles(postsHTML):

    titles = []
    # posts = postsHTML

    # print("PostsHTML: " + str(postsHTML))

    for post in postsHTML:
        # print("Posts: " + post)
        title = post.find('h3')
        titles.append(title)

    return titles


def getPostID(post):
    return post.get('id')


def titleCreated(title):
    file = open("utils/data/posts.txt").readlines()
    for line in file:
        if title.text in line:
            return True
    return False


def takeScreenshot(post, subreddit, category, time, outputDir, headless=True):

    if not os.path.exists(outputDir):
        print("Directory doesnt exist. Creating directory...")
        os.mkdir(outputDir)

    options = webdriver.ChromeOptions()
    options.headless = headless

    driver = webdriver.Chrome(chrome_options=options)
    # driver.execute_script(
    #     "document.body.style['-webkit-transform'] = \"scale(2.0)\";")
    driver.get(f"https://www.reddit.com/r/{subreddit}/{category}/?t={time}")
    postID = getPostID(post)
    element = driver.find_element(By.ID, postID)
    element.screenshot(f'{outputDir}/screenshot.png')
    driver.quit()


def choosePost(subreddit, category, time):
    posts = getPostsHTML(getRedditHTML(
        subreddit=subreddit, category=category, time=time))
    titles = getPostTitles(posts)

    # print(f"Titles: {titles}")

    num = 0
    while (titleCreated(titles[num])):
        num += 1
        if num == len(titles):
            num = 0
            break

    with open('utils/data/posts.txt', 'a', encoding="utf-8") as file:
        file.write(f"{titles[num].text}\n")

    return titles[num], posts[num]
