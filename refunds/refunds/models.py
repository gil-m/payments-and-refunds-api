# -*- coding: utf-8 -*-
from random import choices
from string import ascii_letters, digits

from django.db import models


class Refund(models.Model):
    refund_id = models.CharField(primary_key=True,
                                 max_length=200)
    payment_id = models.CharField(null=False,
                                  max_length=200)
    created_at = models.DateTimeField(null=False,
                                      auto_now_add=True)
    amount = models.FloatField(null=False)

    def __init__(self, *args, **kwargs):
        super(Refund, self).__init__(*args, **kwargs)
        if not self.refund_id:
            random_chars = choices(ascii_letters + digits, k=200)
            self.refund_id = ''.join(random_chars)
