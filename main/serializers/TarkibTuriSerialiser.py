from rest_framework.serializers import ModelSerializer

from main.models.TarkibTuriModel import TarkibTuriModel


class TarkibTuriSerializer(ModelSerializer):
    class Meta:
        model = TarkibTuriModel
        fields = '__all__'