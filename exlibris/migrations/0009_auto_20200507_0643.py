# Generated by Django 3.0.4 on 2020-05-07 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exlibris', '0008_auto_20200507_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together={('title', 'year', 'author')},
        ),
    ]