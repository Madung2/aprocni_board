# Generated by Django 4.1.1 on 2022-10-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_article_board_alter_article_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="uid",
            field=models.CharField(default=0, max_length=1, unique=True),
        ),
    ]
