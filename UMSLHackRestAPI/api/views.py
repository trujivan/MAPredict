# REST
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
# Django
from django.shortcuts import render
from django.conf import settings
from .models import  MLRequest
from .serializeres import MLRequestSerializer
from .utils import get_ml_predictions
# standard
import os
import json


@api_view(http_method_names=['GET'])
def get_dummy_data(request):

    year = request.GET.get('year')

    path = os.path.join(settings.BASE_DIR, 'MapRedict/static/MOCK_DATA2.json')
    with open(path) as json_file:
        data = json.load(json_file)
        if year is not None:
            data = [elem for elem in data if elem['year'].split('/')[-1] == year]
        #data = dict(filter(lambda elem: elem[0]['year'] == year, data[0].items()))
        return Response({"message": "Here is a dummy data, guys!", 'year': year, "data": data})


@api_view(http_method_names=['POST'])
def get_prediction(request):
    year = request.data.get('year')
    print(request.POST)
    return Response({'year': year, 'data': {'state': 'MO', 'color_indicator': 5, 'pollution': 8.5}})


class PredictionView(ListCreateAPIView):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

    def post(self, request, *args, **kwargs):
        result = self.create(request)
        print(result.data)
        return Response(result.data)


def main_view(request):
    return render(request, 'main/index.html', context={})
