from django.db import models
from datetime import datetime

# Create your models here.

class Urun(models.Model):

    class Meta:
        db_table='urun'

    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=255, null=False)
    aciklama = models.CharField(max_length=500, null=False)
    fiyat = models.FloatField(null=False, default=0)

    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    is_deleted = models.BooleanField(default=False)