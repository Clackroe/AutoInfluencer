from selenium import webdriver
from selenium.webdriver.common.by import By
import os



driver = webdriver.Chrome()


def take_screenshot(url, ID, title, postNum):
    
    driver.get(url)
    
    element = driver.find_element(By.ID, ID)
    
    os.mkdir(f"assets/post{postNum}")
    
    element.screenshot(f'assets/post{postNum}/post.png')
    
    driver.quit()

