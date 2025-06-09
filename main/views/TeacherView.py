from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from main.models.TeacherModel import TeacherModel
from main.serializers.TeacherSerializer import TeacherSerializer


class TeacherAPIView(CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = TeacherSerializer

class TeacherListAPIView(ListAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer



class TeacherUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer