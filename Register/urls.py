from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import PasswordChangeView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', views.register_user, name='signup'),
    path('add_user/',views.add_user,name='register'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout, name="logout"),
    path('edituser/', views.edituser, name="edituser"),
    path("update/<str:username>", views.update, name="update"),
    path("password_change/",PasswordChangeView.as_view(template_name='registration/password_change.html'), name="passchange"),


    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html') ,name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete')
]