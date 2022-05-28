from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

User = get_user_model()

# Create your views here.

# register an account
# class RegisterAccount(CreateAPIView):
#     permission_classes = (permissions.AllowAny,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class RegisterAccount(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        phone_number = data['phone_number']
        password = data['password']

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'})
        else:
            user = User.objects.create_user(email=email, name=name, phone_number=phone_number, password=password)
            user.save()
            user_id = User.objects.get(email=email).id
            return Response({
                'success': 'user created successfully',
                'user': {
                    'user_id': user_id,
                    'email': email,
                    'name': name,
                    'phone_number': phone_number,
                }
            })

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

# get all users
class GetUsers(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUpdateUser(MultipleFieldLookupMixin, RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['email',]
