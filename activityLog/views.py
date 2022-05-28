from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import ActivityLog
from .serializers import ActivityLogSerializer

# Create your views here.

# create an activity
class CreateActivityLog(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

# get all activities
class AllActivities(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

#get workspace activities
class WorkspaceActivities(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ActivityLog.workspaceObjects.all()
    serializer_class = ActivityLogSerializer

#get board activities
class BoardActivities(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ActivityLog.boardObjects.all()
    serializer_class = ActivityLogSerializer

#get card activities
class CardActivities(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = ActivityLog.cardObjects.all()
    serializer_class = ActivityLogSerializer



