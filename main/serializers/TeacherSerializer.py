from rest_framework.serializers import ModelSerializer

from main.models.TeacherModel import TeacherModel


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'

