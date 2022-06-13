from django.shortcuts import render
from .models import Mahasiswa
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def read(request, npm):
    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        return Response({'status': 'OK', 'npm': mahasiswa.npm, 'nama': mahasiswa.nama}, status=status.HTTP_200_OK)

    except Mahasiswa.DoesNotExist:
        return Response({'message': 'Mahasiswa not found!'}, status=status.HTTP_404_NOT_FOUND)
