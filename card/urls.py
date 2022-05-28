from django.urls import path
from .views import (
    GetCards, 
    GetAllAttachment, 
    GetCheckList, 
    GetImagesAttachment, 
    GetFilesAttachment, 
    GetLinksAttachment, 
    RetrieveUpdateDeleteCard,
    CreateCard,
    CreateCheckList,
    CreateAttachment,
    UpdateCheckList,
    DeleteChecklist,
    DeleteAttachment,
    CreateComment,
    GetComments,
)

urlpatterns = [
    path('create/', CreateCard.as_view()),
    path('create-checklist/', CreateCheckList.as_view()),
    path('create-attachment/', CreateAttachment.as_view()),
    path('', GetCards.as_view()),
    path('checklists/', GetCheckList.as_view()),
    path('attachments/', GetAllAttachment.as_view()),
    path('attachments/images', GetImagesAttachment.as_view()),
    path('attachments/files', GetFilesAttachment.as_view()),
    path('attachments/links', GetLinksAttachment.as_view()),
    path('<int:id>/', RetrieveUpdateDeleteCard.as_view()),
    path('update-checklist/<int:id>/', UpdateCheckList.as_view()),
    path('delete-checklist/<int:id>/', DeleteChecklist.as_view()),
    path('delete-attachment/<int:id>/', DeleteAttachment.as_view()),
    path('create-comment/', CreateComment.as_view()),
    path('comments/', GetComments.as_view()),
]

