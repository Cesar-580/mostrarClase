# Generated by Django 4.2.6 on 2023-10-23 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_auto_20231022_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ips',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_prestador', models.CharField(max_length=250)),
                ('nit', models.CharField(max_length=15)),
                ('naturaleza', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
