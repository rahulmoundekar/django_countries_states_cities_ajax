from django.forms import forms

from countries_states_cities_ajax.models import Country, State, City


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
