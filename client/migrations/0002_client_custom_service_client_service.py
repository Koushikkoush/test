# Generated by Django 5.1.6 on 2025-03-04 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='custom_service',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='service',
            field=models.CharField(choices=[('Web', 'Web'), ('App', 'App'), ('Web+App', 'Web + App'), ('Other', 'Other')], default='Web', max_length=50),
        ),
    ]
