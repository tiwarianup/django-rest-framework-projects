# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-07-02 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_tweet_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweetText',
            field=models.CharField(max_length=140, validators=[tweets.models.validateTweetText]),
        ),
    ]
