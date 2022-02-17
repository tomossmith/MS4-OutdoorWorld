from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist.as_view(), name='blog'),
    path('<int:;post_id/', views.PostDetail.as_view, name='post_detail'),
]
