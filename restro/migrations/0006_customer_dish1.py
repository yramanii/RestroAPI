# Generated by Django 3.2.6 on 2021-08-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restro', '0005_delete_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Dish1',
            field=models.ManyToManyField(to='restro.Punjabi'),
        ),
    ]
