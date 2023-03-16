# Generated by Django 4.1.7 on 2023-03-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('basic_idea', models.TextField(max_length=500)),
                ('project_type', models.CharField(choices=[('app', 'Mobile App'), ('web', 'Web App'), ('other', 'Other')], max_length=5)),
            ],
        ),
    ]