#WebSrcaping script for Extracting the Football Matches data from a website called "adamchoi"

#Essential libraries are installed 
import selenium
import pandas as pd
from selenium import webdriver

#creating variables to store website url and the web driver path
website='https://www.adamchoi.co.uk/overs/detailed'
path='/Users/cjeev/Downloads/chromedriver'

#connecting the selenium web driver module to the chorme browser and fetching the website
driver=webdriver.Chrome(path)
driver.get(website)

#Locating the elements by their xpath and tag names
all_matches_button=driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()
rows=driver.find_elements_by_tag_name('tr')

#creating lists to store the table data elements from the extracted table row elements
date=[]
home=[]
score=[]
away=[]
for i in rows:
    date.append(i.find_element_by_xpath('./td[1]').text)
    home.append(i.find_element_by_xpath('./td[2]').text)
    score.append(i.find_element_by_xpath('./td[3]').text)
    away.append(i.find_element_by_xpath('./td[4]').text)
    
#Creating dataframe to have a tabular structure of extracted data and exporting it in csv format
df=pd.DataFrame({"Date":date,"home":home,"score":score,"away":away})
print(df)
df.to_csv("footballdataset.csv",index=False)
