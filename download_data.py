'''
    Reference script fo townload data for Python2
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup as bs
import urllib#.request as urllib for Python 3
import time 

# configurations
beatles_url = "https://www.*.com/b/beatles.html"
kinks_url = "https://www.*.com/k/kinks.html"
beatles_band = "beatles"
kinks_band = "kinks"
base_dir = "data/"

url = beatles_url
band = beatles_band


# get to the home page
request = urllib.urlopen(url)
soup = bs(request, "lxml")


# get the name of all the albums
albums = soup.find_all("div", class_="album")
albums = [album.text.split(":")[1].strip().replace("\"", "") for album in albums]
print("total albums:", len(albums))
#(albums[0])


# write album names to a tile
albums_file = open(base_dir + band + "_albums.txt", 'w')
for album in albums:
    albums_file.write("%s\n" % album)

# get all the links
album_data = soup.find_all('div',attrs={"id" : "listAlbum"})
href_tags = album_data[0].find_all(href=True)
print("total songs:", len(href_tags))

songs_file = open(base_dir + band + "_songs_links.txt", 'w')
href_tags = [tag["href"].replace("..", "") for tag in href_tags]
for tag in href_tags:
    songs_file.write("%s\n" % tag)


# once the links are saved just load tags from the disk
songs_file = open(base_dir + band + "_songs_links.txt", 'r')
href_tags = songs_file.readlines()
print("links loaded:", len(href_tags))

# write title + lyrics to a file
lyrics_file = open(base_dir + band + str(lim) +"_file.txt", 'w')

all_lyrics = []
for idx, tag in enumerate(href_tags):
    print("song:", idx)
    # go to the page for each song
    song_url = "https://www.*.com" + tag
    try:
        song_request = urllib.urlopen(song_url)
        song_soup = bs(song_request, "lxml")
        song_name = song_soup.find_all('b')[1].text.replace("\"", "")
        # perform preprocessing on the string
        song_lyrics = song_soup.find_all('div', {'class': ''})[1].text
        song_lyrics = song_name + ":" + song_lyrics
        #print(song_lyrics)
        all_lyrics.append(song_lyrics)
        time.sleep(10)
    except:
        # save lyrics to a file if anything goes wrong
        for lyrics in all_lyrics:
            lyrics_file.write("%s\n" %lyrics)
        

# save lyrics to a file
for lyrics in all_lyrics:
    lyrics_file.write("%s\n" % lyrics)


    

