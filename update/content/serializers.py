from .models import Mahasiswa
from rest_framework import serializers


class MahasiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = '__all__'
