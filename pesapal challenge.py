# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 17:12:10 2022

@author: Simon
"""
#import neccesary liblaries
import requests
from bs4 import BeautifulSoup
from nltk import*


#pass on the website to be scrapped
res=requests.get('https://www.pesapal.com/about-us')

soup=BeautifulSoup(res.content,'html.parser')


#create an empty list of text to be scrapped
scrapped_text=[]
#extract text on the page
element=soup.select('body')

#removing all trailling lines \n and \t
for words in element:
    text=words.select('main')[0].text
    info=text.replace('\n',"")
    info2=info.replace('\t',"")


    scrapped_text.append(info2)
    
    
print(scrapped_text)

#separating words individually

sentense=sent_tokenize(scrapped_text)
tokenized_words=word_tokenize(sentense)
print(tokenized_words)

#getting count of unique words
dist_of_words=FreqDist(tokenized_words)
print(dist_of_words)




#comparing two pages
res=requests.get('input your webpage here')
soup=BeautifulSoup(res.content, 'html.parser')

page2=[]

element2=soup.select('location of your content')

for word in element2:
    text2=word.select(' ')[0].text
    info3=text2.strip('what you want to remove eg spaces and new lines')
    
    page2.append(info3)
    
#make one set and compare to the other list
set1=set(scrapped_text)
intersection=set1.intersection(page2)

common=list(intersection)

#print out list of common words in both
print(common)



#checking for non english words
 