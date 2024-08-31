from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm,MyPasswordChangeForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
    path('category/<str:val>/', views.CategoryView.as_view(), name='category'),
    path('category-title/<val>/', views.CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('address/', views.address, name = 'address'),
    #Login Authentication
    path('customerregistration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name='login'),
    path('password-reset/' , auth_view.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class = MyPasswordResetForm), name = 'password_reset'),
   path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='app/changepassword.html',
        success_url='/passwordchangedone/',
        form_class=MyPasswordChangeForm
    ), name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'
    ), name='passwordchangedone'),
path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

