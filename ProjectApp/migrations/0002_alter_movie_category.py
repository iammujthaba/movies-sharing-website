# Generated by Django 5.0.4 on 2024-05-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=350),
        ),
    ]
