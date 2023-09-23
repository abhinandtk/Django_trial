from django.urls import path
from .import views


urlpatterns = [
    path('mainproject/',views.projects,name="projects"),
    path('project_two/<str:pk>/',views.project,name="project"),
    path('project/',views.project_two,name="project_two"),
]
