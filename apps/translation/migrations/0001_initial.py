# Generated by Django 4.2 on 2023-05-02 18:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Dictionary",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("word", models.CharField(max_length=255)),
                ("translation", models.CharField(max_length=255)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("user", models.ManyToManyField(related_name="words", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "verbose_name_plural": "Dictionary",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("url", models.URLField(unique=True)),
                ("author", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("data", models.TextField()),
                ("translation", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("user", models.ManyToManyField(related_name="articles", to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
