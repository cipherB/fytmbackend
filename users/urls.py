from django.urls import path
from .views import GetUsers, RegisterAccount, RetrieveUpdateUser

urlpatterns = [
    path('register/', RegisterAccount.as_view()),
    path('', GetUsers.as_view()),
    path('<str:email>/', RetrieveUpdateUser.as_view()),
]

