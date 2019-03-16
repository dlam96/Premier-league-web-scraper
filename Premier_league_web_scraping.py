#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os


# In[2]:


# load url
url ="http://www.espn.co.uk/football/table/_/league/eng.1"

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)


# In[3]:


# load data values and append to data list
datalist = []
for i in range(1, 21):
    # pos = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[1]/table[1]/tbody/tr['+ str(i) +']/td/div/span[1]').text   

    teams = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[1]/table[1]/tbody/tr['+ str(i) +']/td/div/span[4]/a').text   

    gp = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[1]/span').text

    w = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[2]/span').text

    d = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[3]/span').text

    l = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[4]/span').text
    
    f = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[5]/span').text

    a = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[6]/span').text

    gd = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[7]/span').text

    p = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[5]/div[3]/div[1]/div/section/section/section/div[1]/section/table/tbody/tr/td[2]/div/div/div[2]/table/tbody/tr/td/table/tbody/tr['+ str(i) +']/td[8]/span').text

    datalist.append([teams, gp, w, d ,l ,f, a, gd, p])

driver.quit()


# In[4]:


# label columns and start row at 1
df = pd.DataFrame(datalist, columns=['Team', 'Games Played', 'Wins', 'Draw', 'Losses', 'Goals Scored', 'Goals Conceeded', 'Goal Difference', 'Points'])
df.index = df.index + 1
df.index.name = 'Position'


# In[5]:


df

