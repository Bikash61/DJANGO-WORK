from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name = 'home'), 
    path('joblist/', views.joblist, name = 'joblist'),
    path('postdetail/', views.postdetail, name = 'postdetail'),
    path('internship/',views.internship, name = 'internship'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
