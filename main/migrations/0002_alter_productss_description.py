# Generated by Django 4.2.2 on 2023-06-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productss',
            name='description',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
