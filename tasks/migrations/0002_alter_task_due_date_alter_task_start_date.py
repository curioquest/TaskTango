# Generated by Django 4.2 on 2023-04-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateField(),
        ),
    ]
