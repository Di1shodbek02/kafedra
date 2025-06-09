from rest_framework.generics import CreateAPIView, UpdateAPIView

from main.models.KafedraFanModel import KafedraFanModel
from main.models.KafedraModel import KafedraModel
from main.serializers.KafedraFanSerializer import KafedraFanSerializer


class AddKafedraFanView(CreateAPIView):
    queryset = KafedraFanModel.objects.all()
    serializer_class = KafedraFanSerializer


class KafedraUpdateView(UpdateAPIView):
    queryset = KafedraModel.objects.all()
    serializer_class = KafedraFanSerializer


