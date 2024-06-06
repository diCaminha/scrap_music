import requests
from bs4 import BeautifulSoup
import pandas as pd

from song import Song


def extrai_tablaturas(html_tablaturas):
    tablaturas = []
    for tab_html in html_tablaturas:
        tablaturas.append(tab_html.text)
    return tablaturas


if __name__ == '__main__':
    response = requests.get('https://www.cifraclub.com.br/arctic-monkeys/')
    soup = BeautifulSoup(response.content, 'html.parser')

    li_songs = soup.find_all(class_='list-links art_musics all listSongArtist')[0]

    songs = []
    for song in li_songs:
        href = song.find("a")["href"]
        link = f"https://www.cifraclub.com.br/{href}"
        song_html = BeautifulSoup(requests.get(link).content, 'html.parser')

        title = song_html.find(class_="t1").text
        tablaturas = extrai_tablaturas(song_html.find_all(class_='tablatura'))
        lyrics = song_html.find("pre").text
        visualizacoes = int(song_html.find(class_="exib").find("b").text.replace('.', ''))

        songs.append(Song(title, tablaturas, lyrics, visualizacoes))

    data = [vars(s) for s in songs]

    df = pd.DataFrame(data)

    print(df["tablatura"])
