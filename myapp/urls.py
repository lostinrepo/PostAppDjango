from django.urls import path,include
from .views import HomePage,AboutPage,PostDetail,CreatePost,UpdatePost,DeletePost

urlpatterns = [
    path("",HomePage.as_view(),name="home"),
    path("post/<int:pk>/",PostDetail.as_view(),name="post_detail"),
    path("post/new/",CreatePost.as_view(),name="post_new"),
    path("post/<int:pk>/edit",UpdatePost.as_view(),name="post_edit"),
    path("post/<int:pk>/delete",DeletePost.as_view(),name="post_delete"),
    path("about/",AboutPage.as_view(),name="about"),
]