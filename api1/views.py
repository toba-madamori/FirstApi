from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    #authentication_classes = [SessionAuthentication, BaseAuthentication]
    authentication_classes= [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer    
    #authentication_classes= [SessionAuthentication, BaseAuthentication]
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated]