from django.shortcuts import render, redirect
from django.db.models import Count
from django.views import View
from .models import Product, Customer, Cart
from .forms import CustomerRegistrationForm , CustomerProfileForm 
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.http import JsonResponse
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
        try:
            customer = Customer.objects.get(user=request.user)
            form = CustomerProfileForm(instance=customer)
        except Customer.DoesNotExist:
            form = CustomerProfileForm()  # or handle it differently
        return render(request, 'app/profile.html', {'form': form})

    def post(self, request):
        try:
            customer = Customer.objects.get(user=request.user)
            form = CustomerProfileForm(request.POST, instance=customer)
        except Customer.DoesNotExist:
            form = CustomerProfileForm(request.POST)
            if form.is_valid():
                # Manually set the user before saving
                new_customer = form.save(commit=False)
                new_customer.user = request.user
                new_customer.save()
                messages.success(request, 'Profile Created Successfully')
                return redirect('profile')
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')  # Redirect to avoid form resubmission
        else:
            messages.warning(request, 'Invalid Input Data')

        return render(request, 'app/profile.html', {'form': form})

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html',locals())

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    if product_id:
        try:
            product = Product.objects.get(id=product_id)
            Cart(user=user, product=product).save()
            messages.success(request, 'Product added to cart.')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found.')
    else:
        messages.error(request, 'No product ID provided.')
    return redirect('/cart')


def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user = request.user)
    amount = 0
    for p in cart:
        value = p.quantity*p.product.discounted_price
        amount = amount+value
    totalamount = amount + 40
    return render(request, 'app/addtocart.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET('prod_id')
        c = cart.objects.get(Q(product = prod_id)& Q(request = request.user))
        c.quantity += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user = request.user)
        for p in cart:
            value = p.quantity*p.product.discounted_price
            amount = amount+value
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)