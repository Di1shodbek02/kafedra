from rest_framework.generics import CreateAPIView

from main.models.QushimchalarModel import QushimchalarModel
from main.serializers.QushimchalarSerializer import QushimchalarSerializer


class AddQushimchalarView(CreateAPIView):
    queryset = QushimchalarModel.objects.all()
    serializer_class = QushimchalarSerializer