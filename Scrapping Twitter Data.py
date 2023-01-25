#!/usr/bin/env python
# coding: utf-8


import streamlit as st
from datetime import datetime
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
from datetime import date,timedelta


def scraped_data(keyword,limit,start_date,end_date):
    
    # Creating list to append Scrapped data 
    tweets_list = []
    
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} since:{start_date}                                                                                     until:{end_date}').get_items()):                 
        if i>limit:
            break
        tweets_list.append([tweet.user.username,tweet.user.id,tweet.id,tweet.date,tweet.rawContent,
                 tweet.url,tweet.source,tweet.lang,tweet.replyCount,tweet.retweetCount,tweet.likeCount])
        
        
    # Creating a dataframe from the tweets list 
    Tweets_df = pd.DataFrame(tweets_list, columns=['Username','User_ID','Tweet Id','Datetime', 'Text',
                    'Url','Source','Language','ReplyCount','RetweetCount','LikeCount'])
        
    return Tweets_df    
        


def upload(df,keyword):
    # Making a Connection with MongoClient
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # database
    db = client["Twitter"]
    # collection
    col= db["Tweets"]
    # Converting the dataframe into list of dict
    Tweets_dict = df.to_dict("records")
    # Inserting the list of dict into database collection
    myquery={f'{keyword}_Tweets':Tweets_dict}
    col.insert_one(myquery)


# Input fatures of web app:
Keyword=st.text_input("Enter the keyword to scrape from Twitter",value="Data Scientist")

Starting_date=st.date_input("Tweets belonging from(starting date):",value=(date.today()
                                                                           -timedelta (days=100)))
    
Ending_date=st.date_input("Tweets upto(Ending date):",value=date.today ())
    
Tweets_counts=st.number_input("How much tweets you want to scrape(max 10000):",max_value=10000,
                                  value=100)
    
    

# Scraping the data and displaying it
if st.button("SCRAPE"):
    Tweets = scraped_data(Keyword, Tweets_counts, Starting_date, Ending_date)
    st.dataframe(Tweets)

# Uploading the scraped data in database
if st.button("UPLOAD"):
    Tweets = scraped_data(Keyword, Tweets_counts, Starting_date, Ending_date)
    upload_to_db=upload(Tweets,Keyword)
    
# Downloading the scraped data in deirable formats:

#For Downloading csv file
Tweets = scraped_data(Keyword, Tweets_counts, Starting_date, Ending_date)
Tweets_csv=Tweets.to_csv().encode('utf-8')
st.download_button("Download as CSV file",data=Tweets_csv,mime='text/csv')

#For Downloading json file
Tweets = scraped_data(Keyword, Tweets_counts, Starting_date, Ending_date)
Tweets_json=Tweets.to_json(orient ='records')
st.download_button("Download as JSON file",data=Tweets_json,mime="application/json")


