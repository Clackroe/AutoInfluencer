import requests
from bs4 import BeautifulSoup as bs
from screenshots import take_screenshot
import os



def getPost(subreddit, postNum):
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=day"

    headers = {'User-Agent': 'chrome'}

    response = requests.get(url, headers=headers)

    soup = bs(response.content, "html.parser")

    posts = soup.find_all('div', attrs={"data-testid": "post-container"})

    titles = []

    for post in posts:
        title = post.find('h3')
        titles.append(title)
    
    post_to_create = 0
    
    while (checkIfCreated(titles[post_to_create])):
        post_to_create += 1
        
        if post_to_create == len(titles):
            post_to_create = 0
            break
    
    
    with open('posts.txt', 'a') as file:
        file.write(f"{titles[post_to_create].text}\n")
    
    take_screenshot(url, posts[post_to_create].get('id'), titles[post_to_create].text, postNum)
    
    return titles[post_to_create]
        


def checkIfCreated(title):
    file = open("posts.txt").readlines()
    
    for line in file:
        if title.text in line:
            return True
    return False
    

    
    

    
