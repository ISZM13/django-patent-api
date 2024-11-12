import csv
from .models import Patent
    
with open('....dataset/cleaned_dataset.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Patent.objects.create(
            patent_id=row['patent_id'],
            country_code=row['country_code'],
            title=row['title'],
            assigne=row['assigne'],
            author=row['author'],
            priority_date=row['priority_date'],
            creation_date=row['creation_date'],
            publ_date=row['publ_date'],
            grant_date=row['grant_date'],
            result_link=row['result_link'],
            fig_link=row['fig_link']
        )
