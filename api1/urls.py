from django.urls import path, include
from .views import ArticleListView, ArticleDetailView, ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')


urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    path('article/', ArticleListView.as_view(), name= 'article'),
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name= 'article_detail'),
]