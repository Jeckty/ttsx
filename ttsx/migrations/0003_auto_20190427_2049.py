# Generated by Django 2.1 on 2019-04-27 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx', '0002_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='productid',
            field=models.CharField(max_length=30),
        ),
    ]