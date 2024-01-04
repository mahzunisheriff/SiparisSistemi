from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from .serializers import SiparisSerializer, UrunSiparisSerializer
from .models import Siparis
from apps.urun.models import Urun

# Create your views here.

class SiparisViewSet(ModelViewSet):

    serializer_class = SiparisSerializer
    queryset = Siparis.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        
        try:
            allSiparis = Siparis.objects.all()
            serializer = SiparisSerializer(allSiparis, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        try:
            Siparis = Siparis.objects.get(id=pk)
            serializer = SiparisSerializer(Siparis, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
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


@api_view(['POST'])
def urun_siparis_olustur(request):

    try:
        # request body nin içinden urun id listesine ulaş.
        urun_detay = request.data.get('urun_detay', [])

        #filter içindeki kodumuzun uzun hali
        # urunler = []
        # for item in urun_detay:
        #     urun = Urun.objects.filter(id=item['id'])
        #     urunler.append(urun)

        #idsi verilen ürünleri veritabanında filtrele.
        urunler = Urun.objects.filter(id__in=[item['id'] for item in urun_detay])

        # eğer gelen id sayısı ile veri tabanında filtrelenen id sayısı aynı değilse hata  dön.
        if len(urunler) != len(urun_detay):
            return Response("Siparişinize eklediğiniz ürünlerin bir kısmı veri tabanında bulunmamaktadır.",
                            status=status.HTTP_404_NOT_FOUND)

        # sipariş kaydı oluşturmak için body oluşturacağız.
        siparis_data = {
            'aciklama':request.data.get('aciklama', ''),
            'toplam_fiyat': request.data.get('toplam_fiyat', 0),
            'adres': request.data.get('adres', None),
            'musteri': request.data.get('musteri', None),
        }

        siparis_serializer = SiparisSerializer(data=siparis_data)

        if siparis_serializer.is_valid():

            siparis = siparis_serializer.save()   

            for detay in urun_detay:
                urun = Urun.objects.get(id=detay['id'])
                urun_siparis_data = {
                    'adet': detay['adet'],
                    'urun' : urun.id, # detay[id]
                    'siparis': siparis.id,
                    'fiyat': urun.fiyat * int(detay['adet'])
                }

                urun_siparis = UrunSiparisSerializer(data=urun_siparis_data)

                if urun_siparis.is_valid():
                    urun_siparis.save()
                    
                else:
                    return Response('Urun sipariş oluşturulurken hata oluştu' + urun_siparis.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response('Sipariş başarıyla oluşturuldu', status=status.HTTP_200_OK)
        else:
            return Response(siparis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        return Response('Siparişiniz başarıyla oluşturuldu', status=status.HTTP_200_OK)
    except Exception as e:

        return Response(e, status= status.HTTP_400_BAD_REQUEST)