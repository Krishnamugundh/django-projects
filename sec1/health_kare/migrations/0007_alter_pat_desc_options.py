# Generated by Django 4.2.5 on 2023-10-01 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_kare', '0006_alter_pat_desc_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pat_desc',
            options={'ordering': ['updated', 'pat_id']},
        ),
    ]