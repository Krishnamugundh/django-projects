# Generated by Django 4.2.5 on 2023-09-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_kare', '0002_pat_desc_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pat_desc',
            name='desc',
            field=models.TextField(default='Please enter some text', max_length=100),
        ),
    ]
