from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.home),
    path('api/ceb/', views.ceb_list),
    path('api/ceb_bill_data/<str:pk>/', views.ceb_bill_data),
    path('api/nwsdb_bill_data/<str:pk>/', views.nwsdb_bill_data),
    path('api/get_average/<str:pk>/', views.get_average),
    path('api/ceb/create/', views.ceb_create),
    path('api/update/<str:pk>/', views.update),
]