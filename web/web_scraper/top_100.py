import requests
from bs4 import BeautifulSoup
import pandas as pd

NAME_OF_SONG = 'Beautiful Things'

# URL of the Billboard Hot 100 chart
url = "https://www.billboard.com/charts/hot-100/"

# Send a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    chart_number = []
    song_names = []

    for entry in soup.find_all('div', class_="o-chart-results-list-row-container"):
        song_number = entry.find('span').text
        chart_number.append(song_number.strip())
        song = entry.find('h3', id='title-of-a-story').text
        song_names.append(song.strip())

if NAME_OF_SONG in song_names:
    index_of_song = song_names.index(NAME_OF_SONG)
    print(f"The song: {NAME_OF_SONG} is number {chart_number[index_of_song]} on the charts...")
else:
    print("The song is not on the charts....")