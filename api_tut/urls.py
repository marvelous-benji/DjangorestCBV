from django.urls import path
from .views import ArticleView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('atricle/detail/<int:id>', ArticleDetailView.as_view()),
]
