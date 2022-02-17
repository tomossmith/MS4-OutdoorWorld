from django.urls import path
from . import views

urlpatterns = [
    path('', views.postlist.as_view(), name='home'),
    #path('<int:post_id>/', views.post_detail, name='post_detail'),
]
