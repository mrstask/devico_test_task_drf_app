from django.urls import path

from user import views

urlpatterns = [
    path('account/', views.UserList.as_view()),
    path('account/<int:pk>/activity/', views.UserDetail.as_view()),
]