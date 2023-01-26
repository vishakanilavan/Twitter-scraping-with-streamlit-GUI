
#Twitter-scraping-with-streamlit-GUI

Data is abundantly available in social media nowadays.This project helps in collecting tweets from Twitter  and downloading the tweets in GUI environment...



## WORKFLOW OF THE PROJECT:
```bash
1.)I/P FEATURES  FOR SCRAPPING TWEETS:
 ```
 Get the input of the KEYWORD to search, DATE RANGE, No of Tweets from the user by GUI setup enviroment built by streamlit library
```bash
 2.)SCRAPING AND DISPLAYING THE DATA:
 ```
 After getting input, scrap the desired tweets and display the tweets in tabular form in the web GUI.

 ```bash
 3)UPLOAD THE SCRAPED DATA IN DATABASE:
 ```
 Next, Upload the scraped tweeets into mongodb database for future accessing
```bash
 4.)DOWNLOAD THE SCRAPED DATA:
 ```
 The final step is downloading the scraped tweets in the required format namely CSV,JSON format.
## EXECUTION OF THE PROJECT:
## Pre requisite Installation
You should install the latest version of python for executing this project


Install some python libraries  

```bash
  pip install streamlit
  pip install pymongo
  pip install pandas
  pip install snscrape
```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/vishakanilavan/Twitter-scraping-with-streamlit-GUI
``
```


Change the directory to directory of project file

```bash
Go to the downloaded/cloned project directory in prompt cmd
```

```bash
for example:
  cd C:\Users\Admin PC\Downloads
```

Now Run the below command
```bash
streamlit run "filename.py"
```
```bash 
for example:
streamlit run Scrapping Twitter Data.py
```

Accessing the localhost server

```bash
 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.43.83:8501
```

  click the above link to display the created Twitter scraping web app


## Screenshots

![img]https://i.imgur.com/Mfz7ffK.jpg


## Demo
Here's My demo video  of the project
in linkedin's profile

https://www.linkedin.com/in/vishaka-nilavan-9345aa138/

