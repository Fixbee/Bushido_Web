# Generated by Django 3.0.7 on 2020-06-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_newregistration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newregistration',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
