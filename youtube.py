from apiclient.discovery import build
from pprint import PrettyPrinter
import pandas as pd
import time
from datetime import datetime
import sys 

key = sys.argv[1]
songs = ' '.join(sys.argv[2:])
youtube = build('youtube','v3',developerKey = key)


#Print the total number of results
#request = youtube.search().list(q='Easy on Me by Adele',part='snippet',type='video',maxResults=1)
#res = request.execute()
#pp = PrettyPrinter()
#pp.pprint(res)

#https://www.youtube.com/watch?v=giEKq_brSY4
#Print the title
#for item in res['items']:
#    print(item['id']['videoId'])



from youtube_service import YoutubeService

lines = [songs]
for i in lines:
    year, song, artist = i.split(',')
    
    print(song,artist,year)
    request = youtube.search().list(q=song[1:len(song)-1] +' by '+artist,part='snippet',type='video',maxResults=1)
    res = request.execute()
    timepublished = datetime.fromisoformat(res['items'][0]['snippet']['publishTime'][:-1] + '+00:00')
    print(timepublished.year, year)
    if(timepublished.year==int(year)-1) or (timepublished.year==int(year)-2):
        print("here")
        f= open('soy_comments/'+song+"_"+artist+'.csv','w')
        f.write("song,artist,comment,timestamp\n")
        video_url = 'https://www.youtube.com/watch?v='+res['items'][0]['id']['videoId']
        print(video_url)
        include_replies = False
        service = YoutubeService(video_url, key)
        all_comments = list(service.get_comment_threads(include_replies, year))
       
        if len(all_comments) >= 1:
            
            length = len(all_comments)
            for j in range(0,length):
                f.write(song+","+artist+","+all_comments[j]+"\n")
        f.close()
    time.sleep(1)
 
