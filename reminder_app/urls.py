from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_reminder, name='add_reminder'),
    path('delete/<reminder_id>', views.delete_reminder, name='delete_reminder'),
    path('<int:reminder_id>', views.show_reminder, name='show_reminder')
]
