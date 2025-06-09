from rest_framework.generics import CreateAPIView

from main.models.FanQushimchaModel import FanQushimchaModel
from main.serializers.FanQushimchaSerialiser import FanQushimchaSerializer


class AddFanQushimchaAPIView(CreateAPIView):
    serializer_class = FanQushimchaSerializer
    queryset = FanQushimchaModel.objects.all()