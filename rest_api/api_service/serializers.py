from api_service.models import PlayList
from rest_framework import serializers

class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields ='__all__'
