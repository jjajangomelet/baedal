# Generated by Django 2.1.8 on 2019-05-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.IntegerField(choices=[(0, '기숙사'), (1, '궁동'), (2, '죽동')], default=0),
        ),
    ]
