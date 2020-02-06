#IMPORTS

import warnings
warnings.filterwarnings('ignore')
# Beautiful Soup parses HTML documents in python.
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from collections import OrderedDict
import math
from urllib.error import HTTPError
from time import sleep
import csv

def make_soup(url):
    uClient = uReq(url)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    return page_soup

def list_page_url(page_count):
    page_lst=[]
    for i in range(1,page_count+1):
        lst.append('https://www.makeupalley.com/product/searching?CategoryID=7&NumberOfReviews=100&page={}'.format(i))
    return page_lst

def prod_page_url(page_lst): 
    prod_lst = []
    for l in page_lst:
        s = make_soup(l)
        prod_links = s.findAll('a',{'class':'item-name'})
        prod_links = list(OrderedDict.fromkeys(prod_links))
        for p in prod_links:
            prod_url.append('https://www.makeupalley.com{}'.format(p['href']))
    return prod_lst
    
def get_review_page_count(url):
    s = make_soup(url).find('a',{'class':'overall-rating'}).get_text()
    pages = ''
    for i in range(len(s)): 
        if (s[i].isdigit()): 
            pages = pages+ str(s[i])
    return math.ceil((int(pages))/10)

def all_reviews(prod_lst)
    all_links = []
    for i in prod_lst:
        pages = get_review_page_count(i)
        for j in range(1,pages):
            all_links.append(i+'?page={}#reviews'.format(j))


def generate_csv(all_links):
    with open(file='makeup_alley_data.csv',mode='w') as fd:
        writer = csv.writer(fd)
        writer.writerow(['Product','Brand', 'Review', 'Rating', 'User'])
   
    for indx, i in enumerate(all_links):          
        #GET HTML
        try:
            s = make_soup(i)
        except:
            HTTPError
            sleep(2) # wait 2 seconds
            continue
       
        #GET FEATS   
        try:
            product_c = s.find('div',{'class':'headline'}).get_text()
        except:
            AttributeError
            product_c = ''
        
        try:
            brand_c = s.find('span',{'class':'brand'}).get_text()
        except:
            AttributeError
            brand_c = ''
            
        try:
            review_c = s.findAll('span',{'class': 'review-text'})
        except:
            AttributeError
            continue
        
        try:
            user_c = s.findAll('div',{'class':'__UserLink__'})    
        except:
            AttributeError
            continue
        
        try:
            rating_c = s.findAll('span',{'class': 'rating-value'})
        except:
            AttributeError
            continue
            
        print(indx)
        for j in range(10):
            newrow = product_c, brand_c
            with open(file='makeup_alley_data.csv',mode='a', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerow([product_c, brand_c, review_c[j].get_text(), rating_c[j].get_text(), user_c[j].get_text()])

    