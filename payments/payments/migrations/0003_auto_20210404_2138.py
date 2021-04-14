# Generated by Django 3.1.7 on 2021-04-04 21:38

from django.db import migrations, models
import payments.models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20210404_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='additional_params',
            field=models.JSONField(encoder=payments.models.AdditionalParamEncoder, null=True),
        ),
    ]
