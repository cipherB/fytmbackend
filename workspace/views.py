from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from .models import Workspace
from .serializers import WorkspaceSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

# register an account
class CreateWorkspace(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


# get all workspace
class GetWorkspaces(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: 
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

class RetrieveUpdateWorkspace(MultipleFieldLookupMixin, RetrieveUpdateAPIView):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    lookup_fields = ['user',]
