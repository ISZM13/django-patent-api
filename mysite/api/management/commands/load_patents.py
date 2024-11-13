from django.core.management.base import BaseCommand
import pandas as pd
from api.models import Patent
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Loads patents into the database'

    def handle(self, *args, **kwargs):
        # Load the cleaned CSV
        df = pd.read_csv('cleaned_dataset.csv')

        # Specify the maximum lengths based on model constraints
        max_lengths = {
            'patent_id': 16,
            'country_code': 2,
            'title': 1000,
            'assignee': 100,
            'author': 100,
            'result_link': 2000,
            'fig_link': 2000
        }

        def is_valid_row(row):
            for field, max_len in max_lengths.items():
                if len(str(row[field])) > max_len:
                    return False
            return True

        # Filter the DataFrame to include only valid rows
        valid_rows = df[df.apply(is_valid_row, axis=1)]

        # Prepare list of Patents to bulk create
        patents_to_create = []
        for _, row in valid_rows.iterrows():
            try:
                patent = Patent(
                    patent_id=row['patent_id'],
                    country_code=row['country_code'],
                    title=row['title'],
                    assigne=row['assignee'],  
                    author=row['author'],
                    priority_date=row['priority_date'],
                    creation_date=row['creation_date'],
                    publ_date=row['publ_date'],
                    grant_date=row['grant_date'],
                    result_link=row['result_link'],
                    fig_link=row['fig_link']
                )
                patents_to_create.append(patent)
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(f"Skipping row due to integrity error: {e}"))

        # Bulk create Patents
        try:
            Patent.objects.bulk_create(patents_to_create)
            self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(patents_to_create)} records into the database."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to bulk create Patents: {e}"))
