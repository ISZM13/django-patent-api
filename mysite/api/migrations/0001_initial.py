# Generated by Django 5.1.3 on 2024-11-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_id', models.CharField(max_length=16)),
                ('country_code', models.CharField(max_length=2)),
                ('title', models.TextField()),
                ('assigne', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('priority_date', models.DateField(auto_now_add=True)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('publ_date', models.DateField(auto_now_add=True)),
                ('grant_date', models.DateField()),
                ('result_link', models.URLField()),
                ('fig_link', models.URLField()),
            ],
        ),
    ]
