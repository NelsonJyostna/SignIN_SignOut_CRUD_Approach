# Generated by Django 3.1.7 on 2021-03-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='pune', max_length=20),
            preserve_default=False,
        ),
    ]
