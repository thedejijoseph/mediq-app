# Generated by Django 5.0.1 on 2024-01-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_alter_organization_organisation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contact_phone',
            field=models.CharField(max_length=20),
        ),
    ]