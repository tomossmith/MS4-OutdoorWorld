from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
]
