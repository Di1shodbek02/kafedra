from rest_framework.serializers import ModelSerializer

from main.models.KafedraFanModel import KafedraFanModel


class KafedraFanSerializer(ModelSerializer):
    class Meta:
        model = KafedraFanModel
        fields = '__all__'