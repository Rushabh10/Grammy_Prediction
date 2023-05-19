import requests
import bs4
import json


f1 = open('record_of_the_year.csv','w')
f1.write('year,award category,song,artist,wasWinner\n')
for y in range(0,65):
	with open("roy_html/"+str(y)+'.html', 'r') as f:
		contents = f.read()
	soup = bs4.BeautifulSoup(contents, "html5lib")
	table = soup.find('section', attrs = {'id':'627'}) 
	winner = table.findAll('div', attrs={'class':'awards-category-link'})
	win = table.findAll('div',attrs={'class':'w-full text-center md-xl:text-left text-17 md-xl:text-22 mr-10px md-xl:mr-30px font-polaris font-bold md-xl:leading-8 tracking-wider'})
	nominees = table.findAll('div', attrs={'class':'awards-nominees-link'})
	nom = table.findAll('div',attrs={'class',"w-full text-left md-xl:text-22 text-17 mr-10px md-xl:mr-30px font-polaris font-bold md-xl:leading-8 tracking-wider flex flex-row justify-between"})

	winner_songs = []
	winner_artists = []
	nominee_songs = []
	nominee_artists = []
	for i in winner:
		winner_artists.append(i.text)

	for i in win:
		winner_songs.append(i.text)

	for i in nominees:
		nominee_artists.append(i.text)

	for i in nom:
		nominee_songs.append(i.text)

	print('winner :')
	for i in range(len(winner_songs)):
		print(winner_songs[i],winner_artists[i])

	print('nominee')
	for i in range(len(nominee_songs)):
		print(nominee_songs[i],nominee_artists[i])

	
	for i in range(len(winner_songs)):
		f1.write(str(y+1958+1)+',Record of the year,'+winner_songs[i].replace('+','').replace(',',';').replace('\\n','').strip()+','+winner_artists[i].replace(',',';').replace('\\n','').strip()+',yes\n')

	#nominees
	for i in range(len(nominee_songs)):
		f1.write(str(y+1958+1)+',Record of the year,'+nominee_songs[i].replace('+','').replace(',',';').replace('\\n','').strip()+','+nominee_artists[i].replace(',',';').replace('\\n','').strip()+',no\n')

f1.close()
