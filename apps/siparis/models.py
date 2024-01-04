from django.db import models
from datetime import datetime
from apps.musteri.models import Musteri
from apps.adres.models import Adres

# Create your models here.

class Siparis(models.Model):

    class Meta:
        db_table='siparis'

    id = models.AutoField(primary_key=True)
    musteri = models.ForeignKey(Musteri, on_delete=models.DO_NOTHING)
    adres = models.ForeignKey(Adres, on_delete=models.DO_NOTHING)
    toplam_fiyat = models.FloatField(null=False)

    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    is_deleted = models.BooleanField(default=False)