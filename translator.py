from googletrans import Translator

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_in_hindi(text):
	translator = Translator()
	value = translator.translate(text,dest="hi")
	return value.text



def get_utube(textToSearch):
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,'html.parser')
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	    var = 'https://www.youtube.com' + vid['href']
	    break
	return var
