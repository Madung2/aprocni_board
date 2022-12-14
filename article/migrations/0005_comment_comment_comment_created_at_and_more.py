# Generated by Django 4.1.1 on 2022-10-04 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0004_article_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="comment",
            field=models.CharField(default="", max_length=200, verbose_name="내용"),
        ),
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="생성 날짜",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
        ),
    ]
