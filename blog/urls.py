from django.urls import path
from blog import views
from blog.views import AboutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, DraftListView, publish_post, add_comment, remove_comment, approve_comment_view

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('about/', AboutView.as_view(), name="about"),
    path('post/<slug:pk>', PostDetailView.as_view(), name="post_detail" ),
    path('post/create/', PostCreateView.as_view(), name="post_create"),
    path('post/<slug:pk>/edit', PostUpdateView.as_view(), name="post_edit"),
    path('post/<slug:pk>/delete', PostDeleteView.as_view(), name="post_delete"),
    path('post_drafts/', DraftListView.as_view(), name="drafts"),
    path('post/<slug:pk>/publish', views.publish_post, name="post_publish"),
    path('post/<slug:pk>/add_comment', views.add_comment, name="add_comment"),
    path('post/<slug:pk>/remove_comment', views.remove_comment, name="remove_comment"),
    path('post/<slug:pk>/approve_comment', views.approve_comment_view, name="approve_comment"),
]
