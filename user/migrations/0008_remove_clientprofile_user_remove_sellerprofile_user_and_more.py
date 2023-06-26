# Generated by Django 4.2.2 on 2023-06-26 02:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_alter_event_created_by_alter_organization_created_by"),
        ("user", "0007_clientprofile_sellerprofile_client_seller"),
    ]

    operations = [
        migrations.RemoveField(model_name="clientprofile", name="user",),
        migrations.RemoveField(model_name="sellerprofile", name="user",),
        migrations.DeleteModel(name="Client",),
        migrations.DeleteModel(name="Seller",),
        migrations.RemoveField(model_name="user", name="role",),
        migrations.AddField(
            model_name="user",
            name="is_client",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="is_seller",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
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
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user", name="last_name", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.CreateModel(
            name="client",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="client",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="seller",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="seller",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "belongs_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_reff",
                        to="shop.organization",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="ClientProfile",),
        migrations.DeleteModel(name="SellerProfile",),
    ]
