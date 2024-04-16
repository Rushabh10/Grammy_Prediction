# Grammy_Prediction
The Grammy Awards are one of the most prestigious music awards in the world.Successfully predicting the winners presents a challenge, demanding a profound comprehension of the music industry and its evolving trends. In this study, we present an experimental Predictive Analytics tool that utilizes AI algorithms and harnesses alternative data sources to predict the winners in the categories of Song of the Year, Record of the Year, and Rap Song of the Year. Our method (1) collects, mines, and fuses data from various alternative sources, such as Billboard rankings, music features of the song, Google search volume, and lyrics, among other sources, and (2) trains AI algorithms to learn from historical data. Our empirical results indicate that the AI tool can accurately predict the winners of these three categories for the last three years. For Song of the Year, our algorithm indicates that energy, acousticness, and loudness were among the best predictive features for a Grammy-winning song. 
For Record of the Year, profanity and sadness were identified as some of the most predictive features. Meanwhile, for Rap song of the Year, negative sentiment, the number of words, and happiness score emerged as the key features for a Grammy-winning song.
The framework presented here has the potential to be utilized by artists for a data-driven approach to song writing and music production, enabling record labels and music fans to gain insights into the factors influencing the odds of winning an award.

## Files 
1) Lyrics analysis - this notebook is used to generate features given the lyrics of a song
2) soy_analysis - given all the datasets, this notebook does some data exploration, tests various predictive models and finally uses an optimal model and feature subset to predict the winners for the Song of the Year
3) spotify_and_billboard - this notebook goes through a list of songs and gets the spotify features for them and also gets their billboard rankings during the year in question
4) trends - given the google trends history, this notebook extracts the mean and peak popularity
5) roy_analysis - given all the datasets, this notebook does some data exploration, tests various predictive models and finally uses an optimal model and feature subset to predict the winners for the Record of the Year
6) youtube.py - this script takes as argument a Youtube Data API Key and a string which is of the form year,song,artist and saves the comments for the song in a csv file along with the song metadata
7) youtube-service.py - this script is a helper script containing utilities used by the above script for fetching Youtube comments
8) reddit.py - this script reads the csv file containing the nominees and winners of the Grammy's for a particular award category and saves the comments extracted from reddit in separate csv files, one corresponding to each song. A developer account has to be created on Reddit and populated in the marked section in order to run this script
9) scrape_soy - script to scrape the nominees and winners of song of the year
10) scrape_record - script to scrape the nominees and wineers of record of the year
11) scrape_rap - script to scrape the nominees and winners of best rap song
12) rapAnalysis - given all the datasets, this notebook does some data exploration, tests various predictive models and finally uses an optimal model and feature subset to predict the winners for the Rap Song of the Year
13) GeniusLyricsClient - contains lyricsgenius client code to fetch lyrics for songs.
