from django.urls import path
from . import views

app_name = 'Gym'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:question_id>/',views.detail, name = 'detail'),
    path('<int:question_id>/summary',views.summary, name = 'summary'),
    path('<int:question_id>/record/',views.record, name = 'record')
]