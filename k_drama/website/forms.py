from django import forms
from website.models import Show, Actor, User, Admin, Award

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        
class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'
        