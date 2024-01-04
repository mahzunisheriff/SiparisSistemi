from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UrunSiparisSerializer
from .models import UrunSiparis
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UrunSiparisViewSet(ModelViewSet):

    serializer_class = UrunSiparisSerializer
    queryset = UrunSiparis.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):

        try:
            allUrunSiparis = UrunSiparis.objects.all()
            serializer = UrunSiparisSerializer(allUrunSiparis, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):

        try:
            UrunSiparis = UrunSiparis.objects.get(id=pk)
            serializer = UrunSiparisSerializer(UrunSiparis, many=False)
            return Response(serializer.data)
        
        except Exception as e:
            return Response(e,status=status.HTTP_400_BAD_REQUEST)
        
    def create(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)