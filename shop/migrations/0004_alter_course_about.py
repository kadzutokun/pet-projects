# Generated by Django 4.2.6 on 2023-10-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
