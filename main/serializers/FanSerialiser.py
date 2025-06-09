from rest_framework.serializers import ModelSerializer

from main.models.FanModel import FanModel


class FanSerializer(ModelSerializer):
    class Meta:
        model = FanModel
        fields = '__all__'
