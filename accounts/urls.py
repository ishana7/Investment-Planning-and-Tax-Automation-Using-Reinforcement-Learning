from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('blog/', views.about, name='blog'),
    path('what-is-ai/', views.whatisai, name='what-is-ai'),
    path('job-loss/', views.jobloss, name='job-loss'),
    path('ml-ai/', views.mlai, name='ml-ai'),
    path('income-tax/', views.incometax, name='income-tax'),
    path('never-search-again/', views.neversearchagain, name='never-search-again'),
    path('ai-value-prop/', views.aivalueprop, name='ai-value-prop'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('reset_password/', PasswordResetView.as_view(template_name='accounts/reset_password.html', email_template_name='accounts/reset_password_email.html', success_url='done/'), name='reset-password'),
    path('reset_password/done/', PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'), name='reset_password_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'), name='reset_password_confirm'),
    path('reset_password/complete/', PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'), name='reset_password_complete'),

]
