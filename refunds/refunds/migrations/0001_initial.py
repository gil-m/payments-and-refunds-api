# Generated by Django 3.1.7 on 2021-04-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('refund_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('payment_id', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
            ],
        ),
    ]