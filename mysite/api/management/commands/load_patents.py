import csv
from django.core.management.base import BaseCommand
from api.models import Patent
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Load patents data from a CSV file into the Patent model'

    def handle(self, *args, **kwargs):
        file_path = '../dataset/cleaned_dataset.csv' 

        # Open the file with UTF-8 encoding
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Patent.objects.create(
                    patent_id=row['patent_id'],
                    country_code=row['country_code'],
                    title=row['title'],
                    assigne=row['assignee'],
                    author=row['author'],
                    priority_date=parse_datetime(row['priority_date']),
                    creation_date=parse_datetime(row['creation_date']),
                    publ_date=parse_datetime(row['publ_date']),
                    grant_date=parse_datetime(row['grant_date']),
                    result_link=row['result_link'],
                    fig_link=row['fig_link']
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
