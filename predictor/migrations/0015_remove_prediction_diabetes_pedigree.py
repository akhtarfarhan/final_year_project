# Generated by Django 5.1.6 on 2025-04-12 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("predictor", "0014_prediction_diabetes_pedigree"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prediction",
            name="diabetes_pedigree",
        ),
    ]
