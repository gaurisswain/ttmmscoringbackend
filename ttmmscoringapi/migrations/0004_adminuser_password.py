# Generated by Django 4.1.4 on 2023-01-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttmmscoringapi', '0003_alter_funding_funding_alter_startup_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='password',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
