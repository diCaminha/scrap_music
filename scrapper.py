import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

from song import Song

class Scrapper:
    def __init__(self, url, nome_arquivo):
        self.url = url
        self.nome_arquivo = nome_arquivo

    def generate_df_songs(self):
        if not os.path.exists(self.nome_arquivo):
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, 'html.parser')

            li_songs = soup.find_all(class_='list-links art_musics alf all artistMusics--allSongs')[0]

            songs = []
            for song in li_songs:
                try:
                    href = song.find("a")["href"]
                    link = f"https://www.cifraclub.com.br/{href}"
                    song_html = BeautifulSoup(requests.get(link).content, 'html.parser')

                    title = song_html.find(class_="t1").text

                    class_pre_lyric = song_html.find("pre")
                    if class_pre_lyric:
                        lyric = class_pre_lyric.text

                        chords = []

                        b_tag_chords = class_pre_lyric.find_all("b")
                        for b_tag in b_tag_chords:
                            chords.append(b_tag.text)
                        if len(chords):
                            chords = set(chords)
                        else:
                            chords = None

                    else:
                        lyric = None
                        chords = None

                    visualizacoes = int(song_html.find(class_="exib").find("b").text.replace('.', ''))

                    menu_versoes = song_html.find_all(class_="vers-r js-version")
                    if menu_versoes:
                        difficulty = menu_versoes[0].find_all("span")[3].text
                    else:
                        continue

                    songs.append(Song(title, chords, lyric, visualizacoes, difficulty))
                except Exception as e:
                    print(e)
                    print(title)

            data = [vars(s) for s in songs]

            df = pd.DataFrame(data)
            df.to_csv(self.nome_arquivo)

        else:
            df = pd.read_csv(self.nome_arquivo)

        return df