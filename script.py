import pandas as pd
from manga.models import Manga


all_manga = pd.read_csv('manga_data.csv')

for i in range(0, 20):
    manga = Manga(
        title=all_manga.iloc[i]['Name'],
        description=all_manga.iloc[i]['Description'],

    )
    manga.save()


