from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('board_a/', views.ArticleAView.as_view()),
    path('board_a/<int:id>/',views.ArticleAView.as_view()),
    path('board_b/', views.ArticleBView.as_view()),
    path('board_b/<int:id>/',views.ArticleBView.as_view()),
    path("comment/", views.CommentView.as_view()),
    path("comment/<int:article_id>/", views.CommentView.as_view()),
    path("like/", views.LikeView.as_view()),
]