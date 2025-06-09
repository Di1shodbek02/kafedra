from django.urls import path

from main.views.FanQushimchaModel import AddFanQushimchaAPIView
from main.views.FanView import AddFanAPIView, FanListAPIView, FanUpdateAPIView
from main.views.KafedraFanView import AddKafedraFanView, KafedraFanDelete, KafedraFanList
from main.views.KafedraView import AddKafedraAPIView, KafedraListAPIView, KafedraDetailAPIView, KafedraUpdateView
from main.views.QushimchalarView import AddQushimchalarView
from main.views.TarkibTuriView import TarkibTuriView
from main.views.TeacherView import TeacherAPIView, TeacherListAPIView, TeacherUpdateAPIView

urlpatterns = [
    path('fan/<int:pk>/update', FanUpdateAPIView.as_view(), name='fan-update'),
    path('kafedra-fan-list/', KafedraFanList.as_view(), name='kafedra-fan-list'),
    path('delete-kafedra-fan/<int:pk>/', KafedraFanDelete.as_view(), name='kafedra-fan-delete'),
    path('kafedra/<int:pk>/update/', KafedraUpdateView.as_view(), name='kafedra-update'),
    path('teacher/<int:pk>/update/', TeacherUpdateAPIView.as_view(), name='teacher-update'),
    path('add-teacher/', TeacherAPIView.as_view(), name='add_teacher'),
    path('list-kafedra/', KafedraListAPIView.as_view(), name='list_kafedra'),
    path('id-kafedra-detail<int:pk>/', KafedraDetailAPIView.as_view(), name='id_kafedra'),
    path('add-kafedra/', AddKafedraAPIView.as_view(), name='add_kafedra'),
    path('add-fan/', AddFanAPIView.as_view(), name='add_fan'),
    path('fan-list/', FanListAPIView.as_view(), name='fan_list'),
    path('teacher-list/', TeacherListAPIView.as_view(), name='teacher_list'),
    path("fan-qo'shimcha/", AddFanQushimchaAPIView.as_view(), name='fan_qushimcha'),
    path("add-qo'shimchalar/", AddQushimchalarView.as_view(), name='add_qushimchalar'),
    path('add-kafedra-fan/', AddKafedraFanView.as_view(), name='add_kafedra_fan'),
    path('add-tarkib-tur/', TarkibTuriView.as_view(), name='add_tarkib'),
]
