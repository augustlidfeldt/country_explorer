# Generated by Django 4.0.4 on 2022-06-01 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population', models.CharField(max_length=80)),
                ('avg_age', models.IntegerField()),
            ],
        ),
    ]