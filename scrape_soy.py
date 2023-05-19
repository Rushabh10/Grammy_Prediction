import time 
start_time=time.time()
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

wiki=requests.get('https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year').text
soup = BeautifulSoup(wiki, 'html.parser')

scraped_tables = soup.find_all('table',{'class':'wikitable sortable'})
years = []
songs = []
artists = []
for table in scraped_tables:
    
    year_tag = table.find_all('a', text = re.compile(r'.*([1-3][0-9]{3})'))
    for y in year_tag:
        years.append(y.text)
    lists_head=table.find_all('ul')
    for lists_head_item in lists_head:
        song_list = []
        artist_list = []
        lists=lists_head_item.find_all('li')
        for item in lists:
            record=(item.text)
            song_list.append(record.split('"')[1])
            artist_list.append(record.split('performed by')[1].split('featuring')[0])
        songs.append(song_list)
        artists.append(artist_list)
            


Nominations=pd.DataFrame(list(zip(years, songs, artists)),columns=['Year','Song','Performer'])

print(Nominations)
pos = 0
for i in years:
    if i=='1978':
        break
    pos+=1
    
years1 = years[:pos+1]+['1978'] + years[pos+1:]
Winner_songs=[]
Winner_perform=[]
for table in scraped_tables:
    rows=table.findAll('tr')
    for row in rows:
       
        
        colum= row.findAll('td')
        id=-1
        for col in colum:
                        
            if id==0:
                Winner_songs.append(col.text.split('"')[1])
            
            elif id==1:
                Winner_perform.append(col.text.strip())
            id=id+1


Winners=pd.DataFrame(list(zip(years1,Winner_songs,Winner_perform)),columns=['Year','Song','Performer'])

print(Winners)

f = open('song_of_the_year.csv','w')
f.write('year,award category,song,artist,wasWinner\n')
for i in zip(years1,Winner_songs,Winner_perform):
    f.write(i[0]+',Song of the Year,'+i[1].replace(',','')+','+i[2].replace(',','')+',yes\n')

#nominees
for i in zip(years,songs, artists):
    for j in range(len(i[1])):
        f.write(i[0]+',Song of the Year,'+i[1][j].replace(',','')+','+i[2][j].replace(',','')+',no\n')

f.close()
