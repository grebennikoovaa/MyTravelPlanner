from django import forms
from .models import Trip, Destination, TripComment, DestinationRating

class TripForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = Trip
        fields = ['title', 'description', 'start_date', 'end_date', 'privacy']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'privacy': forms.Select(attrs={'class': 'form-control'}),
        }

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'description', 'address', 'city', 'country', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Place name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', 'Select category'),
                ('landmark', 'Landmark'),
                ('restaurant', 'Restaurant'),
                ('hotel', 'Hotel'),
                ('museum', 'Museum'),
                ('park', 'Park'),
                ('shop', 'Shop'),
                ('other', 'Other')
            ]),
        }

class TripCommentForm(forms.ModelForm):
    class Meta:
        model = TripComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Share your thoughts about this trip...'
            }),
        }

# ЗАКОММЕНТИРУЙТЕ ЭТУ ФОРМУ ПОКА ЧТО:
'''
class DestinationRatingForm(forms.ModelForm):
    class Meta:
        model = DestinationRating
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Share your experience...'
            }),
        }
'''