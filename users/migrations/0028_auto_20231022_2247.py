# Generated by Django 3.2.22 on 2023-10-23 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_auto_20231022_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='fecha',
            field=models.DateField(auto_now_add=True, default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='triage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
