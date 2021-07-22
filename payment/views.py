from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
import json
import requests

verification_url = "https://khalti.com/api/v2/payment/verify/"


def payment_process(request):
    return render(request, 'payment/process.html')


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def verify_payment(request):
    my_bytes = request.body
    my_json = my_bytes.decode('utf8').replace("'", '"')
    payload = my_json
    headers = {
        "Authorization": "test_secret_key_61fda43d5daf40718e3f5c89904bff58"
    }

    response = requests.post(verification_url, payload, headers = headers)
    return HttpResponse(response)
    # print response , if response status ok, alert payment successful
    # print response , if response status bad, alert payment unsuccessful

    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
