from django.db import models
from datetime import datetime
from apps.musteri.models import Musteri

# Create your models here.


class Adres(models.Model):

    class Meta:
        db_table='adres'

    id = models.AutoField(primary_key=True)
    sehir = models.CharField(max_length=50, null=False)
    ilce = models.CharField(max_length=50, null=False)
    aciklama = models.CharField(max_length=500, null=False)
    musteri = models.ForeignKey(Musteri, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    is_deleted = models.BooleanField(default=False)