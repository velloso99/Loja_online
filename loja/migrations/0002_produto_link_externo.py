# Generated by Django 5.2 on 2025-04-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='link_externo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
