# Generated by Django 2.1 on 2019-04-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx', '0003_auto_20190427_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='longName',
            field=models.CharField(max_length=500),
        ),
    ]