""" Module serve as developing consistency score out of the list of 100+ influencers
    prepared for the streaming input;
    - important notes for input spec is on README.md
    Author : JungHwan Park
    Date : 08.05.2021
    Email : jpark143@g.ucla.edu
    Content : parsing data and developed consistency score
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

# Setting up Selenium Webdriver to open the browser
options = webdriver.ChromeOptions()
options.add_argument('user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'/Users/jpark143g.ucla.edu/chromedriver')

# Retreiving the list of profiles and urls and assign them as lists
d = pd.read_excel('/Users/jpark143g.ucla.edu/book.xlsx')
urls_series = d.iloc[:,1]
urls = urls_series.tolist()

profile_series = d.iloc[:,0]
columns = profile_series.tolist()

# Looping urls, main codebase
data = []
for url, column in zip(urls, columns) :
    # Open url(influencer's page)
    driver.get(url) 

    time.sleep(2)
    
    # Sending request to achieve parsed data through proxy url(ScrapingBee.com/api/v1)
    def send_request():
        webdriver = Chrome(executable_path=r'/Users/jpark143g.ucla.edu/chromedriver')
        response = webdriver.request(
            'GET',
            url='https://app.scrapingbee.com/api/v1/',

            params={
                'api_key': 'RWV5PH4SRGKQIEM2GV38FMXI5PY6LV4V2MPPRGX4Q90EALR5E6PO8HZ795T0480JRNKY05IANVXFM6AA',
                'url': url, 
                'render_js': 'false',
                'premium_proxy': 'true', 
                #'country_code':'us'
            },

        )
        return(response)
    
    r = send_request()
    # BeautifulSoup to parse html
    soup = BeautifulSoup(r.content, 'html.parser') 
    str1 = str(soup) # Coerce soup to string
    # Regular expression to extract timestamps.
    m = re.findall(r"""(["'])taken_at_timestamp\1:(\d+)""", str1) 
    unix = [x[1] for x in m]
    now = datetime.now() # Datetime now.
    # Extracted unix timestamps are valid until 12th value
    # Getting the difference between the last timestamp of the posting and the datetime.now() to get the interval.
    # Consistency score is calculated by the number of timestamps(=number of postings) divided by interval.
    if len(unix) > 12 :
        twelveth = sorted([datetime.fromtimestamp(int(unix[i])).strftime('%Y-%m-%d') for i in range(len(unix))])[-12]
        twelveth_datetime = datetime.strptime(twelveth, '%Y-%m-%d')
        con = now - twelveth_datetime
        seconds_in_day = 24 * 60 * 60
        a = divmod(con.days * seconds_in_day + con.seconds, 60)
        interval = a[0]/(60*24)
        consistency_score = 12/interval
        
        data.append({column : consistency_score

                    })
        time.sleep(2)
    else : 
        try :
            print(column)
            nth = sorted([datetime.fromtimestamp(int(unix[i])).strftime('%Y-%m-%d') for i in range(len(unix))])[0]
            nth_datetime = datetime.strptime(nth, '%Y-%m-%d')
            con = now - nth_datetime
            seconds_in_day = 24 * 60 * 60
            a = divmod(con.days * seconds_in_day + con.seconds, 60)
            duration = a[0]/(60*24)
            consistency_score = len(unix)/duration
            data.append({column : consistency_score})  
        except : 
            pass
        #print(column)
        time.sleep(3)