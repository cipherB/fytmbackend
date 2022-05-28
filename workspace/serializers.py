from rest_framework import serializers
from .models import Workspace

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ["id",  "name", "user"]

    # def to_representation(self, instance):
    #     rep = super(WorkspaceSerializer, self).to_representation(instance)
    #     rep['user'] = instance.user._id
    #     return rep
