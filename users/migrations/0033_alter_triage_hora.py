# Generated by Django 3.2.22 on 2023-10-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_triage_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triage',
            name='hora',
            field=models.TimeField(auto_now_add=True),
        ),
    ]