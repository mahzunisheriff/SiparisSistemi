from django.db import models
from datetime import datetime
from apps.urun.models import Urun
from apps.siparis.models import Siparis

# Create your models here.

class UrunSiparis(models.Model):

    class Meta:
        db_table='urun_siparis'

    id = models.AutoField(primary_key=True)
    adet = models.IntegerField(null=False, default=0)
    urun = models.ForeignKey(Urun, on_delete=models.DO_NOTHING)
    siparis = models.ForeignKey(Siparis, on_delete=models.DO_NOTHING)
    fiyat = models.FloatField(null=False, default=0)

    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    is_deleted = models.BooleanField(default=False)