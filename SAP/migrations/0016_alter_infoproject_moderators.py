# Generated by Django 4.0.2 on 2022-03-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SAP', '0015_projectuabs_pavadinimasproject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoproject',
            name='moderators',
            field=models.TextField(default=''),
        ),
    ]
