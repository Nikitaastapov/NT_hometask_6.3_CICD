# Generated by Django 4.1.7 on 2023-07-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("measurement", "0005_auto_20230313_0915"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="measurement",
            name="image",
        ),
        migrations.AlterField(
            model_name="measurement",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="sensor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
