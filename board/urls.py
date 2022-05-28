from django.urls import path
from .views import GetBoards, CreateBoard, RetrieveUpdateBoard, chart_stats

urlpatterns = [
    path('create/', CreateBoard.as_view()),
    path('', GetBoards.as_view()),
    path('<int:id>/', RetrieveUpdateBoard.as_view()),
    path('<int:id>/chart', chart_stats),
]

