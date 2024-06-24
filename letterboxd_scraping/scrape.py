import requests
from bs4 import BeautifulSoup

import pandas as pd

username = '_temtae'

def scrape_film(link):

  URL = f'https://letterboxd.com/film/{link}/'
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, 'html.parser')

  # film header
  header = soup.find('section', class_='film-header-group')

  title = header.find('h1', class_='filmtitle').find('span').text
  year = header.find('div', class_='releaseyear').find('a').text
  directorlist = []
  directors = header.find('span', class_='directorlist').find_all('a', class_='contributor')
  for director in directors:
    directorlist.append(director.text)

  # details
  runtime = int(soup.find('p', class_='text-link text-footer').text.strip().split(' ')[0][:-5]) # in minutes

  genrelist = []
  genres = soup.find('div', id='tab-genres').find('div').find_all('a')
  for genre in genres:
    genrelist.append(genre.text)

  castlist = {}
  castmembers = soup.find('div', id='tab-cast').find('div').find_all('a')
  for member in castmembers: # limit number of members to display in html
    actor = member.text
    character = member.get('title')
    castlist.update({actor: character})

  synopsis = soup.find('div', class_='review body-text -prose -hero prettify')
  tagline = synopsis.find('h4').text
  summary = synopsis.find('p').text

  # rating
  SUBURL = f'https://letterboxd.com/{username}/film/{link}/activity'
  subpage = requests.get(SUBURL)
  subsoup = BeautifulSoup(subpage.content, 'html.parser')

  ratingstars = subsoup.find('div', class_='activity-table').find('p', class_='activity-summary').find('span', class_='rating').text.strip()
  rating = len(ratingstars)
  if ratingstars[-1] == '½':
    rating -= 0.5
  
  # print(film, title, year, directorlist, runtime, genrelist, castlist, tagline, summary, rating)
  data = {'link': link, 'title': title, 'year': year, 'directorlist': directorlist, 'runtime': runtime, 'genrelist': genrelist, 
          'castlist': castlist, 'tagline': tagline, 'summary': summary, 'rating': rating, 'ratingstars': ratingstars}
  df = pd.DataFrame([data])

  return df

# scrape data from films
links = ['good-will-hunting', 'john-wick']

# one json file per film
import os

for link in links:
  df = scrape_film(link)

  directory = './src/content/film'
  if not os.path.exists(directory):
    os.makedirs(directory)

  filename = link + '.json'
  path = directory + '/' + filename

  df.to_json(path, orient='records', indent=4)
  del df


# # combine all films into one dataframe -> one json file
# df = pd.DataFrame(columns=['link', 'title', 'year', 'directorlist', 'runtime', 'genrelist', 'castlist', 'tagline', 'summary', 'rating'])

# for link in links:
#   row = scrape_film(link)
#   df = pd.concat([df, row], ignore_index=True)

# df.to_json('./data.json', orient='records', indent=4)
