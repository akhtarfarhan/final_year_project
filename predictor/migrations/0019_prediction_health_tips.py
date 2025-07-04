# Generated by Django 5.1.6 on 2025-04-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("predictor", "0018_remove_prediction_probability_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="prediction",
            name="health_tips",
            field=models.TextField(
                blank=True,
                help_text="Personalized health tips based on prediction results (JSON string)",
                null=True,
            ),
        ),
    ]
