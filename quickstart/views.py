from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User , Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer , GroupSerizlizer


class UserViewSet(viewsets.ModelViewSet):
    '''
    api 允许用户去查看或编辑
    '''
    queryset = User.objects.all().order_by('-date_joinded')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerizlizer

