from django.contrib.postgres import fields
from rest_framework.serializers import ModelSerializer
from repertoire.models import File, Work


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"