from django import forms

from cities.models import City


# шаблон для нашей формы
class HtmlForm(forms.Form):
    name = forms.CharField(label='Город')


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', )


