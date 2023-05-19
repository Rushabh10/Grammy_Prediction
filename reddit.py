#######
# IMPORT PACKAGES
#######

import praw
import pandas as pd
from datetime import datetime
import pytz

utc=pytz.UTC

# Acessing the reddit api


reddit = praw.Reddit(client_id="",#my client id
                     client_secret="",  #your client secret
                     user_agent="" #user agent name
                     )

sub = ['all']  # make a list of subreddits you want to scrape the data from

lines = open('record_of_the_year.csv').read().split('\n')

lines=lines[1:]
lines=lines[:len(lines)-1]
p=0
for i in lines:
    if i.split(',')[0] == '2005':
        break
    p+=1
lines=lines[p:][::-1]
for l in lines:
    year, category, song, artist, was_winner = l.split(',')

    for s in sub:
        subreddit = reddit.subreddit(s)   # Chosing the subreddit


    ########################################
    #   CREATING DICTIONARY TO STORE THE DATA WHICH WILL BE CONVERTED TO A DATAFRAME
    ########################################

    #   NOTE: ALL THE POST DATA AND COMMENT DATA WILL BE SAVED IN TWO DIFFERENT
    #   DATASETS AND LATER CAN BE MAPPED USING IDS OF POSTS/COMMENTS AS WE WILL 
    #   BE CAPTURING ALL IDS THAT COME IN OUR WAY

    # SCRAPING CAN BE DONE VIA VARIOUS STRATEGIES {HOT,TOP,etc} we will go with keyword strategy i.e using search a keyword
        query = [artist + ' - '+ song[1:len(song)-1]]
        print(query[0])

        for item in query:
            post_dict = {
                "title" : [],
                "score" : [],
                "id" : [],
                "url" : [],
                "comms_num": [],
                "created" : [],
                "body" : []
            }
            comments_dict = {
                "comment_id" : [],
                "comment_parent_id" : [],
                "comment_body" : [],
                "comment_link_id" : [],
                'timestamp': []
            }
            for submission in subreddit.search(query,limit = 5):
                print(submission.title)
                post_dict["title"].append(submission.title)
                post_dict["score"].append(submission.score)
                post_dict["id"].append(submission.id)
                post_dict["url"].append(submission.url)
                post_dict["comms_num"].append(submission.num_comments)
                post_dict["created"].append(submission.created)
                post_dict["body"].append(submission.selftext)
                
                ##### Acessing comments on the post
                submission.comments.replace_more(limit = 1)
                for comment in submission.comments.list():
                    timestamp = utc.localize(datetime.fromtimestamp(comment.created_utc))
                    year = 2023
                    start = datetime.fromisoformat(str(int(year)-2)+'-10-01T00:00:00.000Z'[:-1] + '+00:00')
                    end = datetime.fromisoformat(str(int(year)-1)+'-09-30T00:00:00.000Z'[:-1] + '+00:00')
                    if(start <= timestamp and timestamp <= end):
                        comments_dict["comment_id"].append(comment.id)
                        comments_dict['timestamp'].append(utc.localize(datetime.fromtimestamp(comment.created_utc)))
                        comments_dict["comment_parent_id"].append(comment.parent_id)
                        comments_dict["comment_body"].append(comment.body)
                        comments_dict["comment_link_id"].append(comment.link_id)
                
            if(len(comments_dict['comment_id'])>=1):
                post_comments = pd.DataFrame(comments_dict)
                post_comments.to_csv('roy_reddit/'+s+"_comments_"+ item.replace('/','') +"subreddit.csv")
            #post_data = pd.DataFrame(post_dict)
            #post_data.to_csv('roy_reddit/'+s+"_"+ item.replace('/','') +"subreddit.csv")

