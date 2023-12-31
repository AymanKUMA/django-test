# Generated by Django 4.2.2 on 2023-06-26 02:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_remove_clientprofile_user_remove_sellerprofile_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="phone_number",),
        migrations.AddField(
            model_name="client",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="seller",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
    ]
