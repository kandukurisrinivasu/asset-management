from django.urls import path
from .import views
from django.urls import path, re_path
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
    path('add', views.add_asset, name="add_asset"),
    path('setup', views.setup, name="setup"),
    path('export', views.export_xls, name='export'),
    path('export_pdf', views.export_pdf, name='export_pdf'),
    path('import_xls', views.import_xls, name='import_xls'),
    path('calendar_test', views.calendar_test, name='calendar_test'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path("feedback/", views.feedback, name="feedback"),
    path('table/',views.table,name='tablepage'),
    path('table1/',views.setup_display,name='setuptable'),
    path('content/',views.setup_book,name='bookevent'),
    path('settings/',views.settings,name='settings'),
    path('delete_asset/<int:id>',views.delete_asset),
    path('edit_asset/<int:id>', views.edit_asset,name='edit_asset'),
    path('delete_setup/<int:id>', views.delete_setup),
    path('edit_setup/<int:id>', views.edit_setup),
    # Matches any html file
    path('', views.index, name='home'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
 #   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
