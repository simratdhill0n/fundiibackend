from django.db import migrations

def create_industries(apps, schema_editor):
    Industry = apps.get_model('startup', 'Industry')

    industries = [
        'Agriculture',
        'Apparel & Fashion',
        'Automotive',
        'Banking',
        'Biotechnology',
        'Chemicals',
        'Communications',
        'Construction',
        'Consulting',
        'Consumer Goods',
        'Cosmetics',
        'Defense',
        'Education',
        'Electronics',
        'Energy',
        'Entertainment',
        'Environmental',
        'Finance',
        'Food & Beverage',
        'Health & Wellness',
        'Healthcare',
        'Hospitality',
        'Information Technology',
        'Insurance',
        'Manufacturing',
        'Media',
        'Nonprofit',
        'Pharmaceuticals',
        'Real Estate',
        'Retail',
        'Sports',
        'Technology',
        'Telecommunications',
        'Transportation',
        'Utilities'
    ]

    for element in industries:

        Industry(name=element).save()


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0002_initial')
    ]

    operations = [
        migrations.RunPython(create_industries)
    ]

