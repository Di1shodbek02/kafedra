from rest_framework.serializers import ModelSerializer

from main.models.QushimchalarModel import QushimchalarModel


class QushimchalarSerializer(ModelSerializer):
    class Meta:
        model = QushimchalarModel
        fields = '__all__'