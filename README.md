# Grammy_Prediction
Project aimed at collecting data and using it to predict the winners of 3 Grammy awards

## Files 
1) Lyrics analysis - this notebook is used to generate features given the lyrics of a song
2) soy_analysis - given all the datasets, this notebook does some data exploration, tests various predictive models and finally uses an optimal model and feature subset to predict the winners for the Song of the Year
3) spotify_and_billboard - this notebook goes through a list of songs and gets the spotify features for them and also gets their billboard rankings during the year in question
4) trends - given the google trends history, this notebook extracts the mean and peak popularity
5) roy_analysis - given all the datasets, this notebook does some data exploration, tests various predictive models and finally uses an optimal model and feature subset to predict the winners for the Record of the Year
6) youtube.py - this script takes as argument a Youtube Data API Key and a string which is of the form year,song,artist and saves the comments for the song in a csv file along with the song metadata
7) youtube-service.py - this script is a helper script containing utilities used by the above script for fetching Youtube comments
8) reddit.py - this script reads the csv file containing the nominees and winners of the Grammy's for a particular award category and saves the comments extracted from reddit in separate csv files, one corresponding to each song. A developer account has to be created on Reddit and populated in the marked section in order to run this script