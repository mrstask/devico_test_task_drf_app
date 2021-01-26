from django.urls import path

from social import views

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetails.as_view()),
    path('post/analytics/', views.PostAnalytics.as_view()),
]