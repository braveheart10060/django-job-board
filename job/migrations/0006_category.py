# Generated by Django 4.1.2 on 2022-10-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0005_job_vacancy_job_experiance_job_salary"),
    ]

    operations = [
        migrations.CreateModel(
            name="category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
            ],
        ),
    ]
