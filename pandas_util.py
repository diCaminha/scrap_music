import pandas as pd


def count_chords(df):
    df['chords'] = df['chords'].apply(lambda x: set() if pd.isna(x) else set(x.strip('{}').split(', ')))
    all_chords = set().union(*df['chords'])
    #print(all_chords)
    print(len(all_chords))


def count_complexities(df):
    print(df["difficulty"].value_counts())