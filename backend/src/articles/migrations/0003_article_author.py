# Generated by Django 3.1.3 on 2020-11-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Nitin', max_length=100),
        ),
    ]
