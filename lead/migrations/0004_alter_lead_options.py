# Generated by Django 4.1.3 on 2022-11-24 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_lead_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'ordering': ('name',)},
        ),
    ]
