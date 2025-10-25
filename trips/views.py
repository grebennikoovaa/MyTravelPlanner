from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required  # ← THIS WAS MISSING
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from .models import Trip, Destination, TripDay, DayDestination
from .forms import TripForm, DestinationForm

class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'
    paginate_by = 12

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Trip.objects.filter(
                Q(owner=self.request.user) | 
                Q(privacy='public')
            ).distinct().select_related('owner')
        else:
            return Trip.objects.filter(privacy='public').select_related('owner')

class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Trip.objects.filter(
                Q(owner=self.request.user) | 
                Q(privacy='public')
            ).distinct()
        else:
            return Trip.objects.filter(privacy='public')

class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        # Create first day automatically
        if self.object.days.count() == 0:
            TripDay.objects.create(
                trip=self.object,
                date=self.object.start_date,
                day_number=1
            )
        return response
    
    def get_success_url(self):
        return reverse_lazy('trip_detail', kwargs={'pk': self.object.pk})

class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'
    
    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('trip_detail', kwargs={'pk': self.object.pk})

class TripDeleteView(LoginRequiredMixin, DeleteView):
    model = Trip
    template_name = 'trips/trip_confirm_delete.html'
    success_url = reverse_lazy('trip_list')
    
    def get_queryset(self):
        return Trip.objects.filter(owner=self.request.user)

# Destination views
@login_required
def add_destination(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id, owner=request.user)
    
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.created_by = request.user
            destination.save()
            
            # Add to first day of trip
            first_day = trip.days.first()
            if first_day:
                DayDestination.objects.create(
                    trip_day=first_day,
                    destination=destination,
                    order=first_day.destinations.count() + 1
                )
                messages.success(request, f'Destination "{destination.name}" added to your trip!')
            else:
                messages.error(request, 'No days available in this trip.')
            
            return redirect('trip_detail', pk=trip_id)
    else:
        form = DestinationForm()
    
    return render(request, 'trips/destination_form.html', {
        'form': form,
        'trip': trip
    })

@login_required
def destination_list(request):
    destinations = Destination.objects.filter(created_by=request.user)
    return render(request, 'trips/destination_list.html', {
        'destinations': destinations
    })