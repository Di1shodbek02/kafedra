from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from main.models.KafedraFanModel import KafedraFanModel
from main.serializers.KafedraFanSerializer import KafedraFanSerializer


class AddKafedraFanView(CreateAPIView):
    queryset = KafedraFanModel.objects.all()
    serializer_class = KafedraFanSerializer


class KafedraFanDelete(RetrieveUpdateDestroyAPIView):
    queryset = KafedraFanModel.objects.all()
    serializer_class = KafedraFanSerializer


class KafedraFanList(ListAPIView):
    queryset = KafedraFanModel.objects.all()
    serializer_class = KafedraFanSerializer

