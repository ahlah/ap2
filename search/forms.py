from django import forms

class SearchForm(forms.Form):
    query = forms.CharField()
    sort = forms.ChoiceField(choices=[
        ('pa', 'price ascending'),
        ('pd', 'price descending'),
        ('ra', 'rating ascending'),
        ('rd', 'price ascending'),
    ])

class FilterByCityForm(forms.Form):
    query = forms.ChoiceField(choices =[
        ('del', 'Delhi'),
        ('mum','Mumbai'),
        ('kol','Kolkata'),
        ('ben','Bengaluru'),
        ('lon','London'),
        ('nyc','New York'),
        ('par','Paris'),
        ('tok','Tokyo'),
    ])
