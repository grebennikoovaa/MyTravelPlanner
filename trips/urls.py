from django.urls import path
from . import views

urlpatterns = [
    path('', views.TripListView.as_view(), name='trip_list'),
    path('trips/<int:pk>/', views.TripDetailView.as_view(), name='trip_detail'),
    path('trips/create/', views.TripCreateView.as_view(), name='trip_create'),
    path('trips/<int:pk>/edit/', views.TripUpdateView.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', views.TripDeleteView.as_view(), name='trip_delete'),
    

    path('trips/<int:trip_id>/add-destination/', views.add_destination, name='add_destination'),
    path('destinations/', views.destination_list, name='destination_list'),
    

    path('trips/<int:trip_id>/like/', views.like_trip, name='like_trip'),
    path('trips/<int:trip_id>/save/', views.save_trip, name='save_trip'),
    path('trips/<int:trip_id>/comment/', views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('saved/', views.saved_trips, name='saved_trips'),
]

