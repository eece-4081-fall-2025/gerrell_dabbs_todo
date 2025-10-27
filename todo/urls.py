from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("<int:task_id>/complete/", views.task_complete, name="task_complete"),
]
