"""Define the URL pattern for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'topics', views.topics, name='topics'),
    path(r'topics/<topic_id>/', views.topic, name='topic'),
]
