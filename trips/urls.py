from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripListView.as_view(), name='trip_list'),
    path('trips/<int:pk>/', views.TripDetailView.as_view(), name='trip_detail'),
    path('trips/create/', views.TripCreateView.as_view(), name='trip_create'),
    path('trips/<int:pk>/edit/', views.TripUpdateView.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', views.TripDeleteView.as_view(), name='trip_delete'),
    
    # Destination routes
    path('trips/<int:trip_id>/add-destination/', views.add_destination, name='add_destination'),
    path('destinations/', views.destination_list, name='destination_list'),
]