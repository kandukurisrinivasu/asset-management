from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('', views.login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('edituser/', views.edituser, name="edituser"),
    path("update/<str:username>/", views.update, name="update"),



    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html') ,name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')
]