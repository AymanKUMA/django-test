# Generated by Django 4.2.2 on 2023-06-25 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_user_role_user_is_student_user_is_teacher"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="is_student",),
        migrations.RemoveField(model_name="user", name="is_teacher",),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("CLIENT", "Client"),
                    ("SELLER", "Seller"),
                ],
                default="SOME STRING",
                max_length=50,
            ),
        ),
    ]
