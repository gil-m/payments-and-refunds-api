# -*- coding: utf-8 -*-
from .models import Payment, CreditCardInformation, MbwayInformation


class PaymentSerializer():
    def __init__(self, obj):
        self.payment_id = obj.get('payment_id')
        self.created_at = obj.get('created_at')
        self.status = obj.get('status')
        self.amount = obj.get('amount')
        self.payment_method = obj.get('payment_method')
        self.settled_at = obj.get('settled_at')
        self.settled_amount = obj.get('settled_amount')
        self.additional_params = obj.get('additional_params')

    def to_payment_model(self):
        return Payment(**self)

    def get_additional_param(self):
        if self.payment_method == 'credit_card' and self.additional_params:
            return CreditCardInformation(**self.additional_params)
        elif self.payment_method == 'mbway' and self.additional_params:
            return MbwayInformation(**self.additional_params)

        return None

    def update_payment(self, payment):
        payment.amount = self.amount
        payment.payment_method = self.payment_method
        additional = self.get_additional_param()
        additional.payment_id = payment.payment_id
        payment.additional_params = additional

        if not payment.settled_at and not payment.settled_amount:
            payment.settled_at = self.settled_at
            payment.settled_amount = self.settled_amount
            payment.status = 'settled'

        return payment

