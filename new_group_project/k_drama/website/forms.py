from django import forms
from website.models import Show, Actor, Award, Character

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'

class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        widgets = {
            '': forms.Select(attrs={'class': 'form-control'}),
        }
        
class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['actor'].queryset = Actor.objects.all()