from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View
from .models import Product
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Function-based views
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

# Class-based views
class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app/customerregistration.html", {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Congratulations! User Registered Successfully')
            return redirect('home')  # Redirect to home or any other page after successful registration
        else:
            messages.warning(request, 'Invalid Input Data')
            return render(request, "app/customerregistration.html", {'form': form})

class ProfileView(View):
    def get(self, request):
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        return render(request, 'app/profile.html', locals())
        
