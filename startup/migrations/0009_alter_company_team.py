# Generated by Django 4.2.1 on 2023-06-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0008_remove_historicalteam_company_remove_team_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='team',
            field=models.ManyToManyField(related_name='team_members', to='startup.team'),
        ),
    ]
