# Generated by Django 3.2.25 on 2024-09-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0003_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatct',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
