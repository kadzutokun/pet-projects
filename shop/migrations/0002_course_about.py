# Generated by Django 4.2.6 on 2023-10-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.CharField(default='null', max_length=255),
        ),
    ]
