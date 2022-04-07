from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,\
    PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    #All user paths we need for create,login and logout.
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout'),
    #In those lines under we have the solution with the forgoten password.Etc.
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_complete'),
]
