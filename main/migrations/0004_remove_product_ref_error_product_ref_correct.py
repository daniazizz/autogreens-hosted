# Generated by Django 5.0.6 on 2025-01-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_ref_error_user_gy_reduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ref_error',
        ),
        migrations.AddField(
            model_name='product',
            name='ref_correct',
            field=models.BooleanField(default=True),
        ),
    ]
