# Generated by Django 4.2.10 on 2024-03-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='s_phone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]