
import time
import re
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests
from selenium import webdriver
import pymongo
from sys import platform


# In[2]:

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape():
    browser = init_browser()
    mars_data_scrape = {}


    mars_news = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news)
    time.sleep(2)
    html = browser.html
    news_soup = bs(html, 'html.parser')
    print(news_soup)
