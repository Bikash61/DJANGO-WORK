# blog/urls.py
from django.urls import path
from .views import ProtectedView, PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
