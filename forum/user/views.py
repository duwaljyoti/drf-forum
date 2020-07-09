from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view


# @api_view(['GET'])
def test_view(self):
    return HttpResponse('something')
