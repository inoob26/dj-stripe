# Generated by Django 3.1.2 on 2020-11-15 22:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0013_auto_20201115_1828"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apikey",
            name="description",
        ),
        migrations.RemoveField(
            model_name="apikey",
            name="metadata",
        ),
        migrations.AlterField(
            model_name="apikey",
            name="livemode",
            field=models.BooleanField(
                default=False,
                help_text="Whether the key is valid for live or test mode. This is automatically detected when saved.",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="apikey",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="An optional name to identify the key.",
                max_length=100,
                verbose_name="Key name",
            ),
        ),
        migrations.AlterField(
            model_name="apikey",
            name="secret",
            field=models.CharField(
                help_text="The value of the key.",
                max_length=128,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^(pk|sk|rk)_(test|live)_([a-zA-Z0-9]{24,99})"
                    )
                ],
            ),
        ),
    ]
