"""
URL configuration for final_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from QuizMaster import views as quiz_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('QuizMaster.urls')),
    path('', quiz_view.select_topic, name='select_topic'), 
    path('topic/<int:topic_id>/', quiz_view.ask_questions, name='ask_questions'),
    
]
