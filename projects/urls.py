from django.urls import path
from . import views


urlpatterns = [
    path('', views.projects, name="projects"),

    path('archived-projects', views.archivedProjects, name="archived-projects"),

    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('archive-project/<str:pk>/', views.archiveProject, name="archive-project"),
    
    path('restore-project/<str:pk>/', views.restoreArchivedProject, name="restore-project"),
]