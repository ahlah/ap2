from django import forms

class ReservationForm(forms.Form):
    adults = forms.IntegerField(min_value=1)
    children = forms.IntegerField(min_value=0)
    checkin = forms.DateField(required=True)
    checkout = forms.DateField(required=True)

class ReviewForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    rating = forms.DecimalField(max_digits=2, min_value=0.5, max_value=5.0)
