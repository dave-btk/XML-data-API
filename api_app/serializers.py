from rest_framework import serializers
from .models import SchoolModel


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = ['id', 'name', 'roll', 'city']
