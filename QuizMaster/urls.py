from django.urls import path
from . import views

urlpatterns = [
    path('topics/', views.select_topic, name='select_topic'),
    path('quiz/<int:topic_id>/', views.ask_questions, name='ask_questions'),
    path('result/', views.quiz_result, name='quiz_result'),
]

