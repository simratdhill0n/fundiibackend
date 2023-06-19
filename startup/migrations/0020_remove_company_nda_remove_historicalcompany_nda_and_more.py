# Generated by Django 4.2.1 on 2023-06-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0019_company_percentage_company_valuation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='nda',
        ),
        migrations.RemoveField(
            model_name='historicalcompany',
            name='nda',
        ),
        migrations.AddField(
            model_name='company',
            name='signed_nda',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='company',
            name='unsigned_nda',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='historicalcompany',
            name='signed_nda',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalcompany',
            name='unsigned_nda',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
