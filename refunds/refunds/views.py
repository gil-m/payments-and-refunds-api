# -*- coding: utf-8 -*-
from json import loads as json_loads

from django.conf import settings
from django.forms.models import model_to_dict
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Refund
from .http_client import HttpClient


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def view_handler(request, id=None):
    if request.method == 'GET':
        return get(request, id)
    elif request.method == 'POST':
        return post(request)


def get(request, id=None):
    if id:
        refund = _get_by_id(request, id)

        if not refund:
            return JsonResponse({})

        result = model_to_dict(refund)
    else:
        filters = {}
        if 'payment_id' in request.GET:
            filters['payment_id'] = request.GET['payment_id']
        if 'refund_id' in request.GET:
            filters['refund_id'] = request.GET['refund_id']
        result = [model_to_dict(item)
                  for item in Refund.objects.filter(**filters)]

    return JsonResponse(result, safe=False)


def post(request):
    byte_data = request.read()
    data = json_loads(byte_data)
    new_refund = Refund()
    new_refund.payment_id = data.get('payment_id')
    new_refund.amount = data.get('amount')

    client = HttpClient(settings.PAYMENTS_URL)
    payment = client.get(f'api/payments/{new_refund.payment_id}')

    if not payment:
        return JsonResponse({})

    refunds = Refund.objects.filter(
        payment_id=new_refund.payment_id
    ).values('amount')
    refund_sum = 0

    if refunds:
        refund_sum = sum([x['amount'] for x in refunds])

    total_refund = refund_sum + new_refund.amount

    if payment['amount'] >= total_refund:
        new_refund.save()
        result = model_to_dict(new_refund)
        return JsonResponse(result)
    else:
        msg = f'The refunds sum ({total_refund}) cannot exceed '\
            + f'the payment amount ({payment["amount"]})'
        return JsonResponse({'errors': msg})


def _get_by_id(request, id):
    try:
        payment = Refund.objects.get(pk=id)
        return payment

    except Refund.DoesNotExist:
        return None
