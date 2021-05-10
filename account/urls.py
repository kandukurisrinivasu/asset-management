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

    path("asset_search/", views.asset_search, name="asset_search"),
    path("asset_search_display/", views.asset_search_display, name="asset_search_display"),
    path("", views.add_asset, name="add_asset"),
    path('export', views.export_xls, name='export'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
    path('import_xls', views.import_xls, name='import_xls'),
    path('calendar_test', views.calendar_test, name='calendar_test'),
    path('event/new/', views.create_lab_event, name='event_new'),
    path('event/<int:event_id>/details/', views.lab_event_details, name='event-detail'),
    path("feedback/", views.feedback, name="feedback"),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 #   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
