from django.shortcuts import render
from .models import Drug
from .serializers import DrugSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class DrugViewSet(viewsets.ViewSet):
    def GetAllDrugs(self,request):
        dru=Drug.objects.all()
        seri=DrugSerializer(dru,many=True)
        return Response(seri.data)
    def GetDrugById(self,request,id):
        dru=Drug.objects.get(Did=id)
        seri=DrugSerializer(dru)
        return Response(seri.data)
    def createdrug(self,request):
        seri=DrugSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response("Data is Added..")
