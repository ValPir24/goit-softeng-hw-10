# Generated by Django 5.0.6 on 2024-05-25 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotesapp", "0002_rename_bio_author_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
