# Generated by Django 4.0.4 on 2022-06-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='', max_length=50)),
                ('npm', models.CharField(default=0, max_length=10)),
            ],
        ),
    ]
