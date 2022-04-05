""" Blog App - urls.py """
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', views.add_post, name="add_post"),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:post_id>/', views.edit_post, name="edit_post"),
    path('delete_post/<int:post_id>/', views.delete_post, name="delete_post"),
    path('delete_comment/<int:comment_id>/',
         views.delete_comment, name="delete_comment"),
]
