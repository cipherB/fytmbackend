from rest_framework import serializers
from .models import Card, CheckList, Attachment, Comments

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

        # def to_representation(self, instance):
        #     rep = super(CardSerializer, self).to_representation(instance)
        #     rep['board'] = instance.board.id
        #     return rep

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"

        # def to_representation(self, instance):
        #     rep = super(AttachmentSerializer, self).to_representation(instance)
        #     rep['card'] = instance.card.id
        #     return rep

class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"

        # def to_representation(self, instance):
        #     rep = super(CheckListSerializer, self).to_representation(instance)
        #     rep['card'] = instance.card.id
        #     return rep

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
