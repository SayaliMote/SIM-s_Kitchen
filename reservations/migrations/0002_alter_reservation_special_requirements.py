# Generated by Django 4.1.1 on 2023-03-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='special_requirements',
            field=models.TextField(),
        ),
    ]