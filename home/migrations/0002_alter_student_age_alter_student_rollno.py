# Generated by Django 5.0.3 on 2024-03-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollNo',
            field=models.IntegerField(default=111111),
        ),
    ]