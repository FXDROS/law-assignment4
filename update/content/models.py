from django.db import models

# Create your models here.


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50, default="")
    npm = models.CharField(max_length=10, default=0)
