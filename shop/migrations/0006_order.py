# Generated by Django 4.2.6 on 2023-10-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_course_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=50)),
                ('userfname', models.CharField(max_length=50)),
                ('courseid', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('status', models.CharField(choices=[('Accepted', 'Заказ принят'), ('paid', 'Заказ оплачен'), ('in work', 'Выполняется'), ('comleted', 'Выполнен')], max_length=255)),
            ],
        ),
    ]