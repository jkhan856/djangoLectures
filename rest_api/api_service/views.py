from api_service.serializers import PlayListSerializer
from rest_framework import generics
from api_service.models import PlayList
# Create your views here.
#RetrieveUpdateDestroyAPIView
#ListCreateAPIView

class PlayListAllView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PlayListSerializer

    def get_queryset(self):
        return PlayList.objects.all()

class PlayListCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = PlayListSerializer
    queryset = PlayList.objects.all()

class PlayListRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PlayListSerializer
    queryset = PlayList.objects.all()
