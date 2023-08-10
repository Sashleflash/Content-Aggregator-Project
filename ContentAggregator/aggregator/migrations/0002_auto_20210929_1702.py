# Generated by Django 3.2.7 on 2021-09-29 22:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='new',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='new',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='website',
            name='rss_item_node',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='website',
            name='rss_parent_node',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='new',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aggregator.website'),
        ),
    ]
