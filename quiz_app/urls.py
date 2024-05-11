from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_topic, name='select_topic'),
    path('ask/<int:question_id>/', views.ask_questions, name='ask_questions'),
    path('check_answer/', views.check_answer, name='check_answer'),
]
