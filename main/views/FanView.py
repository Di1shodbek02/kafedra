from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from main.models.FanModel import FanModel
from main.serializers.FanSerialiser import FanSerializer


class AddFanAPIView(CreateAPIView):
    queryset = FanModel.objects.all()
    serializer_class = FanSerializer


class FanListAPIView(ListAPIView):
    queryset = FanModel.objects.all()
    serializer_class = FanSerializer

class FanUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FanModel.objects.all()
    serializer_class = FanSerializer