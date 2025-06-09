from rest_framework.serializers import ModelSerializer

from main.models.FanQushimchaModel import FanQushimchaModel


class FanQushimchaSerializer(ModelSerializer):
    class Meta:
        model = FanQushimchaModel
        fields = '__all__'