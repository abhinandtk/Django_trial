from django.urls import path
from .import views


urlpatterns = [
    path('',views.projects,name="projects"),
    path('project_two/<str:pk>/',views.project_two,name="project_two"),
    path('project/<str:pk>/',views.project,name="project"),
]
