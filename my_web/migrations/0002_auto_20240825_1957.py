# Generated by Django 3.2.25 on 2024-08-25 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contatct',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='contatct',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]