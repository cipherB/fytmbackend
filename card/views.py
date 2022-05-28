from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, UpdateAPIView
from .models import Card, CheckList, Attachment, Comments
from .serializers import CardSerializer, CheckListSerializer, AttachmentSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

# create a card
class CreateCard(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# create an attachment
class CreateAttachment(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

# create a checklist
class CreateCheckList(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer



# get all cards
class GetCards(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# get all attachment
class GetAllAttachment(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

# get all images attachment
class GetImagesAttachment(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Attachment.imageObjects.all()
    serializer_class = AttachmentSerializer

# get all files attachment
class GetFilesAttachment(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Attachment.fileObjects.all()
    serializer_class = AttachmentSerializer

# get all links attachment
class GetLinksAttachment(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Attachment.linkObjects.all()
    serializer_class = AttachmentSerializer

# get all checklists
class GetCheckList(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer

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

class RetrieveUpdateDeleteCard(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_fields = ['id',]

#update checklist 
class UpdateCheckList(MultipleFieldLookupMixin, UpdateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer
    lookup_fields = ['id',]

#delete checklist
class DeleteChecklist(MultipleFieldLookupMixin, DestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = CheckList.objects.all()
    serializer_class = CheckList
    lookup_fields = ['_id',]

#delete attachment
class DeleteAttachment(MultipleFieldLookupMixin, DestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    lookup_fields = ['_id',]

#create a comment
class CreateComment(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class GetComments(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
