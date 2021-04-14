# -*- coding: utf-8 -*-
from json import loads as json_loads

from django.forms.models import model_to_dict
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import CreditCardInformation, MbwayInformation, Payment
from .serializers import PaymentSerializer


@csrf_exempt
@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def view_handler(request, id=None):
    if request.method == 'GET':
        return get(request, id)
    elif request.method == 'POST':
        return post(request)
    elif request.method == 'PUT':
        return put(request, id)
    elif request.method == 'DELETE':
        return delete(request, id)


def get(request, id=None):
    if id:
        payment = _get_by_id(request, id)

        if not payment:
            return JsonResponse({})

        result = model_to_dict(payment)
        if payment.payment_method == 'credit_card':
            result['additional_params'] = model_to_dict(
                payment.credit_card_params)
        elif payment.payment_method == 'mbway':
            result['additional_params'] = model_to_dict(payment.mbway_params)

    else:
        filters = {}
        if 'payment_id' in request.GET:
            filters['payment_id'] = request.GET['payment_id']
        if 'payment_method' in request.GET:
            filters['payment_method'] = request.GET['payment_method']
        if 'status' in request.GET:
            filters['status'] = request.GET['status']
        if 'amount_gte' in request.GET:
            filters['amount__gte'] = request.GET['amount_gte']
        if 'amount_lte' in request.GET:
            filters['amount__lte'] = request.GET['amount_lte']
        if 'created_at_gte' in request.GET:
            filters['created_at__gte'] = request.GET['created_at_gte']
        if 'created_at_lte' in request.GET:
            filters['created_at__lte'] = request.GET['created_at_lte']
        if 'settled_at_gte' in request.GET:
            filters['settled_at__gte'] = request.GET['settled_at_gte']
        if 'settled_at_lte' in request.GET:
            filters['settled_at__lte'] = request.GET['settled_at_lte']

        result = [model_to_dict(item)
                  for item in Payment.objects.filter(**filters)]

    return JsonResponse(result, safe=False)


def post(request):
    byte_data = request.read()
    data = json_loads(byte_data)
    serializer = PaymentSerializer(data)
    new_payment = serializer.to_payment_model()
    new_payment.save()

    info = serializer.get_additional_param()

    if info:
        info.payment_id = payment.payment_id
        try:
            info.save()
        except:
            payment.status = 'error'
            payment.save()

    result = model_to_dict(new_payment)
    return JsonResponse(result)


def put(request, id):
    payment = _get_by_id(request, id)

    if not payment:
        return JsonResponse({})

    byte_data = request.read()
    data = json_loads(byte_data)
    serializer = PaymentSerializer(data)
    payment = serializer.update_payment(payment)
    payment.save()
    info = serializer.get_additional_param()

    if info:
        info.payment_id = payment.payment_id
        try:
            info.save()
        except:
            payment.status = 'error'
            payment.save()

    result = model_to_dict(payment)
    return JsonResponse(result)


def delete(request, id):
    payment = _get_by_id(request, id)

    if not payment:
        return JsonResponse({})

    result = model_to_dict(payment)
    payment.delete()
    return JsonResponse(result)


def _get_by_id(request, id):
    try:
        payment = Payment.objects.select_related('credit_card_params',
                                                 'mbway_params').get(pk=id)
        return payment

    except Payment.DoesNotExist:
        return None

