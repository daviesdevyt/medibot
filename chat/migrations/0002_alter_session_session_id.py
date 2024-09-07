# Generated by Django 4.2.5 on 2024-09-07 08:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="session_id",
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]