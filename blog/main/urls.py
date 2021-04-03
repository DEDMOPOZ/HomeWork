from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home_page"),
    path("posts", views.posts, name="posts"),
    path("posts/create", views.post_create, name="post_create"),
    path("api/posts", views.api_response, name="api_response"),
    path("about", views.about, name="about"),
]
