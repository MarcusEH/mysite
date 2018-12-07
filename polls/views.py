from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    some_data_to_dump = {
       'some_var_1': 'foo',
       'some_var_2': 'bar',
    }
    data = json.dumps(some_data_to_dump)
    return HttpResponse(data, content_type='application/json')

def show(request):
    some_data_to_dump = {
       'some_var_1': 'bar',
       'some_var_2': 'foo',
    }
    data = json.dumps(some_data_to_dump)
    return HttpResponse(data, content_type='application/json')