# Generated by Django 4.1.4 on 2023-01-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttmmscoringapi', '0004_adminuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='current',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='done',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
