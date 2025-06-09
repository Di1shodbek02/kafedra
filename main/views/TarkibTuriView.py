from rest_framework.generics import CreateAPIView

from main.models.TarkibTuriModel import TarkibTuriModel
from main.serializers.TarkibTuriSerialiser import TarkibTuriSerializer


class TarkibTuriView(CreateAPIView):
    queryset = TarkibTuriModel.objects.all()
    serializer_class = TarkibTuriSerializer