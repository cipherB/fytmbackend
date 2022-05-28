from django.urls import path
from .views import AllActivities, WorkspaceActivities, BoardActivities, CardActivities, CreateActivityLog

urlpatterns = [
    path('', AllActivities.as_view()),
    path('workspace/', WorkspaceActivities.as_view()),
    path('board/', BoardActivities.as_view()),
    path('card/', CardActivities.as_view()),
    path('create/', CreateActivityLog.as_view()),
]

