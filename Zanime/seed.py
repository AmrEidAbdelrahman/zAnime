from django_seed import Seed

from chapter.models import Chapter
from manga.models import ModelGenre, Manga, Genre

# docs: https://github.com/Brobin/django-seed

seeder = Seed.seeder()
seeder.add_entity(Genre, 5, {
    'name': lambda x: 'Genre %s' % x,
})
seeder.add_entity(Manga, 5)
seeder.add_entity(Chapter, 5, {
    'manga': lambda x: seeder.faker.random_int(min=1, max=5),
})

inserted_pks = seeder.execute()
