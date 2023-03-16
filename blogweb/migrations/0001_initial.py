# Generated by Django 4.1.7 on 2023-03-09 09:19

import blogweb.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addblogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blogweb.models.getfilename)),
                ('description', models.TextField(max_length=1000)),
                ('related', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
