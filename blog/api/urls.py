from django.urls import path

from .views import (
    api_detail_blog_view,
    api_title_post,
    api_title_delete,
    api_title_edit,
    example_view
)

app_name = 'blog'

urlpatterns = [
    path('post/', api_title_post, name='post'),
    path('<slug>/', api_detail_blog_view, name='detail'),
    path('<slug>/delete/', api_title_delete, name='delete'),
    path('<slug>/update/', api_title_edit, name='update'),
    path('example/', example_view, name='example')
]