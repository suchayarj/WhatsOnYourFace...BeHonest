# Detect the Fake

**MOTIVATION**

My curiosity in beauty industry has gone beyond finding out what kind of chemicals are used in cosmetics. (See 'What on Your Face')

In the world of dominant online platform becomes the most used where people buy and trade things, fake online reviews are definitely unavoidable.
For example, scandal on Sunday Riley where it forced its employee to write reviews on its products given a quite thorough walkthrough so that it's hard to tell that the review's fake. For example, turn off cookies, review a few products that are not SR before actually review SR. 

My goal is to create a predictive model that identify the fake reviews on Sephora websiteu utilizing natural language processing 

**PIPELINE**

Webscrape (BeautifulSoup) --> Pandas DataFrame --> EDA --> NLP/Sentimental Analysis --> Model

**DATASET**

- Webscrape from www.makeupalley.com : I am treating reviews from this website as **more authentic** since this website's sole purpose is to have the beauty community share honest reviews, while Sephora is try to sell products 
- Sephora reviews, using 'github link'

**EDA**

Sentimental analysis


**MODEL**

With limited ability in obtaining instances on fake reviews, I decided to use One Class Classification from Support Vector Machine algorithm which is appropriate for Unsupervised Outlier Detection

