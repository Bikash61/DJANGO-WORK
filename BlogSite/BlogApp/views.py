from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Handle form submission here (e.g., send an email)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
