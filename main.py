from pandas_util import count_complexities, count_chords
from scrapper import Scrapper


if __name__ == '__main__':

    scrapper = Scrapper("https://www.cifraclub.com.br/caetano-veloso/", "songs_caetano.csv")
    df = scrapper.generate_df_songs()
    #count_chords(df)
    count_complexities(df)
