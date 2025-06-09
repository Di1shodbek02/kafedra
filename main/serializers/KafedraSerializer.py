from rest_framework.serializers import ModelSerializer

from main.models.FanModel import FanModel
from main.models.KafedraFanModel import KafedraFanModel
from main.models.KafedraModel import KafedraModel
from main.models.TeacherModel import TeacherModel


class KafedraSerializer(ModelSerializer):
    class Meta:
        model = KafedraModel
        fields = '__all__'


class FanSerializer(ModelSerializer):
    class Meta:
        model = FanModel
        fields = ['id', 'name', 'talim_yunalishi']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['id', 'name']


class KafedraDetailSerializer(ModelSerializer):
    fanlar = FanSerializer(many=True)
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = KafedraModel
        fields = ['id', 'name', 'fanlar', 'teachers']
