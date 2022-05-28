from rest_framework import serializers
from .models import ActivityLog

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(ActivityLogSerializer, self).to_representation(instance)
        rep['user'] = instance.user.name
        return rep
