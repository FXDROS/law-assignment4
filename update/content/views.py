from django.shortcuts import render
from .models import Mahasiswa
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MahasiswaSerializer

# Create your views here.


@api_view(['POST'])
def update(request):
    data = {**request.data}
    npm = data['npm']
    nama = data['nama']

    try:
        mahasiswa = Mahasiswa.objects.get(npm=npm)
        serializer = MahasiswaSerializer(mahasiswa, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

    except Mahasiswa.DoesNotExist:
        return Response({'message': 'Mahasiswa not found!'}, status=status.HTTP_404_NOT_FOUND)
