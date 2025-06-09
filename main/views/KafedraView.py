from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.KafedraModel import KafedraModel
from main.serializers.KafedraSerializer import KafedraSerializer, KafedraDetailSerializer


class AddKafedraAPIView(CreateAPIView):
    queryset = KafedraModel.objects.all()
    serializer_class = KafedraSerializer



class KafedraDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            kafedra = KafedraModel.objects.get(id=pk)
        except KafedraModel.DoesNotExist:
            return Response({'detail': 'Kafedra topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = KafedraDetailSerializer(kafedra)
        return Response(serializer.data)


class KafedraListAPIView(ListAPIView):
    queryset = KafedraModel.objects.all()
    serializer_class = KafedraSerializer


class KafedraUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = KafedraModel.objects.all()
    serializer_class = KafedraSerializer
