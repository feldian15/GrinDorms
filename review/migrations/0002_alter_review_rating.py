# Generated by Django 5.1.6 on 2025-04-04 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Awful'), (2, 'Poor'), (3, 'Okay'), (4, 'Good'), (5, 'Awesome')], default=3),
        ),
    ]
