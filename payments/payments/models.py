# -*- coding: utf-8 -*-
from json import JSONEncoder
from random import choices
from string import ascii_letters, digits

from django.db import models

from .choices import PAYMENT_METHOD_CHOICES, PAYMENT_STATUS_CHOICES


class Payment(models.Model):
    payment_id = models.CharField(primary_key=True,
                                  max_length=200)
    amount = models.FloatField(null=False)
    payment_method = models.CharField(null=False,
                                      max_length=50,
                                      choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(null=False,
                                      auto_now_add=True)
    status = models.CharField(null=False,
                              max_length=20,
                              choices=PAYMENT_STATUS_CHOICES,
                              default='success')
    settled_at = models.DateTimeField(null=True)
    settled_amount = models.FloatField(null=True)

    def __init__(self, *args, **kwargs):
        super(Payment, self).__init__(*args, **kwargs)
        if not self.payment_id:
            random_chars = choices(ascii_letters + digits, k=200)
            self.payment_id = ''.join(random_chars)


class CreditCardInformation(models.Model):
    payment = models.OneToOneField(Payment,
                                   primary_key=True,
                                   related_name='credit_card_params',
                                   on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    method = models.CharField(null=False,
                              max_length=50,
                              choices=PAYMENT_METHOD_CHOICES)
    number = models.CharField(null=False,
                              max_length=16)
    name = models.CharField(null=False,
                            max_length=19)
    expiration_month = models.CharField(null=False,
                                        max_length=2)
    expiration_year = models.CharField(null=False,
                                       max_length=4)
    cvv = models.CharField(null=False,
                           max_length=3)


class MbwayInformation(models.Model):
    payment = models.OneToOneField(Payment,
                                   primary_key=True,
                                   related_name='mbway_params',
                                   on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    method = models.CharField(null=False,
                              max_length=50,
                              choices=PAYMENT_METHOD_CHOICES)
    phone_number = models.CharField(null=False,
                                    max_length=9)

class AdditionalParamEncoder():
    pass