# Generated by Django 4.2 on 2023-04-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translation", "0002_rename_text_article_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="url",
            field=models.URLField(unique=True),
        ),
    ]
