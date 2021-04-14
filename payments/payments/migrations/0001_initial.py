# Generated by Django 3.1.7 on 2021-04-04 20:41

from django.db import migrations, models
import payments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCardAdditionalParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('method', models.CharField(choices=[('credit_card', 'credit_card'), ('mbway', 'mbway')], max_length=50)),
                ('number', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=19)),
                ('expiration_month', models.CharField(max_length=2)),
                ('expiration_year', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MbwayAdditionalParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('method', models.CharField(choices=[('credit_card', 'credit_card'), ('mbway', 'mbway')], max_length=50)),
                ('phone_number', models.CharField(max_length=9)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('payment_method', models.CharField(choices=[('credit_card', 'credit_card'), ('mbway', 'mbway')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('success', 'success'), ('error', 'error'), ('settled', 'settled')], max_length=20)),
                ('settled_at', models.DateTimeField()),
                ('settled_amount', models.FloatField()),
                ('additional_params', models.JSONField(encoder=payments.models.AdditionalParamEncoder)),
            ],
        ),
    ]