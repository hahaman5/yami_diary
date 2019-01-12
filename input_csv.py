import os,django,csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yami_diary.settings")
django.setup()

from post.models import Idea,Division
from django.db import models

with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            divi=Division.objects.get(division=row[1])
            "asdf"
        except Division.DoesNotExist:
            "add a new division"
            divi=Division(division=row[1])
            divi.save()

        created = Idea(
                subject=row[0],
                division=divi,
                )
        if len(row) >= 3:
            created.pub_date = row[2]

        created.save()
