from django import forms
from website.models import Show, User

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'