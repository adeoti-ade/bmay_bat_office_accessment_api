from django.db import models
from rest_framework import viewsets
from .serializers import FileSerializer, WorkSerializer
from .models import File, Work


class FileViewset(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    
