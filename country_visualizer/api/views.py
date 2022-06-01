from django.shortcuts import render
from urllib import request
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WorldFertility

# Create your views here.


class GetFertility(APIView):
    # serializer class serializer_class = fertilitySerializer
    lookup_url_kwarg = 'country'

    def get(self, request, format=None):
        country = request.GET.get(self.lookup_url_kwarg)
        if country != None:
            fertility = WorldFertility.objects.filter(country=country)
            if len(fertility) > 0:
                return str(fertility)
                # data = RoomSerializer(room[0]).data
