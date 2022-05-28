from django.urls import path
from .views import GetWorkspaces, CreateWorkspace, RetrieveUpdateWorkspace

urlpatterns = [
    path('create/', CreateWorkspace.as_view()),
    path('', GetWorkspaces.as_view()),
    path('<int:user>/', RetrieveUpdateWorkspace.as_view()),
]

