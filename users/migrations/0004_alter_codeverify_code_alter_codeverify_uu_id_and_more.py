# Generated by Django 5.0.6 on 2024-06-06 13:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_codeverify_code_alter_codeverify_uu_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeverify',
            name='code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='codeverify',
            name='uu_id',
            field=models.UUIDField(default=uuid.UUID('b66ad7b4-6d5e-43ab-a69e-c6e3649a6a87'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='followers',
            name='uu_id',
            field=models.UUIDField(default=uuid.UUID('b66ad7b4-6d5e-43ab-a69e-c6e3649a6a87'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
