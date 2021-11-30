from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),

    path('create-project/', views.createProject, name="create-project"),

    path('create-product/', views.createProduct, name="create-product"),


    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
]
