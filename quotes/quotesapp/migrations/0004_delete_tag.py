# Generated by Django 5.0.6 on 2024-05-25 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("quotesapp", "0003_tag"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Tag",
        ),
    ]