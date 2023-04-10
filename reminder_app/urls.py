from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_reminder, name='add_reminder'),
    path('delete/<int:pk>', views.delete_reminder, name='delete_reminder')
]
