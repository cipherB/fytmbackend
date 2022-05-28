from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

    # def to_representation(self, instance):
    #     rep = super(BoardSerializer, self).to_representation(instance)
    #     rep['members'] = instance.members.email
    #     return rep
