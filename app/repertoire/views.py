from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import FileSerializer, WorkSerializer
from .models import File, Work
from .utils import get_source

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


class FileViewset(viewsets.ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["filename"]

    @action(methods=["get"], detail=True, url_path="works")
    def works(self, request, *args, **kwargs):
        file = self.get_object()
        source = get_source(file)
        works_qs = Work.objects.filter(source=source)
        # works_qs = get_list_or_404(Work, source=source)
        work_serializer = WorkSerializer(works_qs, many=True)
        data = {
            "count": works_qs.count(),
            "works": work_serializer.data,
            "file": self.get_serializer(file).data,
        }

        return Response(data)

    @action(methods=["get"], detail=True, url_path="works/(?P<work_id>[^/.]+)")
    def single_works(self, request, work_id, *args, **kwargs):
        file = self.get_object()
        source = get_source(file)
        works_qs = get_object_or_404(Work, source=source, pk=work_id)
        work_serializer = WorkSerializer(works_qs)

        return Response(work_serializer.data)
