# Generated by Django 3.1.4 on 2021-03-28 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='billuser',
            name='Name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
