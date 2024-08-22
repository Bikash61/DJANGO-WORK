from django.shortcuts import render

# path('login/', views.login, name = 'login'),
#     path('profile/', views.profile, name = 'profile'),
#     path('signup', views.signup, name = 'signup'),
#     path('blog/', views.blog, name = 'blog')

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    return render(request, 'signup.html')

def blog(request):
    return render(request, 'blog.html')

def login(request):
    return render(request, 'login.html')