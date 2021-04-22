from django.urls import path
from .import views
#from BoschEBBAsset.BoschEBBAsset import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('',views.home,name="homepage"),
    #path('Dashboard/', views.Dashboard,name="Dashboard"),
    #path('Register/',LoginView.as_view(),name='login_url'),
    #path('register/', views.register,name="register_url"),
    #path('logout/',LogoutView.as_view(next_page='Dashboard'),name="logout"),

    path('', views.regform, name='registration form'),
    path('update/', views.updateProfile, name='updateform')
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 #   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
