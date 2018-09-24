from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import requests


def init_browser():

    # Initiate headless driver for deployment
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():


    browser = init_browser()
    mars_data = {}

    # Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('div', class_='list_text')
    news_title = results.find('div', class_='content_title').text
    news_par = results.find('div', class_='article_teaser_body').text

    mars_data["news_title"] = news_title
    mars_data["news_par"] = news_par

    print("Mars News Obtained")
    
    # Featured Image
    map_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    
    browser.visit(map_url)
    browser.find_by_id('full_image').click()
    featured_image_url = browser.find_by_css('.fancybox-image').first['src']

    mars_data["featured_image_url"] = featured_image_url

    print("Mars Feature Image Obtained")


    # Mars Weather

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    
    browser.visit(weather_url)
    weather_html = browser.html
    weather_soup = BeautifulSoup(weather_html, 'html.parser')
    weather_results = weather_soup.find('div', class_='js-tweet-text-container')
    mars_weather = weather_results.find('p', class_='tweet-text').text

    mars_data["mars_weather"] = mars_weather

    print("Mars Weather Obtained")

    # Mars Facts

    facts_url = 'https://space-facts.com/mars/'
    
    facts_table = pd.read_html(facts_url)
    table_df = facts_table[0]
    table_df.columns = ['Description', 'Facts']
    html_table = table_df.to_html()
    html_table.replace('\n', '')

    mars_data["html_table"] = html_table

    print("Mars Facts Obtained")

    # Mars Hemispheres
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    browser.visit(hemi_url)
    hemi_cerberus = browser.find_by_tag('h3')[0].text
    browser.find_by_css('.thumb')[0].click()
    hemi_first_img = browser.find_by_text('Sample')['href']
    browser.back()


    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    hemi_schiaparelli = browser.find_by_tag('h3')[1].text
    browser.find_by_css('.thumb')[1].click()
    hemi_second_img = browser.find_by_text('Sample')['href']
    browser.back()


    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    hemi_syrtis = browser.find_by_tag('h3')[2].text
    browser.find_by_css('.thumb')[2].click()
    hemi_third_img = browser.find_by_text('Sample')['href']
    browser.back()


    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    
    hemi_valles = browser.find_by_tag('h3')[3].text
    browser.find_by_css('.thumb')[3].click()
    hemi_fourth_img = browser.find_by_text('Sample')['href']
    browser.back()

    hemisphere_image_urls = [
    {'title': hemi_cerberus, 'img_url': hemi_first_img},
    {'title': hemi_schiaparelli, 'img_url': hemi_second_img},
    {'title': hemi_syrtis, 'img_url': hemi_third_img},
    {'title': hemi_valles, 'img_url': hemi_fourth_img}

    ]

    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    

    print("Mars Hemispheres Obtained")

 

    return mars_data

